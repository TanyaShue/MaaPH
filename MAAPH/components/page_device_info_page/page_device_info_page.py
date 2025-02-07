from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QScrollArea
from siui.components.widgets.scrollarea import SiScrollArea

from MAAPH.components.option_card import OptionCardPlaneForWidgetDemos
from siui.components import SiPushButton
from siui.components.option_card import SiOptionCardLinear, SiOptionCardPlane
from siui.components.page import SiPage
from siui.components.progress_bar import SiProgressBar
from siui.components.titled_widget_group import SiTitledWidgetGroup
from siui.components.widgets import (
    SiDenseHContainer,
    SiDenseVContainer,
    SiLabel
)
from siui.components.widgets.timeline import SiTimeLine, SiTimeLineItem
# 假设 SiColor 已经定义，你也可以自行替换为具体颜色代码
from siui.core import SiColor
from siui.core import SiGlobal, Si


class ExampleDeviceInfoPage(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 设置页面整体属性
        self.setPadding(64)
        # 增加页面宽度以适应三个面板（左侧、操作面板、右侧日志面板）
        self.setScrollMaximumWidth(1600)
        self.setScrollAlignment(Qt.AlignLeft)
        self.setTitle("设备信息")

        # 创建 TitledWidgetGroup 用于管理页面内的各设备容器
        self.titled_widget_group = SiTitledWidgetGroup(self)
        self.titled_widget_group.setSiliconWidgetFlag(Si.EnableAnimationSignals)

        # 假设有多个设备信息，下面用一个列表模拟
        devices = ["设备 A", "设备 B", "设备 C"]

        # 动态创建每个设备的嵌套容器并添加到页面中
        for device in devices:
            device_container = self.create_device_container(device)
            self.titled_widget_group.addTitle(device)
            self.titled_widget_group.addWidget(device_container)
            # 添加间隔让页面布局更美观
            self.titled_widget_group.addPlaceholder(12)

        # 将 TitledWidgetGroup 作为页面的主体附件
        self.setAttachment(self.titled_widget_group)

    def create_device_container(self, device_name):
        """
        创建一个设备信息展示的嵌套容器，
        包含：左侧（基本信息和资源监视器）、中间（操作面板）和右侧（日志面板：以时间线形式展示）。
        """
        # 创建水平容器，用于放置三个面板
        container_h = SiDenseHContainer(self)
        container_h.setSpacing(8)
        # 根据各面板内容调整高度（此处示例高度为固定值，可根据实际需要修改）
        container_h.setFixedHeight(80 + 8 + 250)

        # ---------------- 左侧面板：基本信息与资源监视器 ----------------
        container_v = SiDenseVContainer(self)
        container_v.setSpacing(8)
        container_v.setAdjustWidgetsSize(True)

        # 基本信息卡片
        container_description = SiOptionCardLinear(self)
        container_description.setTitle("设备信息", f"展示 {device_name} 的基本信息")
        container_description.load(SiGlobal.siui.iconpack.get("ic_fluent_slide_layout_regular"))
        detail_button = SiPushButton(self)
        detail_button.resize(60, 24)
        detail_button.attachment().setText("详情")
        container_description.addWidget(detail_button)

        # 资源监视器卡片
        container_resource = SiOptionCardPlane(self)
        container_resource.setTitle("资源选择")
        container_resource.setFixedHeight(250)

        # 模拟的资源监视器数据
        label_cpu = SiLabel(self)
        label_cpu.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_C"]))
        label_cpu.setText("CPU")
        progress_bar_cpu = SiProgressBar(self)
        progress_bar_cpu.setFixedHeight(8)
        progress_bar_cpu.setValue(0.12)

        label_ram = SiLabel(self)
        label_ram.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_C"]))
        label_ram.setText("内存")
        progress_bar_ram = SiProgressBar(self)
        progress_bar_ram.setFixedHeight(8)
        progress_bar_ram.setValue(0.61)

        label_gpu = SiLabel(self)
        label_gpu.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_C"]))
        label_gpu.setText("GPU")
        progress_bar_gpu = SiProgressBar(self)
        progress_bar_gpu.setFixedHeight(8)
        progress_bar_gpu.setValue(0.23)

        resource_body = container_resource.body()
        resource_body.setAdjustWidgetsSize(True)
        resource_body.addWidget(label_cpu)
        resource_body.addWidget(progress_bar_cpu)
        resource_body.addWidget(label_ram)
        resource_body.addWidget(progress_bar_ram)
        resource_body.addWidget(label_gpu)
        resource_body.addWidget(progress_bar_gpu)

        # 将基本信息卡片与资源监视器卡片添加到左侧垂直容器中
        container_v.addWidget(container_description)
        container_v.addWidget(container_resource)

        # ---------------- 中间面板：操作面板 ----------------
        container_operation = SiOptionCardPlane(self)
        container_operation.setTitle("任务面板")
        container_operation.setFixedHeight(80 + 8 + 250)
        container_operation.setFixedWidth(320)

        label_operation = SiLabel(self)
        label_operation.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_D"]))
        label_operation.setText(f"这里可以操作 {device_name} 的各项功能")
        label_operation.setAlignment(Qt.AlignCenter)
        label_operation.setFixedHeight(220)

        operation_body = container_operation.body()
        operation_body.setAdjustWidgetsSize(True)
        operation_body.addWidget(label_operation)
        # ---------------- 中间面板：操作设置 ----------------
        container_setting = SiOptionCardPlane(self)
        container_setting.setTitle("设置面板")
        container_setting.setFixedHeight(80 + 8 + 250)
        container_setting.setFixedWidth(320)

        label_setting = SiLabel(self)
        label_setting.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_D"]))
        label_setting.setText(f"这里可以操作 {device_name} 的各项功能")
        label_setting.setAlignment(Qt.AlignCenter)
        label_setting.setFixedHeight(220)

        setting_body = container_setting.body()
        setting_body.setAdjustWidgetsSize(True)
        setting_body.addWidget(label_setting)

        # ---------------- 右侧面板：日志面板（以时间线形式展示） ----------------
        # 使用 OptionCardPlaneForWidgetDemos 替代传统的 QPlainTextEdit 展示方式
        container_log = OptionCardPlaneForWidgetDemos(self)
        container_log.setTitle("日志面板")
        container_log.setFixedHeight(80 + 8 + 250)
        container_log.setFixedWidth(320)

        # 创建时间线组件
        timeline = SiTimeLine(self)
        timeline.setFixedWidth(300)  # 调整宽度以适应面板

        # 示例时间线项
        item1 = SiTimeLineItem(self)
        item1.setContent("11:45:14", f"{device_name} 启动成功")
        item1.adjustSize()

        item2 = SiTimeLineItem(self)
        item2.setContent("19:19:10", f"{device_name} 运行正常")
        item2.setIcon(SiGlobal.siui.iconpack.get(
            "ic_fluent_info_filled", color_code=self.getColor(SiColor.SIDE_MSG_THEME_SUCCESS)))
        item2.setIconHint("信息")
        item2.setThemeColor(self.getColor(SiColor.SIDE_MSG_THEME_SUCCESS))
        item2.adjustSize()

        item3 = SiTimeLineItem(self)
        item3.setContent("00:00:00", f"{device_name} 检测到异常")
        item3.setIcon(SiGlobal.siui.iconpack.get(
            "ic_fluent_warning_shield_filled", color_code=self.getColor(SiColor.PROGRESS_BAR_COMPLETING)))
        item3.setIconHint("警告")
        item3.setThemeColor(self.getColor(SiColor.PROGRESS_BAR_COMPLETING))
        item3.adjustSize()

        # 将时间线项添加到时间线组件中
        timeline.addWidget(item1)
        timeline.addWidget(item2)
        timeline.addWidget(item3)

        # 将时间线组件加入日志面板的主体中，并添加适当的占位
        container_log.body().addWidget(timeline)
        container_log.body().addPlaceholder(12)

        # ---------------- 将三个面板加入到水平容器中 ----------------
        container_h.addWidget(container_v)
        container_h.addWidget(container_operation)
        container_h.addWidget(container_setting)
        container_h.addWidget(container_log)

        return container_h

