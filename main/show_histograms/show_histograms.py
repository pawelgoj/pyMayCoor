from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
import matplotlib.pyplot as plt
import seaborn as sns
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
# from kivy.graphics.vertex_instructions import Rectangle
# from kivy.graphics import Color
from kivy.metrics import dp

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.widget import MDWidget
from kivy.properties import Clock

Builder.load_file("show_histograms/showhistograms.kv")


class ShowHistograms(MDBoxLayout):

    figures: list = []

    def make_hists(self, pair: str, mbo: list[float], bins: int):

        fig, ax = plt.subplots(1)

        ax.set_title(pair)
        sns.histplot(data=mbo, bins=bins, kde=True, ax=ax)
        ax.set_xlabel("MBO")
        ax.set_ylabel("Count")

        # plt.show()

        box_layout = MDRelativeLayout()
        box_layout.size_hint = (None, None)

        # widget = MDWidget()
        # widget.size_hint = (None, None)

        box_layout.height = 400
        box_layout.width = 550
        box_layout.default_height = box_layout.height
        box_layout.default_width = box_layout.width
        # canvas = fig.canvas
        # box_layout.add_widget(canvas)
        figure = FigureCanvasKivyAgg(plt.gcf())
        box_layout.add_widget(figure)
        box_layout.figure = figure
        box_layout.bind(on_touch_down=ShowHistograms.figure_press)
        box_layout.zooming = False
        box_layout.size_binded = False
        # figure.pos = (10,10)
        self.ids.hist_stack_layout.add_widget(box_layout, index=1)
        self.figures.append(box_layout)

    @ staticmethod
    def figure_press(widget, touch):
        print('presed')
        print(widget)
        print(touch)
        # print(dir(touch))

        def auto_resise(parent, args):
            print(1)
            if widget.zooming:
                widget.width = parent.width - dp(100)
                widget.height = parent.parent.height
            # else:
            #     widget.width = widget.default_width
            #     widget.height = widget.default_height

        def update(dt):
            widget.width = widget.default_width
            widget.height = widget.default_height

        if widget.collide_point(*touch.pos):
            if touch.button == 'left':
                if not widget.zooming:
                    ratio = widget.height / widget.width
                    print("34")
                    widget.width = widget.parent.width - dp(100)
                    widget.height = widget.parent.parent.parent.height
                    if not widget.size_binded:
                        widget.parent.bind(size=auto_resise)
                    widget.size_binded = True
                    widget.zooming = True
                else:
                    Clock.schedule_once(update, 0)
                    widget.zooming = False
