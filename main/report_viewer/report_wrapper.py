from .report_segment import ReportSegment
from kivymd.uix.widget import MDWidget
from kivy.properties import NumericProperty
from kivy.properties import StringProperty


class ReportWrapper(MDWidget):
    text_in_segment: StringProperty\
        = StringProperty()
    nr: NumericProperty \
        = NumericProperty()
