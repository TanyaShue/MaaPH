import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
from siui.components.container import SiDenseContainer

from siui.components.widgets.button import SiSimpleButton

from MAAPH.components.option_card import OptionCardPlaneForWidgetDemos
from siui.components.widgets.label import SiDraggableLabel

from siui.components.widgets.container import SiFlowContainer, SiMasonryContainer

from MAAPH.components.custom_components.log_item import SiLogItem
from siui.components import SiPushButton
from siui.components.button import SiRadioButtonRefactor
from siui.components.option_card import SiOptionCardLinear, SiOptionCardPlane
from siui.components.page import SiPage
from siui.components.titled_widget_group import SiTitledWidgetGroup
from siui.components.widgets import (
    SiDenseHContainer,
    SiDenseVContainer,
    SiLabel,
    SiScrollArea,  # 导入 SiScrollArea
)
# 假设 SiColor 已经定义，你也可以自行替换为具体颜色代码
from siui.core import SiGlobal, Si, SiColor


class ExampleDeviceInfoPage(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 设置页面整体属性 (保持不变)
        self.setPadding(64)
        self.setScrollMaximumWidth(1600)
        self.setScrollAlignment(Qt.AlignLeft)
        self.setTitle("设备信息")

        # 创建 TitledWidgetGroup 用于管理页面内的各设备容器 (保持不变)
        self.titled_widget_group = SiTitledWidgetGroup(self)
        self.titled_widget_group.setSiliconWidgetFlag(Si.EnableAnimationSignals)

        # 假设有多个设备信息 (保持不变)
        devices = ["设备 A", "设备 B", "设备 C"]

        # 动态创建每个设备的嵌套容器并添加到页面中 (保持不变)
        for device in devices:
            device_container = self.create_device_container(device)
            self.titled_widget_group.addTitle(device)
            self.titled_widget_group.addWidget(device_container)
            # 添加间隔让页面布局更美观 (保持不变)
            self.titled_widget_group.addPlaceholder(12)

        # 将 TitledWidgetGroup 作为页面的主体附件 (保持不变)
        self.setAttachment(self.titled_widget_group)

    def create_device_container(self, device_name):
        """
        创建一个设备信息展示的嵌套容器，
        包含：左侧（基本信息和资源监视器）、中间（操作面板）和右侧（日志面板：以时间线形式展示）。
        """
        # 创建水平容器，用于放置三个面板 (保持不变)
        container_h = SiDenseHContainer(self)
        container_h.setSpacing(8)
        container_h.setFixedHeight(80 + 8 + 300)

        # ---------------- 左侧面板：基本信息与资源监视器 (基本信息卡片保持不变) ----------------
        container_v = SiDenseVContainer(self)
        container_v.setSpacing(8)
        container_v.setAdjustWidgetsSize(True)

        # 基本信息卡片 (保持不变)
        container_description = SiOptionCardLinear(self)
        container_description.setFixedWidth(500)
        container_description.setTitle("设备信息", f"展示 {device_name} 的基本信息")
        container_description.load(SiGlobal.siui.iconpack.get("ic_fluent_slide_layout_regular"))
        detail_button = SiPushButton(self)
        detail_button.resize(60, 24)
        detail_button.attachment().setText("详情")
        container_description.addWidget(detail_button)

        # 资源选择卡片 (修改为 SiScrollArea 滚动容器 - 保持不变)
        container_resource = SiOptionCardPlane(self)
        container_resource.setTitle("资源选择")
        container_resource.setFixedHeight(300)

        # -------------------- 资源选择卡片内容修改 - 使用 SiScrollArea (保持不变) --------------------
        resource_scroll_area = SiScrollArea(self)  # 创建 SiScrollArea 滚动区域
        resource_scroll_area.setFixedWidth(440)
        resource_scroll_area.setFixedHeight(200)
        resource_scroll_area.adjustSize()
        resource_scroll_content = SiDenseVContainer(self)  # 使用 SiDenseVContainer 作为 SiScrollArea 的内容
        resource_scroll_content.setSpacing(6)  # 设置垂直间距，让资源列表更清晰

        # 假设的资源列表 (保持不变)
        resources = ["阴阳师", "明日方舟", "M9A", "战双", "阴阳师", "明日方舟", "M9A", "战双", "阴阳师", "明日方舟",
                     "M9A", "战双"]
        radio_buttons = []

        for resource_name in resources:
            # 创建一行的水平布局容器 (保持不变)
            resource_row = SiDenseHContainer(self)
            resource_row.setFixedWidth(420)

            radio_button = SiRadioButtonRefactor(self)
            radio_button.setText(resource_name)
            radio_button.adjustSize()
            resource_row.addWidget(radio_button, side="left")

            setting_button = SiPushButton(self)
            setting_button.resize(48, 24)
            setting_button.attachment().setText("设置")
            setting_button.adjustSize()
            execute_button = SiPushButton(self)
            execute_button.resize(48, 24)
            execute_button.attachment().setText("执行")
            execute_button.adjustSize()
            resource_row.addWidget(setting_button, side="right")
            resource_row.addWidget(execute_button, side="right")

            resource_scroll_content.addWidget(resource_row)  # 将每一行添加到 SiDenseVContainer 中

        resource_scroll_area.setAttachment(resource_scroll_content)  # 设置 SiDenseVContainer 为 SiScrollArea 的滚动内容
        container_resource.body().addWidget(resource_scroll_area)  # 将 SiScrollArea 添加到卡片的内容区域

        # 将基本信息卡片与资源选择卡片添加到左侧垂直容器中 (保持不变)
        container_v.addWidget(container_description)
        container_v.addWidget(container_resource)

        # ---------------- 中间面板：操作面板 - 使用 SiScrollArea 滚动容器 ----------------
        # container_operation = SiOptionCardPlane(self)
        # container_operation.setTitle("任务面板")
        # container_operation.setFixedHeight(80 + 8 + 300)
        # container_operation.setFixedWidth(320)
        #
        # operation_scroll_area = SiScrollArea(self)  # 创建 操作面板 的滚动区域
        # operation_scroll_area.setFixedWidth(310)
        # operation_scroll_area.setFixedHeight(300)
        # operation_scroll_area.adjustSize()
        #
        # operation_scroll_content = SiMasonryContainer(self)  # 使用 SiMasonryContainer 作为滚动内容
        # # operation_scroll_content.setSpacing(6) # 可以根据需要调整 SiMasonryContainer 的 Spacing
        # operation_scroll_content.setAutoAdjustColumnAmount(True)
        # operation_scroll_content.setColumns(2)
        # operation_scroll_content.setFixedWidth(300)
        # operation_scroll_content.setFixedHeight(300)
        #
        # for _ in range(16):
        #     label = SiDraggableLabel(self)
        #
        #     # ---  创建 SiDenseHContainer 容器替代原有的 SiSimpleButton ---
        #     container_h = SiDenseContainer(label)  # 创建水平容器，以 label 作为父对象
        #
        #     # 左侧按钮
        #     button_left = SiSimpleButton(container_h)  # 创建左侧按钮，以水平容器 container_h 作为父对象
        #     button_left.colorGroup().assign(SiColor.BUTTON_OFF, button_left.getColor(SiColor.INTERFACE_BG_D))
        #     button_left.setFixedSize(40, 40)  # 设置左侧按钮的固定大小，您可以根据需要调整尺寸
        #     # button_left.setAttribute(Qt.WA_TransparentForMouseEvents) #  鼠标事件应该由按钮处理，不再需要透明
        #
        #     # 中间标签
        #     text_label = QLabel("任务名称", container_h)  # 创建 QLabel 作为中间的文本标签，以水平容器 container_h 作为父对象
        #     # 您可以根据需要设置 text_label 的样式，例如字体，对齐方式等等
        #     # 例如: text_label.setAlignment(Qt.AlignCenter)
        #
        #     # 右侧按钮1
        #     button_right1 = SiSimpleButton(container_h)  # 创建右侧第一个按钮
        #     button_right1.colorGroup().assign(SiColor.BUTTON_OFF, button_right1.getColor(SiColor.INTERFACE_BG_D))
        #     button_right1.setFixedSize(30, 30)  # 设置右侧按钮的固定大小，您可以根据需要调整尺寸
        #     # button_right1.setAttribute(Qt.WA_TransparentForMouseEvents) # 鼠标事件应该由按钮处理
        #
        #     # 右侧按钮2
        #     button_right2 = SiSimpleButton(container_h)  # 创建右侧第二个按钮
        #     button_right2.colorGroup().assign(SiColor.BUTTON_OFF, button_right2.getColor(SiColor.INTERFACE_BG_D))
        #     button_right2.setFixedSize(30, 30)  # 设置右侧按钮的固定大小，您可以根据需要调整尺寸
        #     # button_right2.setAttribute(Qt.WA_TransparentForMouseEvents) # 鼠标事件应该由按钮处理
        #
        #     # 将创建的控件按照水平顺序添加到 SiDenseHContainer 容器中
        #     container_h.addWidget(button_left)  # 添加左侧按钮
        #     container_h.addWidget(text_label)  # 添加中间标签
        #     container_h.addWidget(button_right1)  # 使用 addWidgets 一次性添加右侧两个按钮
        #     container_h.addWidget(button_right2)
        #
        #
        #
        #     container_h.resize(300, 40)  # 设置水平容器的初始大小，使其宽度和高度与之前的 button 保持一致, 可以根据内容调整
        #     # container_h.adjustSize() # 或者使用 adjustSize() 让容器根据内容自动调整大小
        #
        #     label.setFixedStyleSheet("border-radius: 4px")
        #     label.setColor(self.getColor(SiColor.INTERFACE_BG_D))
        #     label.resize(container_h.size())  # label 的大小需要调整为与 container_h 的大小一致
        #     # label.adjustSize() #  或者使用 adjustSize() 让 label 根据内容自动调整大小
        #
        #     operation_scroll_content.addWidget(label, ani=False)
        #     operation_scroll_content.regDraggableWidget(label)
        #
        # operation_scroll_area.setAttachment(operation_scroll_content)  # 设置滚动内容
        # container_operation.body().addWidget(operation_scroll_area)  # 将滚动区域添加到操作面板卡片的内容

        # ---------------- 右侧面板：日志面板 - 使用 SiScrollArea 滚动容器 - 优化后 ----------------
        container_log = SiOptionCardPlane(self)
        container_log.setTitle("日志面板")
        container_log.setFixedHeight(388)
        container_log.setFixedWidth(320)

        log_scroll_area = SiScrollArea(self)  # 创建 日志面板 的滚动区域
        log_scroll_area.setFixedWidth(200)  # 设置 SiScrollArea 的宽度, 保留固定宽度
        log_scroll_area.setFixedHeight(300)  # 设置 SiScrollArea 的高度,  保留固定高度
        log_scroll_area.adjustSize()  # 移除 adjustSize()

        log_scroll_content = SiDenseVContainer(self)  # 使用 SiDenseVContainer 作为滚动内容
        log_scroll_content.adjustSize()
        log_scroll_content.setSpacing(1)  # Reduced spacing for log items

        # 示例日志项 - 使用 SiLogItem (保持不变)
        item1 = SiLogItem(self)
        item1.setContent("11:45:14", f"{device_name} 启动成功")
        item1.setFixedWidth(log_scroll_area.width()-8)
        item1.adjustSize()

        item2 = SiLogItem(self)
        item2.setContent("19:19:10", f"{device_name} 运行正常")
        item2.setContent("19:19:10",
                         f"{device_name} 运行正常, 这是一个比较长的日志信息，用于测试SiLogItem组件的自动换行和显示效果。看看多行日志是否能够正确显示和滚动。")  # Example with longer description
        item2.setFixedWidth(log_scroll_area.width()-8)
        item2.adjustSize()

        item3 = SiLogItem(self)
        item3.setContent("00:00:00", f"{device_name} 检测到异常")
        item3.setFixedWidth(log_scroll_area.width()-8)
        item3.adjustSize()

        # 将日志项添加到滚动内容的布局中 (保持不变)
        log_scroll_content.addWidget(item1)
        log_scroll_content.addWidget(item2)
        log_scroll_content.addWidget(item3)

        log_scroll_area.setAttachment(log_scroll_content)
        container_log.body().addWidget(log_scroll_area)

        # ---------------- 将三个面板加入到水平容器中 (保持不变) ----------------
        container_h.addWidget(container_v)
        # container_h.addWidget(container_operation)
        container_h.addWidget(container_log)

        return container_h