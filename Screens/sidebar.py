from kivymd.uix.boxlayout import MDBoxLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivymd.uix.button import MDRaisedButton
from kivy.properties import ListProperty
from kivy.clock import Clock

class Sidebar(MDBoxLayout):
    screen_buttons = ListProperty([
        {'screen': 'dashboard', 'label': 'Dashboard'},
        {'screen': 'graph', 'label': 'Graph'},
        {'screen': 'control', 'label': 'Control'},
        {'screen': 'settings', 'label': 'Settings'}
    ])

    def __init__(self, **kwargs):
        super(Sidebar, self).__init__(**kwargs)
        self.rect = None  # Initialize the rect attribute
        self.bind(pos=self.update_rect, size=self.update_rect)
        Window.bind(mouse_pos=self.on_mouse_pos)

        with self.canvas.before:
            Color(0.121, 0.161, 0.216, 1)  # #1f2937 in RGBA
            self.rect = Rectangle(pos=self.pos, size=self.size)

        Clock.schedule_once(self.create_buttons, 0)

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

    def create_buttons(self, *args):
        buttons_box = self.ids.buttons_box
        for button_info in self.screen_buttons:
            button = MDRaisedButton(
                text=button_info['label'],
                on_press=lambda x, screen=button_info['screen']: self.change_screen(screen),
                md_bg_color=(0.121, 0.161, 0.216, 1),
                theme_text_color='Custom',
                text_color=(1, 1, 1, 1),
                size_hint=(0.9, None),  # Set button width to 90% of the sidebar's width
                height=50  # Adjust button height to match the design
            )
            buttons_box.add_widget(button)
