from PyQt5.QtCore import Qt, QSize
from siui.components.widgets.abstracts.widget import SiWidget
from siui.components.widgets.label import SiLabel
from siui.core import SiColor
from siui.gui import SiFont


class SiLogItem(SiWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = SiLabel(self)
        self.title.setFont(SiFont.getFont(size=10)) # Smaller font size for timestamp
        self.title.setTextColor(self.getColor(SiColor.TEXT_D))
        self.title.setAlignment(Qt.AlignLeft)
        self.title.setContentsMargins(0, 4, 0, 0) # Reduced top margin
        self.title.move(0, 0) # Align to the left edge
        self.title.adjustSize()

        self.description = SiLabel(self)
        self.description.setFont(SiFont.getFont(size=12)) # Keep description font size or adjust as needed
        self.description.setTextColor(self.getColor(SiColor.TEXT_B))
        self.description.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.description.setWordWrap(True) # Enable word wrap for long logs
        self.description.move(0, self.title.height()) # Position below title
        self.description.adjustSize()

    def setContent(self, title, description):
        self.title.setText(title)
        self.title.adjustSize()
        self.description.setText(description)
        self.description.adjustSize()
        self.adjustSize() # Adjust SiLogItem size after content change

    def sizeHint(self):
        # Calculate size hint based on title and description heights with minimal spacing
        return QSize(self.width(), self.title.height() + self.description.height() + 4) # Minimal spacing

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Ensure word wrap works correctly in resizeEvent
        self.title.resize(event.size().width(), self.title.height()) # Title takes full width
        self.description.resize(event.size().width(), 0) # Reset height to recalculate based on width
        self.description.adjustSize() # Adjust description height based on width and word wrap
        self.description.move(0, self.title.height() + 4) # Position description below title with spacing

