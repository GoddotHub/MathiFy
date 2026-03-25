from kivy.uix.screenmanager import ScreenManager
from ui.home_screen import HomeScreen
from ui.solver_screen import SolverScreen
from kivy.core.window import Window

class MainScreen(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(HomeScreen(name="home"))
        self.add_widget(SolverScreen(name="solver"))