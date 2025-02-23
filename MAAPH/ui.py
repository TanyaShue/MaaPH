from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDesktopWidget, QSystemTrayIcon

import siui
from MAAPH.icons import parser as icons
from MAAPH.components.page_appmarket.app_market_page import AppMarketPage
from MAAPH.components.page_device_info_page.page_device_info_page import ExampleDeviceInfoPage
from MAAPH.components.page_homepage.homepage import Homepage
from MAAPH.control.tasker_service_manager import TaskerServiceManager
from MAAPH.components.page_about import About
from siui.core import SiColor, SiGlobal
from siui.templates.application.application import SiliconApplication

# 载入图标
siui.core.globals.SiGlobal.siui.loadIcons(
    icons.IconDictionary(color=SiGlobal.siui.colors.fromToken(SiColor.SVG_NORMAL)).icons
)


class MySiliconApp(SiliconApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.task_manager = TaskerServiceManager()

        screen_geo = QDesktopWidget().screenGeometry()
        self.setMinimumSize(1024, 380)
        self.resize(1366, 916)
        self.move((screen_geo.width() - self.width()) // 2, (screen_geo.height() - self.height()) // 2)
        self.layerMain().setTitle("MAAPH")
        self.setWindowTitle("MAAPH")
        self.setWindowIcon(QIcon("img/empty_icon.png"))
        self.layerMain().addPage(Homepage(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_home_filled"),
                                 hint="首页", side="top")
        self.layerMain().addPage(ExampleDeviceInfoPage(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_list_bar_filled"),
                                 hint="设备管理", side="top")
        self.layerMain().addPage(AppMarketPage(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_apps_add_in_filled"),
                                 hint="资源市场", side="top")

        self.layerMain().addPage(About(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_info_filled"),
                                 hint="关于", side="bottom")

        self.layerMain().setPage(0)

        SiGlobal.siui.reloadAllWindowsStyleSheet()
    # def closeEvent(self, event):
    #     # 关闭窗口时最小化到托盘而不是退出
    #     event.ignore()
    #     self.hide()
    #     self.tray_icon.showMessage("MyApp", "Application is running in background.", QSystemTrayIcon.Information, 2000)
    #
    # def show_window(self):
    #     # 恢复窗口显示
    #     self.show()