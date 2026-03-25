from kivy.utils import platform
from kivy.graphics.texture import Texture
from PIL import Image as PILImage
import pytesseract
from core.parser import solve_equation_auto

# Mobile camera support
if platform in ('android', 'ios'):
    from plyer import camera
else:
    from tkinter import Tk, filedialog


class CameraOCR:
    def __init__(self, image_widget=None, on_result=None):
        """
        image_widget: optional Kivy Image widget to display the captured photo
        on_result: callback function that receives recognized text and result
        """
        self.image_widget = image_widget
        self.on_result = on_result

    def capture(self):
        """Capture image from camera (mobile) or file picker (desktop)."""
        if platform in ('android', 'ios'):
            try:
                camera.take_picture(filename="captured.png", on_complete=self.process_image)
            except Exception as e:
                print("Camera error:", e)
                if self.on_result:
                    self.on_result("", f"Camera error: {e}")
        else:
            try:
                root = Tk()
                root.withdraw()
                filepath = filedialog.askopenfilename(
                    title="Select image",
                    filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
                )
                root.destroy()
                if filepath:
                    self.process_image(filepath)
                else:
                    if self.on_result:
                        self.on_result("", "No file selected")
            except Exception as e:
                print("File picker error:", e)
                if self.on_result:
                    self.on_result("", f"Error: {e}")

    def process_image(self, filepath):
        """Display image (optional), run OCR, and solve the detected equation."""
        try:
            pil_image = PILImage.open(filepath).convert("RGB")

            # Display image in Kivy Image widget
            if self.image_widget:
                # Convert PIL image to Kivy texture
                tex = Texture.create(size=pil_image.size)
                tex.flip_vertical()  # Kivy textures are flipped vertically
                tex.blit_buffer(pil_image.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
                self.image_widget.texture = tex

            # OCR with pytesseract
            detected_text = pytesseract.image_to_string(pil_image).strip()

            # Solve equation using parser
            result = solve_equation_auto(detected_text)

            # Callback with recognized text and solution
            if self.on_result:
                self.on_result(detected_text, result)

        except Exception as e:
            print("Error processing image:", e)
            if self.on_result:
                self.on_result("", f"Error: {e}")