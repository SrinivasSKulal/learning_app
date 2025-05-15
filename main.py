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
from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
