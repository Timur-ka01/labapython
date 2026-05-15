from PIL import Image, ImageDraw, ImageFont

class MemeError(Exception):
    pass

class MemeModel:
    def __init__(self):
        self.img = None
    
    def load(self, path):
        self.img = Image.open(path)
        return self.img
    
    def make(self, top, bottom):
        if not self.img:
            raise MemeError("Нет фото")
        
        mem = self.img.copy()
        draw = ImageDraw.Draw(mem)
        
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            font = ImageFont.load_default()
        
        w, h = mem.size
        
        if top:
            draw.text(((w - len(top)*20)//2, 20), top, fill="white", font=font)
        if bottom:
            draw.text(((w - len(bottom)*20)//2, h-60), bottom, fill="white", font=font)
        
        self.img = mem
        return mem
    
    def get_image(self):
        return self.img