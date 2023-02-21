from kivymd.uix.scrollview import MDScrollView
from kivy.lang.builder import Builder


Builder.load_file("myscrollview/myscrollview.kv")


class MyScrollView(MDScrollView):

    def on_touch_down(self, touch):
        super().on_touch_down(touch)

    def on_touch_up(self, touch):
        super().on_touch_up(touch)

    def on_touch_move(self, touch):
        if touch.button == 'left':

            coor_for_better_performance = 20

            if self.size_hint_x is not None:

                correction = self.width\
                    * ((1 - self.size_hint_x) / self.size_hint_x)

                if (touch.pos[0] < self.width + correction
                        and touch.pos[0] > self.width - self.bar_width
                        - coor_for_better_performance
                        + correction)\
                    and (touch.pos[1] > self.pos[1]
                         and touch.pos[1] < self.pos[1] + self.height):

                    super().on_touch_move(touch)

            else:
                if (touch.pos[0] < self.width + self.pos[0]
                        and touch.pos[0] > self.width - self.bar_width
                        - coor_for_better_performance)\
                    and (touch.pos[1] > self.pos[1]
                         and touch.pos[1] < self.pos[1] + self.height):

                    super().on_touch_move(touch)

        else:
            super().on_touch_move(touch)

    def on_bar_color(self, *args):
        # for update scroll after theme change
        # Sometimes theme color not update automatically
        self.update_from_scroll()

    def on_bar_inactive_color(self, *args):
        # for update scroll after theme change
        # Sometimes theme color not update automatically
        self.update_from_scroll()
