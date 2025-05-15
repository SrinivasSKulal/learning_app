from customtkinter import *
from PIL import Image

app = CTk()

app.geometry("500x400")
img = Image.open("message.png")
set_appearance_mode("dark")

def on_click(value):
    print("Selected " , value)



combox = CTkComboBox(master=app , values=["1" , "2" , "3"] , command=on_click)
checkbox = CTkCheckBox(master=app , text="Option")
switch = CTkSwitch(master=app, text="Hello")
slider = CTkSlider(master=app , from_=0 , to=100, number_of_steps=5)
entry = CTkEntry(master=app, placeholder_text="Enter something")
combox.place(relx=0.5, rely=0.1 , anchor="n")
btn = CTkButton(master=app , text ="Click me", corner_radius=32,fg_color="#c850c0",hover_color="#4158d0" , border_color="#ffcc70" , border_width=2 , image=CTkImage(dark_image=img,light_image=img))
btn.place(relx=0.5 , rely = 0.5 , anchor="center") 
app.mainloop()

