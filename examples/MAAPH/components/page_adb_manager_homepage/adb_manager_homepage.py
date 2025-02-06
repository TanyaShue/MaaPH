from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from siui.components import SiPixLabel
from siui.components.option_card import SiOptionCardPlane, SiOptionCardLinear
from siui.components.page import SiPage
from siui.components.slider import SiSliderH
from siui.components.titled_widget_group import SiTitledWidgetGroup
from siui.components.widgets import (
    SiDenseHContainer,
    SiDenseVContainer,
    SiLabel,
    SiLineEdit,
    SiLongPressButton,
    SiPushButton,
    SiSimpleButton,
    SiSwitch,
)
from siui.core import GlobalFont, Si, SiColor, SiGlobal, SiQuickEffect, GlobalFontSize
from siui.gui import SiFont


# 用于展示 adb 设备的卡片示例
from siui.components.option_card import SiOptionCardPlane
from siui.components.widgets import SiDenseVContainer, SiLabel, SiSimpleButton
from siui.core import SiGlobal


class ADBDeviceCard(SiOptionCardPlane):
    def __init__(self, device_name="Unknown Device", status="Disconnected", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setTitle(device_name)
        self.setFixedSize(250, 150)
        # 设置一个简单的描述文本，显示连接状态
        self.body().addWidget(
            SiLabel(self, text=f"Status: {status}"),
            side="top"
        )
        # 添加一个按钮用于后续的操作（如查看详情、连接、断开）
        manage_btn = SiSimpleButton(self)
        manage_btn.attachment().setText("Manage")
        self.footer().addWidget(manage_btn, side="right")


# 用于展示项目的卡片示例
class ProjectCard(SiOptionCardPlane):
    def __init__(self, project_name="New Project", description="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setTitle(project_name)
        self.setFixedSize(250, 180)
        # 设置描述信息（例如项目介绍、任务数等）
        desc_label = SiLabel(self)
        desc_label.setText(description or "No description available.")
        desc_label.setStyleSheet("color: {};".format(SiGlobal.siui.colors["TEXT_B"]))
        desc_label.setWordWrap(True)
        self.body().addWidget(desc_label, side="top")

        # 添加一个按钮用于进入项目详情或执行任务
        open_btn = SiSimpleButton(self)
        open_btn.attachment().setText("Open")
        self.footer().addWidget(open_btn, side="right")

# 主页面：自动操作 adb 设备、项目和插件的入口
class ADBManagerHomepage(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 整个页面使用一个带标题的容器，实现滚动效果
        self.scroll_container = SiTitledWidgetGroup(self)

        # ------------------ 顶部区域 ------------------
        self.header_area = SiLabel(self)
        self.header_area.setFixedHeight(300)
        # 设置背景图片或颜色
        self.header_area.setStyleSheet("background-color: #2C3E50; border-radius: 6px;")

        # 应用背景图（如果有图片资源可用）
        self.header_background = SiPixLabel(self.header_area)
        self.header_background.setFixedSize(1366, 300)
        self.header_background.load("./img/adb_manager_background.png")  # 请确保图片存在

        # 大标题
        self.title = SiLabel(self.header_area)
        self.title.setGeometry(64, 20, 500, 64)
        self.title.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.title.setText("ADB Automation Manager")
        self.title.setStyleSheet("color: {};".format(SiGlobal.siui.colors["TEXT_A"]))
        self.title.setFont(SiFont.tokenized(GlobalFont.XL_MEDIUM))

        # 副标题
        self.subtitle = SiLabel(self.header_area)
        self.subtitle.setGeometry(64, 84, 600, 32)
        self.subtitle.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.subtitle.setText("Manage multiple adb devices and projects effortlessly")
        self.subtitle.setStyleSheet("color: {};".format(SiColor.trans(SiGlobal.siui.colors["TEXT_A"], 0.9)))
        self.subtitle.setFont(SiFont.tokenized(GlobalFont.S_MEDIUM))

        # ------------------ 设备展示区域 ------------------
        # 用于展示已连接的 adb 设备（示例中添加两个设备卡片）
        self.devices_container = SiDenseHContainer(self)
        self.devices_container.setFixedHeight(180)
        self.devices_container.setAlignment(Qt.AlignCenter)
        self.devices_container.setSpacing(16)

        # 示例设备卡片（后续可动态生成）
        device_card_1 = ADBDeviceCard(device_name="Device 1", status="Connected", parent=self)
        device_card_2 = ADBDeviceCard(device_name="Device 2", status="Connected", parent=self)
        self.devices_container.addWidget(device_card_1)
        self.devices_container.addWidget(device_card_2)

        # # ------------------ 项目展示区域 ------------------
        # # 用于展示各个项目（可从插件市场中下载加载）
        # self.projects_container = SiDenseHContainer(self)
        # self.projects_container.setFixedHeight(200)
        # self.projects_container.setAlignment(Qt.AlignCenter)
        # self.projects_container.setSpacing(16)
        #
        # # 示例项目卡片
        # project_card_1 = ProjectCard(
        #     project_name="Project Alpha",
        #     description="A sample project for automation tasks.",
        #     parent=self
        # )
        # project_card_2 = ProjectCard(
        #     project_name="Project Beta",
        #     description="Another project with dynamic scripts.",
        #     parent=self
        # )
        # self.projects_container.addWidget(project_card_1)
        # self.projects_container.addWidget(project_card_2)

        # ------------------ 底部按钮区域 ------------------
        # 一个简单的按钮区域，例如进入插件市场
        self.bottom_area = SiDenseVContainer(self)
        self.bottom_area.setAlignment(Qt.AlignCenter)
        self.bottom_area.setSpacing(12)

        plugin_market_button = SiPushButton(self)
        plugin_market_button.resize(210, 32)
        plugin_market_button.attachment().setText("Go to Plugin Market")
        self.bottom_area.addWidget(plugin_market_button)

        # ------------------ 将各区域添加到滚动容器中 ------------------
        self.scroll_container.addWidget(self.header_area)
        self.scroll_container.addWidget(self.devices_container)
        # self.scroll_container.addWidget(self.projects_container)
        self.scroll_container.addWidget(self.bottom_area)

        # 设置滚动容器为页面主要内容
        self.setAttachment(self.scroll_container)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        w = event.size().width()
        self.header_area.setFixedWidth(w)
        self.header_background.setFixedWidth(w)
        self.devices_container.setFixedWidth(w)
        self.bottom_area.setFixedWidth(w)
        self.scroll_container.adjustSize()
