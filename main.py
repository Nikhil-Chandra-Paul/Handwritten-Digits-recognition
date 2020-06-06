from keras.models import load_model
from tkinter import *
import tkinter as tk
from PIL import ImageGrab, Image,ImageTk
import numpy as np

model = load_model('mnist.h5')
def predict_digit(img):

    img = img.resize((28,28))
    img = img.convert('L')
    img = np.array(img)

    img = img.reshape(1,28,28,1)
    img = img/255.0

    res = model.predict([img])[0]
    
    return np.argmax(res), max(res)

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.x = self.y = 0
        self.resizable(0,0)


        self.canvas = tk.Canvas(self, width=400, height=400, bg = "black", cursor="cross")
        self.label = tk.Label(self, text="Thinking..", font=("Helvetica", 43))
        self.classify_btn = tk.Button(self, text = "Recognise", command =self.classify_handwriting,width=25,height=5,bd=5)
        self.button_clear = tk.Button(self, text = "Clear", command = self.clear_all,width=10,height=5,bd=5)
        self.lab=tk.Label(self,text="Hello....")
        
        self.lab.pack()
        self.canvas.pack()
        self.label.pack()
        self.classify_btn.pack()
        self.button_clear.pack()
        

        self.canvas.bind("<B1-Motion>", self.draw_lines)

    def clear_all(self):
        self.canvas.delete("all")
    def classify_handwriting(self):
    
        im=ImageGrab.grab((700,50,1200,650))
    
        digit, acc = predict_digit(im)
        self.label.configure(text= str(digit)+', '+ str(int(acc*100))+'%')
    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r=25
        self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, outline='white',fill='white')
    

app = App()
mainloop()
