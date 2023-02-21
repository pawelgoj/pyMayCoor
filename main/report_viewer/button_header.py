from kivymd.uix.button.button import MDRectangleFlatButton
from .report_wrapper import ReportWrapper
from kivy.properties import ObjectProperty
from kivy.animation import Animation


class ButtonHeader(MDRectangleFlatButton):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text_section = None

    def on_press(self):
        height_in_scroll = self.text_section.parent.height
        
        # For reset movement of scrollbar
        self.parent.parent.parent.ids.report_scrollView_2.effect_y.reset(0)
        
        tym = (self.text_section.height + self.text_section.pos[1])
        ratio = (tym - self.text_section.parent.parent.height)\
            / (height_in_scroll - self.text_section.parent.parent.height)
        self.parent.parent.parent.ids.report_scrollView_2.scroll_y = ratio
        self.parent.parent.parent.ids.report_scrollView_2\
            .update_from_scroll()
