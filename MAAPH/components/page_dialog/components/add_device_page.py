from PyQt5.QtCore import pyqtSignal

from siui.components import (
    SiOptionCardPlane,
    SiPushButton,
    SiTitledWidgetGroup,
)
from siui.components.combobox.combobox import SiComboBox
from siui.components.editbox import SiLineEdit
from siui.components.page.child_page import SiChildPage
from siui.components.widgets.button import SiSimpleButton
from siui.core import SiGlobal


class AddDevicePage(SiChildPage):
    # 定义信号，信号携带一个字典参数，用于传递设备配置
    device_added_signal = pyqtSignal(dict)
    def __init__(self, *arg, **kwargs): # 接受 homepage_instance 参数
        super().__init__(*arg, **kwargs)

        self.view().setMinimumWidth(800)
        self.content().setTitle("添加新设备")
        self.content().setPadding(64)


        # 页面内容 - 使用 SiTitledWidgetGroup 分组
        self.titled_widget_group = SiTitledWidgetGroup(self)

        # self.titled_widget_group.header().addWidget(header_button)

        with self.titled_widget_group as group:
            # 设备信息区域
            self.device_info_card = SiOptionCardPlane(self)
            self.device_info_card.setTitle("设备信息") # 设备信息卡片标题
            header_button = SiSimpleButton(self)
            header_button.setFixedHeight(32)
            header_button.attachment().setText("搜索设备")
            header_button.attachment().load(SiGlobal.siui.iconpack.get("ic_fluent_window_header_horizontal_regular"))
            header_button.adjustSize()
            select_device_combobox = SiComboBox(self)
            select_device_combobox.resize(256, 32)
            select_device_combobox.addOption("Chicken you are so beautiful")
            select_device_combobox.addOption("你干嘛嗨嗨呦~")
            select_device_combobox.addOption("迎面走来的你让我如此蠢蠢欲动")
            select_device_combobox.addOption("唱跳Rap篮球")
            select_device_combobox.addOption("鸡你实在是太美")
            select_device_combobox.addOption("我们一起学鸡叫")
            select_device_combobox.menu().setShowIcon(False)
            select_device_combobox.menu().setIndex(0)
            self.device_info_card.header().addWidget(select_device_combobox,side="right")
            self.device_info_card.header().addWidget(header_button,side="right")
            # 重载样式,解决下拉菜单样式丢失的bug
            SiGlobal.siui._reloadWidgetStyleSheet(select_device_combobox.menu())
            select_device_combobox.menu().reloadStyleSheet()


            # 设备名称输入框
            self.line_edit_device_name = SiLineEdit(self)
            self.line_edit_device_name.setTitle("设备名称") # 设备名称标签
            self.line_edit_device_name.setFixedHeight(32) # 设置高度
            self.line_edit_device_name.resize(560, 32)

            # ADB 路径
            self.line_edit_adb_path = SiLineEdit(self)
            self.line_edit_adb_path.setTitle("ADB 路径") # ADB 路径标签
            self.line_edit_adb_path.setFixedHeight(32)
            self.line_edit_adb_path.resize(560, 32)
            # self.line_edit_adb_path.setReadOnly(True) # 设置为只读，因为通常自动获取

            # ADB 地址
            self.line_edit_adb_address = SiLineEdit(self)
            self.line_edit_adb_address.setTitle("ADB 地址") # ADB 地址标签
            self.line_edit_adb_address.setFixedHeight(32)
            self.line_edit_adb_address.resize(560, 32)
            # self.line_edit_adb_address.setReadOnly(True) # 设置为只读

            # Screencap Methods
            self.line_edit_screencap_methods = SiLineEdit(self)
            self.line_edit_screencap_methods.setTitle("截图方法") # 截图方法标签
            self.line_edit_screencap_methods.setFixedHeight(32)
            self.line_edit_screencap_methods.resize(560, 32)
            # self.line_edit_screencap_methods.setReadOnly(True) # 设置为只读

            # Input Methods
            self.line_edit_input_methods = SiLineEdit(self)
            self.line_edit_input_methods.setTitle("输入法") # 输入法标签
            self.line_edit_input_methods.setFixedHeight(32)
            self.line_edit_input_methods.resize(560, 32)
            # self.line_edit_input_methods.setReadOnly(True) # 设置为只读

            # 将设备名称和 ADB 配置信息输入框添加到设备信息卡片中
            self.device_info_card.body().setAdjustWidgetsSize(True) # 允许调整部件大小
            self.device_info_card.body().addWidget(self.line_edit_device_name)
            self.device_info_card.body().addWidget(self.line_edit_adb_path)
            self.device_info_card.body().addWidget(self.line_edit_adb_address)
            self.device_info_card.body().addWidget(self.line_edit_screencap_methods)
            self.device_info_card.body().addWidget(self.line_edit_input_methods)
            self.device_info_card.body().addPlaceholder(12) # 添加一些空白占位
            self.device_info_card.adjustSize() # 调整卡片大小

            group.addWidget(self.device_info_card) # 将设备信息卡片添加到分组

        with self.titled_widget_group as group:
            # 高级设置区域
            self.advanced_settings_card = SiOptionCardPlane(self)
            self.advanced_settings_card.setTitle("高级设置") # 高级设置卡片标题

            # 定时启动
            self.line_edit_scheduled_startup = SiLineEdit(self)
            self.line_edit_scheduled_startup.setTitle("定时启动") # 定时启动标签
            self.line_edit_scheduled_startup.setFixedHeight(32)
            self.line_edit_scheduled_startup.resize(560, 32)

            # 启动前命令
            self.line_edit_pre_startup_command = SiLineEdit(self)
            self.line_edit_pre_startup_command.setTitle("启动前命令") # 启动前命令标签
            self.line_edit_pre_startup_command.setFixedHeight(32)
            self.line_edit_pre_startup_command.resize(560, 32)


            # 启动后命令
            self.line_edit_post_startup_command = SiLineEdit(self)
            self.line_edit_post_startup_command.resize(560, 32)
            self.line_edit_post_startup_command.setFixedHeight(32)
            self.line_edit_post_startup_command.setTitle("启动后命令") # 启动后命令标签

            # 将高级设置输入框添加到高级设置卡片中
            self.advanced_settings_card.body().setAdjustWidgetsSize(True)
            self.advanced_settings_card.body().addWidget(self.line_edit_scheduled_startup)
            self.advanced_settings_card.body().addWidget(self.line_edit_pre_startup_command)
            self.advanced_settings_card.body().addWidget(self.line_edit_post_startup_command)
            self.advanced_settings_card.body().addPlaceholder(12)
            self.advanced_settings_card.adjustSize()

            group.addWidget(self.advanced_settings_card) # 将高级设置卡片添加到分组

        self.content().setAttachment(self.titled_widget_group) # 将分组设置为子页面的主要内容

        # 控制面板
        self.add_device_button = SiPushButton(self)
        self.add_device_button.resize(128, 32)
        self.add_device_button.attachment().setText("添加设备")
        self.add_device_button.clicked.connect(self.on_add_device_clicked)  # 修改点击事件连接到新的方法

        self.panel().addWidget(self.add_device_button, "right")

        # 加载样式表
        SiGlobal.siui.reloadStyleSheetRecursively(self)

    def on_add_device_clicked(self):
        device_name = self.line_edit_device_name.text()
        print(device_name)
        if not device_name:
            # SiGlobal.siui.messagebox.warning(self, "设备名称不能为空", "请填写设备名称")
            device_name = "Unknown Device"
            # return

        # 获取设备配置数据 (从输入框中获取，或者您有其他获取配置的方式)
        device_config = {
            "device_name": device_name,
            "adb_path": self.line_edit_adb_path.text(),
            "adb_address": self.line_edit_adb_address.text(),
            "screencap_methods": self.line_edit_screencap_methods.text(),
            "input_methods": self.line_edit_input_methods.text(),
            "scheduled_startup": self.line_edit_scheduled_startup.text(),
            "pre_startup_command": self.line_edit_pre_startup_command.text(),
            "post_startup_command": self.line_edit_post_startup_command.text(),
            # ... 其他配置信息 ...
        }
        # 发射信号，传递设备配置数据
        self.device_added_signal.emit(device_config)
        self.closeParentLayer()

    # def set_adb_config(self, adb_config):
    #     """
    #     用于设置 ADB 配置信息，并更新到界面上。
    #     """
    #     if adb_config:
    #         self.line_edit_adb_path.setText(adb_config.get("adb_path", ""))
    #         self.line_edit_adb_address.setText(adb_config.get("adb_address", ""))
    #         # 转换数值型 methods 为字符串显示
    #         screencap_methods_str = str(adb_config.get("screencap_methods", ""))
    #         input_methods_str = str(adb_config.get("input_methods", ""))
    #         self.line_edit_screencap_methods.setText(screencap_methods_str)
    #         self.line_edit_input_methods.setText(input_methods_str)

