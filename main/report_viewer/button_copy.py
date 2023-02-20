from kivymd.uix.button import MDTextButton
from kivymd.color_definitions import colors
from kivy.core.window import Window


class ButtonCopy(MDTextButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_mouse_down=self.on_mouse_down)
        Window.bind(mouse_pos=self.on_mouseover)

    def on_mouseover(self, window, pos):
        pos = self._recalculate_position_to_relative(*pos)
        if self.collide_point(pos[0], pos[1]):
            self.text_color = "black"
        else:
            self.text_color = "white"

    def _recalculate_position_to_relative(self, x, y):
        delta_height = (self.parent.parent.parent.parent.parent.nav_bar_hight
                        + self.parent.parent.parent.height
                        - Window.height)

        pos = (x, y + delta_height *
               self.parent.parent.parent.parent.scroll_y)

        x = pos[0] - self.parent.parent.parent.parent.pos[0]
        y = pos[1] - self.parent.parent.parent.parent.pos[1]
        return x, y

    def _revers_y_coordinate(self, y):
        y = Window.height - y
        return y

    def on_mouse_down(self, window, x, y, *modifiers):
        if modifiers[0] == 'left':
            y = self._revers_y_coordinate(y)
            pos = self._recalculate_position_to_relative(x, y)
            if self.collide_point(pos[0], pos[1]):

                # copy to windows
                self.parent.children[1]\
                    .copy(self.parent.children[1].selection)

        self.parent.children[1].selection = ''
        Window.unbind(mouse_pos=self.on_mouseover)
        Window.unbind(on_mouse_down=self.on_mouse_down)

        if self.parent.children[1]:
            self.parent.children[1].button_copy = None
        self.parent.remove_widget(self)
