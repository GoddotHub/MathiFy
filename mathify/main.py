from kivymd.app import MDApp
from ui.main_screen import MainScreen


class MathifyApp(MDApp):
    def build(self):
        # ===== Theme Settings =====
        self.theme_cls.primary_palette = "Blue"  # Main color
        self.theme_cls.theme_style = "Dark"      # Dark/Light theme

        # ===== Root Widget =====
        self.main_screen = MainScreen()
        return self.main_screen

    def on_start(self):
        """
        Called after app starts.
        Can be used to initialize global things like keyboard focus or splash screens.
        """
        pass


if __name__ == "__main__":
    MathifyApp().run()