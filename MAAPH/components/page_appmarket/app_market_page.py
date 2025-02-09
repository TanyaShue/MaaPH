from PyQt5.QtCore import Qt

from siui.components.option_card import SiOptionCardLinear, SiOptionCardPlane
from siui.components.page import SiPage
from siui.components.titled_widget_group import SiTitledWidgetGroup
from siui.components.widgets import SiDenseHContainer, SiDenseVContainer, SiLabel, SiPushButton
from siui.core import Si
from siui.core import SiGlobal


class AppMarketPage(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 设置页面属性
        self.setPadding(64)
        self.setScrollMaximumWidth(1200)
        self.setScrollAlignment(Qt.AlignLeft)
        self.setTitle("资源市场")

        # 创建整体容器（带标题分组）
        self.titled_widget_group = SiTitledWidgetGroup(self)
        self.titled_widget_group.setSiliconWidgetFlag(Si.EnableAnimationSignals)

        # 创建一个水平容器，左侧显示应用列表，右侧显示应用详情
        main_container = SiDenseHContainer(self)
        main_container.setSpacing(16)

        # ----------------------
        # 左侧：应用列表容器
        # ----------------------
        self.app_list_container = SiDenseVContainer(self)
        self.app_list_container.setSpacing(8)
        self.app_list_container.setAdjustWidgetsSize(True)
        # 模拟加载应用数据（后续可替换为真实 API 调用）
        self.loadApps()

        # ----------------------
        # 右侧：应用详情容器
        # ----------------------
        self.details_container = SiOptionCardPlane(self)
        self.details_container.setTitle("资源详情")
        # 固定详情容器的宽度（可根据实际需求调整）
        self.details_container.setFixedWidth(600)

        # 初始化详情区域，提示用户选择一个应用
        self.detail_placeholder = SiLabel(self)
        self.detail_placeholder.setText("请选择一个应用查看详情")
        self.detail_placeholder.setAlignment(Qt.AlignCenter)
        self.details_container.body().addWidget(self.detail_placeholder, side="top")

        # 将左右两个容器添加到主容器中
        main_container.addWidget(self.app_list_container)
        main_container.addWidget(self.details_container)

        # 添加一个标题和主容器到整体的分组中
        self.titled_widget_group.addTitle("资源市场")
        self.titled_widget_group.addWidget(main_container)
        self.titled_widget_group.addPlaceholder(64)  # 占位符

        # 设置页面的附件为整体容器
        self.setAttachment(self.titled_widget_group)

    def loadApps(self):
        """
        模拟从 API 获取应用数据，并构建应用卡片列表。
        你可以将下面的 apps 列表替换为实际 API 返回的数据。
        """
        apps = [
            {
                "name": "应用一",
                "description": "这是第一个应用，功能强大，体验流畅。",
                "icon": "ic_fluent_slide_layout_regular",  # 请确保图标名称在 SiGlobal.siui.iconpack 中存在
                "version": "1.0.0",
                "author": "开发者A"
            },
            {
                "name": "应用二",
                "description": "第二个应用，提供便捷服务，界面美观。",
                "icon": "ic_fluent_slide_layout_regular",
                "version": "2.3.1",
                "author": "开发者B"
            },
            {
                "name": "应用三",
                "description": "第三个应用，专为高效办公设计，体验极致。",
                "icon": "ic_fluent_slide_layout_regular",
                "version": "0.9.5",
                "author": "开发者C"
            }
        ]

        # 遍历应用数据，为每个应用构建一个线性选项卡卡片
        for app in apps:
            app_card = SiOptionCardLinear(self)
            app_card.setTitle(app["name"], app["description"])
            app_card.load(SiGlobal.siui.iconpack.get(app["icon"]))

            # 创建一个“详情”按钮，点击后展示该应用的详细信息
            detail_button = SiPushButton(self)
            detail_button.resize(80, 32)
            detail_button.attachment().setText("详情")
            # 注意：这里使用 lambda 绑定参数 app
            # detail_button.clicked.connect(lambda checked, app=app: self.showAppDetails(app))
            app_card.addWidget(detail_button)

            # 将应用卡片添加到应用列表容器中
            self.app_list_container.addWidget(app_card)

    def showAppDetails(self, app):
        """
        更新右侧详情区域，显示选中应用的详细信息
        """
        body_container = self.details_container.body()

        # 清理详情区域：先从布局中移除所有子控件
        layout = body_container.layout()
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                    widget.deleteLater()

        # 构造应用详细信息文本
        detail_text = (
            f"应用名称：{app['name']}\n\n"
            f"描述：{app['description']}\n\n"
            f"版本：{app['version']}\n\n"
            f"作者：{app['author']}\n"
        )

        detail_label = SiLabel(self)
        detail_label.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_B"]))
        detail_label.setText(detail_text)
        detail_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        # 添加详细信息到详情区域（建议使用垂直排列）
        body_container.addWidget(detail_label, side="top")

        # 调整相关组件的尺寸以适应内容变化
        self.details_container.adjustSize()
        self.titled_widget_group.adjustSize()
        self.adjustSize()
