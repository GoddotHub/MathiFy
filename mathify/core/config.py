# ================= App Settings =================
APP_NAME = "Mathify"

# Default theme
THEME_STYLE = "Dark"  # Options: "Light", "Dark"
PRIMARY_COLOR = "Blue"

# File where history will be saved
SAVE_HISTORY_FILE = "history.json"

# Auto-solve behavior
AUTO_SOLVE_DEFAULT = False
DEFAULT_THEME = "dark"

# History settings
MAX_HISTORY_ITEMS = 50

# Keyboard settings
KEYBOARD_LAYOUT = [
    ["7", "8", "9", "/", "√"],
    ["4", "5", "6", "*", "^"],
    ["1", "2", "3", "-", "("],
    ["0", ".", "=", "+", ")"],
    ["x", "y", "π", "e", "C"],
    ["sin", "cos", "tan", "log", "ln"]
]

# Supported operators/functions for parser validation
SUPPORTED_OPERATORS = ["+", "-", "*", "/", "**", "^", "(", ")", "√"]
SUPPORTED_FUNCTIONS = ["sin", "cos", "tan", "log", "ln", "sqrt"]

# Default TextInput settings
INPUT_FONT_SIZE = 28
RESULT_FONT_SIZE = 22