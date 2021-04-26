from kivy.lang import Builder
from kivymd.app import MDApp
import CardStack
from kivy.clock import Clock
from kivy.uix.button import Button

class Mainapp(MDApp):
    def build(self):
        self.test = CardStack.CardStack()
        self.test.pos_hint = {'center_x':.5, "center_y":.5}
        self.test.size = (800,800)
        return self.test

    def on_start(self):
        Clock.schedule_interval(self.runner, 2)

    def runner(self, *args):
        self.test.change()
        self.test.current_card.add_widget(Button(size_hint = (.5,.5) )
                                                                )
if __name__ == "__main__":
    MainApp().run()
