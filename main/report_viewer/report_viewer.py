from kivymd.uix.boxlayout import MDBoxLayout
from .report_wrapper import ReportWrapper
from .button_header import ButtonHeader
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import Clock


Builder.load_file("report_viewer/reportviewer.kv")
Builder.load_file("report_viewer/reportsegment.kv")
Builder.load_file("report_viewer/reportwrapper.kv")
Builder.load_file("report_viewer/buttoncopy.kv")
Builder.load_file("report_viewer/buttonheader.kv")


class ReportViewer(MDBoxLayout):
    report_text: StringProperty = StringProperty()
    nav_bar_hight: NumericProperty = NumericProperty()
    report_wrappers_and_headers: list[tuple[ButtonHeader, ReportWrapper]]\
        = []

    def on_report_text(self, *args, **kwargs):
        self.ids.report_label1.text = self.report_text

    def show_report(self, output: str):
        splited = output.split('\n# ')
        self.ids.wraper1.text_in_segment = ''
        self.report_wrappers = []
        i = 0
        self.ids.report_scrollView_2.width
        for item in splited:
            if item != '':
                self.report_wrappers_and_headers.append((ButtonHeader(),
                                                         ReportWrapper()))

                self.report_wrappers_and_headers[i][1].nr = i
                self.report_wrappers_and_headers[i][1]\
                    .text_in_segment = item

                self.report_wrappers_and_headers[i][0]\
                    .text_section = self.report_wrappers_and_headers[i][1]

                pos = item.find('\n')
                self.report_wrappers_and_headers[i][0].text = item[:pos]
                self.report_wrappers_and_headers[i][1].width\
                    = self.ids.report_scrollView_2.width

                self.ids.report_scrollView_2.children[0]\
                    .add_widget(self.report_wrappers_and_headers[i][1])

                self.ids.report_scrollView_1.children[0]\
                    .add_widget(self.report_wrappers_and_headers[i][0])

                i += 1

        self.get_root_window(
        ).children[0].ids.main_tabs_of_app.switch_tab("Report")

        Clock.schedule_once(self.update_report, 0)

    def update_report(self, dt):
        self.ids.report_scrollView_2.scroll_y = 1

    def remove_report(self):
        for item in self.report_wrappers_and_headers:
            self.ids.report_scrollView_2.children[0]\
                .remove_widget(item[1])
            self.ids.report_scrollView_1.children[0]\
                .remove_widget(item[0])
        self.report_wrappers_and_headers = []
