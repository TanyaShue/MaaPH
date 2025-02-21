from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QBoxLayout, QAction

from siui.components.combobox import SiComboBox
from siui.components.menu_ import SiRoundMenu

from siui.components.menu import SiMenu
from siui.components.widgets.label import SiLabel

from siui.components import (
    SiPushButton,
    SiTitledWidgetGroup, SiLineEdit, )
from siui.components.button import SiSwitchRefactor
from siui.components.container import SiTriSectionPanelCard, SiDenseContainer
from siui.components.label import SiLabelRefactor
from siui.components.page.child_page import SiChildPage
from siui.core import SiGlobal


class TaskSettingPage(SiChildPage):
    device_added_signal = pyqtSignal(dict)

    def __init__(self, parent, resource_config=None, entry_name=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.resource_config = resource_config
        self.entry_name = entry_name
        print(f"TaskSettingPage resource_config: {self.resource_config}")
        print(f"TaskSettingPage entry_name: {entry_name}")

        self.view().setMinimumWidth(500)
        self.width_ratio = 0.382

        if entry_name:
            self.content().setTitle(f"{entry_name}")
        else:
            self.content().setTitle("任务设置")
        self.content().setPadding(64)

        # 页面内容 - 使用 SiTitledWidgetGroup 分组
        self.titled_widget_group = SiTitledWidgetGroup(self)

        with self.titled_widget_group as group:
            # 设备信息区域
            self.device_info_card = SiTriSectionPanelCard(self)
            self.device_info_card.setTitle("任务设置")

            # 动态生成设置选项
            if self.resource_config and self.entry_name:
                self.generate_settings()

            self.device_info_card.adjustSize()
            group.addWidget(self.device_info_card)

        self.content().setAttachment(self.titled_widget_group)

        # 控制面板
        self.add_device_button = SiPushButton(self)
        self.add_device_button.resize(128, 32)
        self.add_device_button.attachment().setText("添加设备")

        self.panel().addWidget(self.add_device_button, "right")

        # 加载样式表
        SiGlobal.siui.reloadStyleSheetRecursively(self)
        self.titled_widget_group.arrangeWidget()

    def generate_settings(self):
        # 找到当前entry_name对应的task
        print(self.resource_config.resource_tasks)
        for task in self.resource_config.resource_tasks:
            print(f"task: {task},当前entry_name: {self.entry_name}")
            if task.task_entry == self.entry_name:
                print(f"找到当前entry_name对应的task: {task}")


        current_task = next((task for task in self.resource_config.resource_tasks
                             if task.task_entry == self.entry_name), None)


        if not current_task:
            return

        # 获取当前task的选项列表
        option_names = current_task.option

        # 遍历选项名称，找到对应的选项配置并生成UI
        for option_name in option_names:
            option_config = next((opt for opt in self.resource_config.options
                                  if opt.name == option_name), None)

            if not option_config:
                continue

            # 创建选项容器
            option_container = SiDenseContainer(self, direction=QBoxLayout.LeftToRight)

            # 创建标签
            label = SiLabel(self)
            label.setText(option_config.name)
            label.setTextColor("#ffffff")
            option_container.addWidget(label)

            # 根据选项类型创建对应的控件
            if option_config.type == 'boole':
                control = SiSwitchRefactor(self)
                control.setChecked(option_config.default)
                option_container.addWidget(control, side=Qt.LeftEdge)

            elif option_config.type == 'input':
                control = SiLineEdit(self)
                control.setFixedWidth(100)
                # control.setText(str(option_config.default))
                option_container.addWidget(control)

            elif option_config.type == 'select':
                control = SiComboBox(self)
                control.setFixedWidth(100)
                for choice in option_config.choices:
                    control.addOption(choice.name)
                # control.setCurrentText(str(option_config.default))
                option_container.addWidget(control)
                # 重载样式
                SiGlobal.siui._reloadWidgetStyleSheet(control.menu())
                control.menu().reloadStyleSheet()

            # 将选项添加到卡片中
            self.device_info_card.body().addWidget(option_container)