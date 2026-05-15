import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

#Исключение
class MemeError(Exception):
    pass

#класс
class MemeMaker:
    def __init__(self, root):
        self.root = root
        self.root.title("MemeMaker")
        self.img = None
        
        # Кнопки и поля (минимум)
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
                self.img = Image.open(path)
                self.show()
            except:
                raise MemeError("Не загрузить фото")
    
    def show(self):
        img2 = self.img.copy()
        img2.thumbnail((400, 300))
        self.tk_img = ImageTk.PhotoImage(img2)
        self.canvas.create_image(200, 150, image=self.tk_img)
    
    def make(self):
        try:
            if not self.img: raise MemeError("Нет фото")
            
            mem = self.img.copy()
            draw = ImageDraw.Draw(mem)
            font = ImageFont.truetype("arial.ttf", 40)
            w, h = mem.size
            
            t = self.top.get()
            if t:
                draw.text(((w-len(t)*20)//2, 20), t, fill="white", font=font)
            
            b = self.bottom.get()
            if b:
                draw.text(((w-len(b)*20)//2, h-60), b, fill="white", font=font)
            
            self.img = mem
            self.show()
        except MemeError as e:
            messagebox.showerror("Ошибка", str(e))
    
    def save(self):
        try:
            if not self.img: raise MemeError("Нет мема")
            path = filedialog.asksaveasfilename(defaultextension=".png")
            if path:
                self.img.save(path)
                messagebox.showinfo("Ок", "Сохранено!")
        except MemeError as e:
            messagebox.showerror("Ошибка", str(e))
            
root = tk.Tk()
MemeMaker(root)
root.mainloop()