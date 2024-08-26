import tkinter as tk
from tkinter import filedialog, ttk
import cv2
import pytesseract
from PIL import Image, ImageTk
import csv

class DocumentDigitalizationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Document Digitalization")
        self.master.geometry("1000x600")

        self.create_widgets()

    def create_widgets(self):
        # Left frame for image display
        self.left_frame = ttk.Frame(self.master, padding="10")
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.left_frame, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Right frame for extracted data
        self.right_frame = ttk.Frame(self.master, padding="10")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.data_text = tk.Text(self.right_frame, wrap=tk.WORD, width=50)
        self.data_text.pack(fill=tk.BOTH, expand=True)

        # Buttons
        self.upload_btn = ttk.Button(self.master, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(side=tk.BOTTOM, pady=10)

        self.save_btn = ttk.Button(self.master, text="Save to CSV", command=self.save_to_csv)
        self.save_btn.pack(side=tk.BOTTOM, pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")])
        if file_path:
            self.process_image(file_path)

    def process_image(self, file_path):
        # Display image
        image = Image.open(file_path)
        image.thumbnail((500, 500))  # Resize for display
        photo = ImageTk.PhotoImage(image)
        self.canvas.config(width=photo.width(), height=photo.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

        # Perform OCR
        img = cv2.imread(file_path)
        text = pytesseract.image_to_string(img)
        self.data_text.delete(1.0, tk.END)
        self.data_text.insert(tk.END, text)

    def save_to_csv(self):
        text = self.data_text.get(1.0, tk.END).strip()
        if text:
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if file_path:
                with open(file_path, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    for line in text.split('\n'):
                        writer.writerow([line])
                print(f"Data saved to {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DocumentDigitalizationApp(root)
    root.mainloop()