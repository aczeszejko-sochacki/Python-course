from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from clasificate_iris import Target
from basic_plot import BasicPlot
import pandas as pd
import kivy
import threading
kivy.require('1.10.0')


Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '700')


class Main(GridLayout):

    """Klasa główna"""

    def __init__(self):

        all_data = pd.read_csv('iris.csv')

        self.data = all_data.drop('species', axis=1)
        self.data = self.data.drop('Unnamed: 0', axis=1)
        self.data = self.data.values
        self.target = all_data['species']
        self.target = self.target.values

        basic_plot = BasicPlot()
        basic_plot.save_basic_plot(self.data, self.target)
        GridLayout.__init__(self)

    def set_clasificated(self, sl, sw, pl, pw, n_neighbours):

        """funkcja modyfikująca okno aplikacji po
        sklasyfikowaniu"""

        target = Target(self.data, self.target)

        if target.clasificate_all_iris(sl, sw, pl, pw, n_neighbours):
            self.ids.plot.reload()
            self.ids.comm.text = 'Correct parmaters. Please type new ones'


class MainApp(App):

    """klasa inicjalizująca aplikację"""

    def build(self):

        """funkcja inicjalizująca aplikację"""

        return Main()


if __name__ == "__main__":
    klasyfikator = MainApp()
    klasyfikator.run()
