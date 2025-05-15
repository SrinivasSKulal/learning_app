# from customtkinter import *
# from PIL import Image
#
# app = CTk()
#
# app.geometry("500x400")
# img = Image.open("message.png")
# set_appearance_mode("dark")
#
# def on_click():
#    print(entry.get()) 
#
#
# # combox = CTkComboBox(master=app , values=["1" , "2" , "3"] , command=on_click)
# # checkbox = CTkCheckBox(master=app , text="Option")
# # switch = CTkSwitch(master=app, text="Hello")
# # slider = CTkSlider(master=app , from_=0 , to=100, number_of_steps=5)
# entry = CTkEntry(master=app, placeholder_text="Enter something" , width=1000)
# entry.place(relx=0.5, rely=0.1 , anchor="n")
# btn = CTkButton(master=app , command=on_click,text ="Click me", corner_radius=32,fg_color="#c850c0",hover_color="#4158d0" , border_color="#ffcc70" , border_width=2 , image=CTkImage(dark_image=img,light_image=img))
# btn.place(relx=0.5 , rely = 0.5 , anchor="center") 
# app.mainloop()
#
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1", trust_remote_code=True)
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)
