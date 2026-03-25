from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from core.constants import APP_TITLE, BUTTON_COLOR, BUTTON_TEXT_COLOR

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # ===== Main layout =====
        layout = MDBoxLayout(
            orientation="vertical",
            padding=50,
            spacing=30,
            adaptive_size=True
        )

        # ===== App title =====
        title = MDLabel(
            text=APP_TITLE,
            halign="center",
            font_style="H2"
        )

        # ===== Start button =====
        start_btn = MDRaisedButton(
            text="Start Solving",
            pos_hint={"center_x": 0.5},
            md_bg_color=BUTTON_COLOR,
            text_color=BUTTON_TEXT_COLOR
        )
        start_btn.bind(on_press=self.go_to_solver)

        # ===== Add widgets =====
        layout.add_widget(title)
        layout.add_widget(start_btn)
        self.add_widget(layout)

    def go_to_solver(self, instance):
        """Switch to solver screen"""
        self.manager.current = "solver"