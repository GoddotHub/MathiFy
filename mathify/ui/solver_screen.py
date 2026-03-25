# ui/solver_screen.py

from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.core.clipboard import Clipboard

from core.camera_ocr import CameraOCR
from controllers.app_controller import AppController


class SolverScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.controller = AppController()
        self.history = []
        self.dark_mode = True
        self.auto_solve = False
        self.colors = self.get_colors()

        # Step system
        self.steps = []
        self.current_step = 0

        # ===== MAIN LAYOUT =====
        main_layout = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=10
        )

        # ===== INPUT =====
        self.input_box = TextInput(
            hint_text="Enter math expression...",
            multiline=False,
            font_size=28,
            size_hint_y=None,
            height=70,
            background_color=self.colors['input_bg'],
            foreground_color=self.colors['input_fg']
        )

        # ===== RESULT =====
        self.result_label = Label(
            text="Result will appear here",
            font_size=24,
            size_hint_y=None,
            height=60,
            color=self.colors['text']
        )

        # ===== BUTTON ROW =====
        button_row = BoxLayout(size_hint_y=None, height=50, spacing=10)

        self.solve_button = Button(text="Solve")
        self.solve_button.bind(on_press=self.on_solve)

        self.clear_input_btn = Button(text="Clear")
        self.clear_input_btn.bind(on_press=self.clear_input)

        button_row.add_widget(self.solve_button)
        button_row.add_widget(self.clear_input_btn)

        # ===== NEXT STEP BUTTON (FIXED POSITION) =====
        self.next_step_btn = Button(text="Next Step", size_hint_y=None, height=50)
        self.next_step_btn.bind(on_press=self.show_next_step)

        # ===== EXTRA BUTTONS =====
        self.copy_btn = Button(text="Copy Result", size_hint_y=None, height=50)
        self.copy_btn.bind(on_press=self.copy_result)

        self.auto_btn = Button(text="Auto-Solve: OFF", size_hint_y=None, height=50)
        self.auto_btn.bind(on_press=self.toggle_auto)

        self.theme_btn = Button(text="Toggle Theme", size_hint_y=None, height=50)
        self.theme_btn.bind(on_press=self.toggle_theme)

        # ===== OCR =====
        self.image_widget = Label(size_hint_y=0.3)
        self.camera_ocr = CameraOCR(
            image_widget=self.image_widget,
            on_result=self.handle_camera_result
        )

        self.capture_btn = Button(text="Capture", size_hint_y=None, height=50)
        self.capture_btn.bind(on_press=self.capture_image)

        # ===== HISTORY =====
        self.history_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.history_layout.bind(minimum_height=self.history_layout.setter('height'))

        # ===== ADD WIDGETS =====
        main_layout.add_widget(self.input_box)
        main_layout.add_widget(button_row)
        main_layout.add_widget(self.result_label)
        main_layout.add_widget(self.next_step_btn)  # ✅ FIXED
        main_layout.add_widget(self.copy_btn)
        main_layout.add_widget(self.capture_btn)
        main_layout.add_widget(self.image_widget)
        main_layout.add_widget(self.auto_btn)
        main_layout.add_widget(self.history_layout)
        main_layout.add_widget(self.theme_btn)

        self.add_widget(main_layout)

        # Safe binding
        self.input_box.bind(text=self.on_text_change)

    # ================= SOLVE =================
    def on_solve(self, instance):
        exp = self.input_box.text.strip()

        if not exp:
            self.result_label.text = "Enter something"
            return

        self.steps = self.controller.get_steps(exp)
        self.current_step = 0

        self.show_next_step(None)

        # Save to history
        self.history.append(exp)
        self.update_history()

    def show_next_step(self, instance):
        if not self.steps:
            return

        if self.current_step < len(self.steps):
            self.result_label.text = self.steps[self.current_step]
            self.current_step += 1
        else:
            self.result_label.text = "✅ Done"

    # ================= HISTORY =================
    def update_history(self):
        self.history_layout.clear_widgets()
        for item in self.history[-20:][::-1]:
            self.history_layout.add_widget(
                Label(text=item, size_hint_y=None, height=30)
            )

    # ================= INPUT =================
    def on_text_change(self, instance, value):
        if self.auto_solve and value.strip():
            self.on_solve(None)

    def toggle_auto(self, instance):
        self.auto_solve = not self.auto_solve
        self.auto_btn.text = f"Auto-Solve: {'ON' if self.auto_solve else 'OFF'}"

    def clear_input(self, instance):
        self.input_box.text = ""

    def clear_history(self, instance):
        self.history.clear()
        self.update_history()

    # ================= COPY =================
    def copy_result(self, instance):
        Clipboard.copy(self.result_label.text)

    # ================= OCR =================
    def capture_image(self, instance):
        self.camera_ocr.capture()

    def handle_camera_result(self, text, result):
        self.input_box.text = text
        self.result_label.text = result

    # ================= THEME =================
    def toggle_theme(self, instance):
        self.dark_mode = not self.dark_mode
        self.colors = self.get_colors()

    def get_colors(self):
        if self.dark_mode:
            return {
                "input_bg": get_color_from_hex("#333333"),
                "input_fg": (1, 1, 1, 1),
                "text": (1, 1, 1, 1)
            }
        else:
            return {
                "input_bg": get_color_from_hex("#EEEEEE"),
                "input_fg": (0, 0, 0, 1),
                "text": (0, 0, 0, 1)
            }