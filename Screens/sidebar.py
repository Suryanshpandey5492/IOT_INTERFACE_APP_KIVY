from kivymd.uix.boxlayout import MDBoxLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

class Sidebar(MDBoxLayout):
    def __init__(self, **kwargs):
        super(Sidebar, self).__init__(**kwargs)
        self.rect = None  # Initialize the rect attribute
        self.bind(pos=self.update_rect, size=self.update_rect)
        Window.bind(mouse_pos=self.on_mouse_pos)

        with self.canvas.before:
            Color(0.121, 0.161, 0.216, 1)  # #1f2937 in RGBA
            self.rect = Rectangle(pos=self.pos, size=self.size)

    def change_screen(self, screen_name):
        self.parent.parent.manager.current = screen_name

    def update_rect(self, *args):
        if self.rect:
            self.rect.pos = self.pos
            self.rect.size = self.size

    def on_mouse_pos(self, window, pos):
        for child in self.children:
            if child.collide_point(*pos):
                self.on_hover(child)
            else:
                self.on_leave(child)

    def on_hover(self, instance):
        instance.md_bg_color = (0.215, 0.255, 0.316, 1)  # Slightly lighter for hover effect

    def on_leave(self, instance):
        instance.md_bg_color = (0.121, 0.161, 0.216, 1)  # Back to original color
