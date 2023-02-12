from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.dialog import MDDialog


class NavButton(MDFillRoundFlatIconButton, HoverBehavior):
    dialog: MDDialog

    def on_enter(self, *args):
        self.md_bg_color = self.theme_cls.hover_color

    def on_leave(self, *args):
        self.md_bg_color = self.theme_cls.primary_color
