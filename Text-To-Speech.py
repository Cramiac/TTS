import time

import pytesseract
import pyttsx3
from PIL import ImageGrab


def read_text_aloud(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the properties (optional)
    # You can set properties like volume, rate, and voice.
    # Uncomment and modify these lines as needed.

    # engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    # engine.setProperty('rate', 150)    # Speed (words per minute)
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)  # Use the first voice

    # Read the text aloud
    engine.say(text)

    # Block while processing all the currently queued commands
    engine.runAndWait()

def capture_screen_text():
    # Capture the screen as an image
    screen = ImageGrab.grab()

    # Perform OCR to extract text from the image
    text = pytesseract.image_to_string(screen)

    return text.strip()

if __name__ == "__main__":
    print("Automatic Text-to-Speech Application")
    print("Press Ctrl+C to stop the application.")
    
    try:
        while True:
            text_to_read = capture_screen_text()
            if text_to_read:
                print("Detected Text: ", text_to_read)
                read_text_aloud(text_to_read)
            time.sleep(1)  # Wait for 1 second before refreshing the image and processing again
    except KeyboardInterrupt:
        print("Application stopped.")
