from kivymd.uix.boxlayout import MDBoxLayout
from .report import Report
from .button_copy import ButtonCopy
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.properties import NumericProperty


Builder.load_file("raport_viewer/raportviewer.kv")
Builder.load_file("raport_viewer/report.kv")
Builder.load_file("raport_viewer/buttoncopy.kv")


class RaportViewer(MDBoxLayout):
    report_text: StringProperty = StringProperty()
    nav_bar_hight: NumericProperty = NumericProperty()

    def on_report_text(self, *args, **kwargs):
        self.ids.report_label.text = self.report_text
