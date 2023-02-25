import threading
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
import matplotlib.pyplot as plt
import seaborn as sns
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

from kivy.metrics import dp
from functools import partial
from show_histograms.save_fig import SaveFig
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from main_kivy import myApp

Builder.load_file("show_histograms/showhistograms.kv")
Builder.load_file("show_histograms/savefig.kv")
Builder.load_file("show_histograms/savefigtextinput.kv")


class ShowHistograms(MDBoxLayout):

    figures: list = []
    free_index: int = 0
    first_used: bool = True

    def __init__(self, **kwargs):
        global figs
        figs = []
        global on_save_fig
        on_save_fig = False
        global fig_titles_data
        fig_titles_data = []
        super().__init__(**kwargs)

    def make_hists(self, pair: str, mbo: list[float], bins: int):

        if self.first_used:
            self.ids.hist_stack_layout.remove_widget(
                self.ids.info_label)
            self.first_used = False

        global figs
        global fig_titles_data

        sns.set_theme(context='notebook', style='white',
                      palette='deep', font='sans-serif',
                      font_scale=1, color_codes=True, rc=None)

        fig, ax = plt.subplots(1)
        figs.append(fig)
        fig_titles_data.append((pair, mbo, bins))

        ax.set_title(pair)

        sns.histplot(data=mbo, bins=bins, kde=True, ax=ax)
        ax.set_xlabel("MBO")
        ax.set_ylabel("Count")

        relative_layout = MDRelativeLayout()
        relative_layout.size_hint = (None, None)

        relative_layout.height = 420
        relative_layout.width = 550
        relative_layout.default_height = relative_layout.height
        relative_layout.default_width = relative_layout.width

        figure = FigureCanvasKivyAgg(plt.gcf())
        relative_layout.add_widget(figure)
        relative_layout.figure = figure
        relative_layout.bind(on_touch_down=ShowHistograms.figure_press)
        relative_layout.zooming = False
        relative_layout.size_binded = False
        relative_layout.fig_id = self.free_index

        self.ids.hist_stack_layout.add_widget(relative_layout,
                                              index=self.free_index)
        self.free_index += 1
        self.figures.append(relative_layout)
        Clock.schedule_once(self.switch_to_histogram_tab, 0)

    def switch_to_histogram_tab(self, dt):
        myApp.root.ids.main_tabs_of_app.switch_tab(
            "Histograms")

    @ staticmethod
    def figure_press(widget, touch):
        global on_save_fig

        def auto_resise(parent, args):
            if widget.zooming:
                widget.width = parent.width - dp(100)
                widget.height = parent.parent.height

        def update_f(dt):
            widget.width = widget.default_width
            widget.height = widget.default_height

        def update_t(dt):
            widget.parent.parent.scroll_y = 1

        def update_other(child, dt):
            child.width = child.default_width
            child.height = child.default_height

        if not on_save_fig:
            if widget.collide_point(*touch.pos):
                if touch.button == 'left':
                    if not widget.zooming:
                        p = widget.parent
                        nr = len(p.children)

                        for child in p.children:
                            if child.zooming:
                                Clock.schedule_once(
                                    partial(update_other, child), 0)
                                child.zooming = False

                        p.remove_widget(widget)
                        p.add_widget(widget, index=nr)
                        widget.width = widget.parent.width - dp(100)
                        widget.height = widget.parent.parent.parent.height
                        if not widget.size_binded:
                            widget.parent.bind(size=auto_resise)
                        widget.size_binded = True
                        widget.zooming = True

                        Clock.schedule_once(update_t, 0)
                    else:
                        Clock.schedule_once(update_f, 0)
                        widget.zooming = False
                elif touch.button == 'right':
                    pos_temp = list(widget.to_local(*touch.pos))

                    widget_f = SaveFig()

                    box_width = widget_f.ids.save_fig_widget.width
                    box_height = widget_f.ids.save_fig_widget.height

                    if (pos_temp[0] + box_width) >= widget.width:
                        pos_temp[0] = pos_temp[0] - box_width

                    if (pos_temp[1] + box_height) >= widget.height:
                        pos_temp[1] = pos_temp[1] - box_height

                    widget_f.pos = tuple(pos_temp)
                    widget.add_widget(widget_f)
                    on_save_fig = True

    def save_fig(self, id: int, path, width: float,
                 height: float):
        global fig_titles_data
        pair, mbo, bins = fig_titles_data[id]

        fig_s, ax_s = plt.subplots(1)
        cm = 1 / 2.54
        fig_s.set_figwidth(width*cm)
        fig_s.set_figheight(height*cm)

        ax_s.set_title(pair)
        ax_s.set_xlabel("MBO")
        ax_s.set_ylabel("Count")

        sns.histplot(data=mbo, bins=bins, kde=True, ax=ax_s)
        fig_s.set_figwidth(width)
        fig_s.set_figheight(height)
        fig_s.savefig(path)
        plt.close()

    def remove_all_figs(self):
        self.ids.hist_stack_layout.clear_widgets()
        self.figures = []
        self.free_index = 0
        global figs
        figs = []
        global fig_titles_data
        fig_titles_data = []
        global on_save_fig
        on_save_fig = False

    def update_text_inputs(self):
        global on_save_fig
        # Because of problem of theming in TextInput in kivyMD
        if on_save_fig:
            for child in self.ids.hist_stack_layout.children:
                for child_2 in child.children:
                    if type(child_2) is SaveFig:

                        def update(child_2, dt):
                            child_2.ids.save_fig_text_input_1.focus = True
                            child_2.ids.save_fig_text_input_1.focus = False
                            child_2.ids.save_fig_text_input_2.focus = True
                            child_2.ids.save_fig_text_input_2.focus = False

                        Clock.schedule_once(partial(update, child_2), 0)

    def set_on_save(self, value: bool):
        global on_save_fig
        on_save_fig = value
