import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import pyperclip
import tkinter as tk
from tkinter import filedialog

def process_image():

    file_path = filedialog.askopenfilename(filetypes=[('JPEG Files', '*.jpg')])

    img = cv2.imread(file_path)

    cv2.imshow("Wybierz obszar z tekstem", img)
    rect = cv2.selectROI("Wybierz obszar z tekstem", img, fromCenter=False, showCrosshair=True)

    (x, y, w, h) = rect
    cropped_img = img[y:y+h, x:x+w]
    gray_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray_img, lang='eng')

    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, text)

def copy_text():
    text = text_box.get("1.0", tk.END)
    pyperclip.copy(text)

root = tk.Tk()
root.title("OCR - wybór obrazu")
root.geometry("400x250")

button = tk.Button(root, text="Wybierz obraz", command=process_image)
button.pack(pady=10)

text_box = tk.Text(root, height=10)
text_box.pack()

copy_button = tk.Button(root, text="Kopiuj", command=copy_text)
copy_button.pack(pady=(10))

root.mainloop()
