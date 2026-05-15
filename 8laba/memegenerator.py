import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk
from models import MemeModel, MemeError

class MemeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MemeMaker")
        self.model = MemeModel()
        
        # Интерфейс
        tk.Button(root, text="Загрузить", command=self.load).pack(pady=5)
        self.top = tk.Entry(root, width=30)
        self.top.pack()
        self.bottom = tk.Entry(root, width=30)
        self.bottom.pack()
        tk.Button(root, text="Сделать мем", command=self.make).pack(pady=5)
        tk.Button(root, text="Сохранить", command=self.save).pack(pady=5)
        
        self.canvas = tk.Canvas(root, bg="gray", width=400, height=300)
        self.canvas.pack(pady=10)
    
    def load(self):
        path = filedialog.askopenfilename()
        if path:
            try:
                img = self.model.load(path)
                self.show(img)
            except Exception as e:
                messagebox.showerror("Ошибка", str(e))
    
    def make(self):
        try:
            img = self.model.make(self.top.get(), self.bottom.get())
            self.show(img)
        except MemeError as e:
            messagebox.showerror("Ошибка", str(e))
    
    def show(self, img):
        img_copy = img.copy()
        img_copy.thumbnail((400, 300))
        self.tk_img = ImageTk.PhotoImage(img_copy)
        self.canvas.delete("all")
        self.canvas.create_image(200, 150, image=self.tk_img)
    
    def save(self):
        try:
            img = self.model.get_image()
            if not img:
                raise MemeError("Нет мема")
            path = filedialog.asksaveasfilename(defaultextension=".png")
            if path:
                img.save(path)
                messagebox.showinfo("Успех", "Сохранено!")
        except MemeError as e:
            messagebox.showerror("Ошибка", str(e))

# Запуск
root = tk.Tk()
MemeApp(root)
root.mainloop()