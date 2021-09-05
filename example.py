from kivy.lang import Builder
from kivymd.app import MDApp
from cardstack import CardStack
from kivy.clock import Clock
from kivy.uix.button import Button


class MainApp(MDApp):
    def build(self):
        self.cardstack = CardStack()
        self.cardstack.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.cardstack.size = (800, 800)
        return self.cardstack

    def on_start(self):
        Clock.schedule_interval(self.runner, 2)

    def runner(self, *args):
        self.cardstack.change()
        self.cardstack.current_card.add_widget(Button(size_hint=(0.5, 0.5)))


if __name__ == "__main__":
    MainApp().run()
