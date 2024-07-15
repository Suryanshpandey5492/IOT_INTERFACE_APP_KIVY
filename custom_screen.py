# custom_screen.py

from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle

class CustomScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            self.bg_color = Color(242 / 255.0, 244 / 255.0, 246 / 255.0, 1)  # Set your background color here
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)
            self.bind(pos=self.update_bg, size=self.update_bg)

    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
