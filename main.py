from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, Clock, ObjectProperty, StringProperty


class BoxLayoutExample(BoxLayout):
    pass

class MainWidget(Widget):
    count = 0
    power = 1
    upgrade = 0
    upgrade2 = 0
    cost = 1
    cost2 = 1
    my_text = StringProperty("0")

    def on_button_click(self):
        self.count += int(self.power)
        self.my_text = str(self.count)
        print(self.power)

    def on_button_upgrade(self):
        self.cost += int(self.cost) * 0.25
        self.upgrade += 1
        self.count -= 50 * int(self.cost)
        self.power += int(self.upgrade)
        self.my_text = str(self.count)


    def on_button_upgrade2(self):
        self.cost2 += int(self.cost2) * 0.25
        self.upgrade2 += 5
        self.count -= 200 * int(self.cost2)
        self.power +=  int(self.upgrade2)
        self.my_text = str(self.count)

    def update(self, dt):
        #print("dt: " + str(dt*60))
        time_factor = dt*60
        self.on_button_click()
        self.on_button_upgrade()


class ClickApp(App):
    pass

ClickApp().run()
