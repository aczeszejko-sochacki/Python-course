import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.clock import Clock

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '500')


class Menu(GridLayout):

    counter_time = 0
    switched_on = False

    def set_value(self, time_value):
        if self.switched_on is False:
            self.ids.timer.text = time_value

    def timer(self, iterations_number):
        if self.switched_on is False and iterations_number != 'KONIEC':
            self.switched_on = True
            self.counter_time = int(iterations_number)
            Clock.max_iteration = int(iterations_number)
            Clock.schedule_interval(self.decrement_time, 0.5)

    def decrement_time(self, dt):
        self.ids.timer.text = str(self.counter_time)

        if self.counter_time == 0:
            Clock.unschedule(self.decrement_time)
            self.ids.timer.text = str('KONIEC')
            self.switched_on = False

        self.counter_time -= 0.5

    def stop_timer(self):
        if self.switched_on is True:
            Clock.unschedule(self.decrement_time)
            self.ids.timer.text = str(0.0)
            self.switched_on = False


class TimerApp(App):

    def build(self):
        return Menu()


if __name__ == "__main__":
    timer_app = TimerApp()
    timer_app.run()
