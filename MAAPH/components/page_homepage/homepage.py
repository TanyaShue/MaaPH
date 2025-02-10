from PyQt5.QtCore import Qt
from siui.components.container import SiDenseContainer

from MAAPH.components.page_dialog.components.add_device_page import AddDevicePage
from siui.components import SiPixLabel
# 用于展示 adb 设备的卡片示例
from siui.components.option_card import SiOptionCardPlane
from siui.components.page import SiPage
from siui.components.titled_widget_group import SiTitledWidgetGroup
from siui.components.widgets import (
    SiDenseHContainer,
    SiPushButton,
)
from siui.components.widgets import SiDenseVContainer, SiLabel, SiSimpleButton
from siui.core import GlobalFont, SiColor
from siui.core import SiGlobal
from siui.gui import SiFont


class ADBDeviceCard(SiOptionCardPlane):
    def __init__(self, device_name="Unknown Device",config="{}", status="Disconnected", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setTitle(device_name)
        self.setFixedSize(250, 150)
        self.config=config
        # 设置一个简单的描述文本，显示连接状态
        self.body().addWidget(
            SiLabel(self, text=f"Status: {status}"),
            side="top"
        )
        # 添加一个按钮用于后续的操作（如查看详情、连接、断开）
        manage_btn = SiSimpleButton(self)
        manage_btn.attachment().setText("Manage")
        manage_btn.clicked.connect(
            lambda: SiGlobal.siui.windows["MAIN_WINDOW"].layerChildPage().setChildPage(AddDevicePage(self))
        )
        self.footer().addWidget(manage_btn, side="right")

# 主页面：自动操作 adb 设备、项目和插件的入口
class Homepage(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 整个页面使用一个带标题的容器，实现滚动效果
        self.scroll_container = SiTitledWidgetGroup(self)

        # ------------------ 顶部区域 ------------------
        self.header_area = SiLabel(self)
        self.header_area.setFixedHeight(300)
        # 设置背景图片或颜色
        # self.header_area.setStyleSheet("background-color: #2C3E50; border-radius: 6px;")

        self.header_background = SiPixLabel(self.header_area)
        self.header_background.setFixedSize(1366, 300)
        self.header_background.load("./img/bg_2.jpg")  # 请确保图片存在
        # self.header_background.setAlignment(Qt.AlignTop)

        # 大标题
        self.title = SiLabel(self.header_area)
        self.title.setGeometry(64, 20, 500, 64)
        self.title.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.title.setText("MAA Project Helper")
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
        self.devices_container = SiDenseContainer(self)
        self.devices_container.setFixedHeight(180)

        # 示例设备卡片（后续可动态生成）
        device_card_1 = ADBDeviceCard(device_name="Device 1",config="{}", status="Connected", parent=self)
        self.devices_container.addWidget(device_card_1)
        # device_card_2 = ADBDeviceCard(device_name="Device 2",config="{}", status="Connected", parent=self)
        # self.devices_container.addWidget(device_card_2)

        # ------------------ 底部按钮区域 ------------------
        self.bottom_area = SiDenseVContainer(self)
        self.bottom_area.setAlignment(Qt.AlignCenter)
        self.bottom_area.setSpacing(12)

        add_device_button = SiPushButton(self)
        add_device_button.resize(210, 32)
        add_device_button.attachment().setText("Add Device")
        add_device_button.clicked.connect(self.show_add_device_page)
        self.bottom_area.addWidget(add_device_button)


        # ------------------ 将各区域添加到滚动容器中 ------------------
        self.scroll_container.addWidget(self.header_area)
        self.scroll_container.addWidget(self.devices_container)
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

    def show_add_device_page(self):
        add_device_page = AddDevicePage() #  不再需要传递 Homepage 实例
        # 连接 AddDevicePage 的 device_added_signal 信号到 Homepage 的槽函数 self.handle_device_added
        add_device_page.device_added_signal.connect(self.handle_device_added)
        SiGlobal.siui.windows["MAIN_WINDOW"].layerChildPage().setChildPage(add_device_page)

    def handle_device_added(self, device_config):  # 新的槽函数，用于接收设备配置数据
        # 使用 device_config 创建 ADBDeviceCard 实例
        device_card = ADBDeviceCard(
            device_name=device_config.get("device_name", "Unknown Device"),
            config=device_config,  # 传递整个配置数据
            status="Disconnected",  # 初始状态设置为 "Disconnected"
            parent=self
        )
        # SiGlobal.siui._reloadWidgetStyleSheet(device_card)
        device_card.reloadStyleSheet()
        device_card.show()
        device_card.setVisible(True)
        device_card.adjustSize()

        self.devices_container.addWidget(device_card)


        # 修复样式无法显示,以及位置不正确的bug
        SiGlobal.siui.reloadAllWindowsStyleSheet()