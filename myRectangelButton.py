from kivymd.uix.button import MDIconButton
from kivy.core.window import Window


class MyRectangleButton(MDIconButton):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouseover)

    def on_mouseover(self, window, pos):

        delta_height = (self.parent.content_in_MDScrollView_height
                        + self.parent.content_outside_MDScrollView_height
                        - Window.height)

        corrected_pos = (pos[0], pos[1] + delta_height *
                         self.parent.scroll_view.scroll_y)

        # because parent is RelativeLayout we must have position of parent:
        pos_relative_to_parent = (pos[0] - self.parent.pos[0],
                                  corrected_pos[1] - self.parent.pos[1])

        if self.collide_point(pos_relative_to_parent[0], pos_relative_to_parent[1]):
            self.icon_color = 'black'
        else:
            self.icon_color = 'white'
