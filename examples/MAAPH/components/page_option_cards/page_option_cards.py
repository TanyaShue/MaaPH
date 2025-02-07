from PyQt5.QtCore import Qt

from siui.components.option_card import SiOptionCardLinear, SiOptionCardPlane
from siui.components.page import SiPage
from siui.components.progress_bar import SiProgressBar
from siui.components.titled_widget_group import SiTitledWidgetGroup
from siui.components.widgets import SiDenseHContainer, SiDenseVContainer, SiLabel
from siui.core import Si
from siui.core import SiGlobal


class ExampleOptionCards(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # From here, we can start to build our first page in Silicon Application
        # You can set the name of this page, and add widgets to varify the function to beautify it.

        # Set the title of the page
        # self.setTitle("应用模版")

        # Set X Offset for better outfit.
        self.setPadding(64)
        self.setScrollMaximumWidth(1000)
        self.setScrollAlignment(Qt.AlignLeft)
        self.setTitle("选项卡")

        # Create a SiTitledWidgetGroup object
        self.titled_widget_group = SiTitledWidgetGroup(self)
        self.titled_widget_group.setSiliconWidgetFlag(Si.EnableAnimationSignals)

        # 容器

        container_h = SiDenseHContainer(self)
        container_h.setSpacing(8)
        container_h.setFixedHeight(80+8+250+8+250)

        container_v = SiDenseVContainer(self)
        container_v.setSpacing(8)
        container_v.setAdjustWidgetsSize(True)
        self.titled_widget_group.resized.connect(lambda pos: container_v.setFixedWidth(pos[0] - 320 - 8))

        container_description = SiOptionCardLinear(self)
        container_description.setTitle("嵌套容器", "让你的界面布局更加美观和直观")
        container_description.load(SiGlobal.siui.iconpack.get("ic_fluent_slide_layout_regular"))

        container_plane_left_bottom = SiOptionCardPlane(self)
        container_plane_left_bottom.setTitle("资源监视器")
        container_plane_left_bottom.setFixedHeight(250)

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

        container_plane_left_bottom.body().setAdjustWidgetsSize(True)
        container_plane_left_bottom.body().addWidget(label_cpu)
        container_plane_left_bottom.body().addWidget(progress_bar_cpu)
        container_plane_left_bottom.body().addWidget(label_ram)
        container_plane_left_bottom.body().addWidget(progress_bar_ram)
        container_plane_left_bottom.body().addWidget(label_gpu)
        container_plane_left_bottom.body().addWidget(progress_bar_gpu)

        container_v.addWidget(container_description)
        container_v.addWidget(container_plane_left_bottom)

        container_plane_right = SiOptionCardPlane(self)
        container_plane_right.setTitle("操作面板")
        container_plane_right.setFixedHeight(80+8+250)
        container_plane_right.setFixedWidth(320)

        label_nothing = SiLabel()
        label_nothing.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_D"]))
        label_nothing.setText("这里好像什么也没有")
        label_nothing.setAlignment(Qt.AlignCenter)
        label_nothing.setFixedHeight(220)

        container_plane_right.body().setAdjustWidgetsSize(True)
        container_plane_right.body().addWidget(label_nothing)

        container_h.addWidget(container_v)
        container_h.addWidget(container_plane_right)

        # <- ADD
        self.titled_widget_group.addTitle("设备信息")
        self.titled_widget_group.addWidget(container_h)

        # add placeholder for better outfit
        self.titled_widget_group.addPlaceholder(64)

        # Set SiTitledWidgetGroup object as the attachment of the page's scroll area
        self.setAttachment(self.titled_widget_group)


