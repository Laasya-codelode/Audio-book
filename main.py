import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

for num in range(0, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()  # extractText() is also deprecated
    player = pyttsx3.init()
    player.say(text)            # removed the player.say=(text) line, that was a bug
    player.runAndWait()