from PyQt5.QtCore import QThreadPool, QRunnable, pyqtSignal, QObject
import traceback

class BackgroundTaskRunner(QObject):
    """
    用于在后台线程中运行任务的类，避免阻塞主线程。

    信号:
        task_finished: 任务完成时发出信号，携带任务的结果 (可以是任何 Python 对象)。
        error: 任务执行出错时发出信号，携带错误信息。
    """
    task_finished = pyqtSignal(object)  # 任务完成信号，携带结果
    error = pyqtSignal(str)         # 错误信号，携带错误信息

    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool.globalInstance() # 使用全局线程池

    class _BackgroundTask(QRunnable): # 内部类，用于封装后台任务
        def __init__(self, func, args, kwargs, parent):
            super().__init__()
            self.func = func
            self.args = args
            self.kwargs = kwargs
            self.parent = parent # 指向 BackgroundTaskRunner 实例，用于发送信号

        def run(self):
            """
            在线程中执行任务。
            """
            try:
                result = self.func(*self.args, **self.kwargs) # 执行传入的函数
                self.parent.task_finished.emit(result) # 任务成功完成，发送 task_finished 信号
            except Exception as e:
                error_msg = traceback.format_exc() # 获取完整的错误信息，包括堆栈跟踪
                self.parent.error.emit(error_msg) # 任务出错，发送 error 信号

    def run(self, func, *args, **kwargs):
        """
        启动后台任务。

        Args:
            func: 要在后台执行的函数。
            *args: 传递给 func 的位置参数。
            **kwargs: 传递给 func 的关键字参数。
        """
        task = self._BackgroundTask(func, args, kwargs, self) # 创建后台任务
        self.threadpool.start(task) # 将任务放入线程池执行