from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.utils import get_color_from_hex


# ===== Reusable Text Input =====
def create_input_box(hint_text="Enter math...", height=60, dark_mode=True):
    bg = get_color_from_hex("#333333") if dark_mode else get_color_from_hex("#EEEEEE")
    fg = (1, 1, 1, 1) if dark_mode else (0, 0, 0, 1)

    return TextInput(
        hint_text=hint_text,
        multiline=False,
        font_size=28,
        size_hint_y=None,
        height=height,
        background_color=bg,
        foreground_color=fg
    )


# ===== Reusable Result Label =====
def create_result_label(text="Answer will appear here", height=50, dark_mode=True):
    color = (1, 1, 1, 1) if dark_mode else (0, 0, 0, 1)
    return Label(
        text=text,
        font_size=22,
        size_hint_y=None,
        height=height,
        color=color
    )


# ===== Reusable MD Button =====
def create_md_button(text="Button", height=50, size_hint=(1, None), pos_hint=None):
    return MDRaisedButton(
        text=text,
        size_hint=size_hint,
        height=height,
        pos_hint=pos_hint or {"center_x": 0.5}
    )


# ===== Reusable Kivy Button =====
def create_button(text="Button", height=50, background_color=(0.3,0.3,0.3,1)):
    return Button(
        text=text,
        size_hint_y=None,
        height=height,
        background_color=background_color
    )


# ===== Reusable History Label =====
def create_history_label(text, height=30, dark_mode=True):
    color = (1, 1, 1, 1) if dark_mode else (0, 0, 0, 1)
    return Label(
        text=text,
        size_hint_y=None,
        height=height,
        color=color
    )