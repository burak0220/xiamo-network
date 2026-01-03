from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import ctypes
import os

class XiamoApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        self.status = Label(text="Xiamo Mobile Node Ready", font_size='20sp')
        btn = Button(text="Start Mining", size_hint=(1, 0.2))
        btn.bind(on_press=self.start_mining)
        layout.add_widget(self.status)
        layout.add_widget(btn)
        return layout

    def start_mining(self, instance):
        self.status.text = "Mining Started..."

if __name__ == '__main__':
    XiamoApp().run()
