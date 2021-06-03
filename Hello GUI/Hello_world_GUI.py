#Hello world GUI
#Icon source http://www.iconsmind.com

import tkinter
from tkinter import BOTH,END, PhotoImage, StringVar, image_names
from PIL import ImageTk, Image

root=tkinter.Tk()
root.title("Hello GUI")
#root.iconbitmap("")
root.geometry("400x400")
root.resizable(0,0)

root_color = "#224870"
input_color = "#2a4494"
output_color = "#4ea5d9"
root.config(bg=root_color)

#define Function
def submit_name():
    '''say hello to the user'''
    if case_style.get() == "normal":
        name_label = tkinter.Label(output_frame, text = "Hello "+ name.get() + " ! Keep learning Tkinter")
    elif case_style.get() == 'upper':
        name_label = tkinter.Label(output_frame, text = ("Hello "+ name.get() + " ! Keep learning Tkinter").upper())

    #pack label onto screen
    name_label.pack()

    # clear the entry name for next user
    name.delete(0,END)


#define layout
#define frame
input_frame = tkinter.LabelFrame(root, bg = input_color)
output_frame = tkinter.LabelFrame(root, bg = output_color)
input_frame.pack()
output_frame.pack(padx= 10, pady =(0,10), fill = BOTH, expand= True)

#create widtge 
name = tkinter.Entry(input_frame, text= "Enter your name: ", width = 20)
submit_button = tkinter.Button(input_frame, text = "Submit", command=submit_name)
name.grid(row = 0, column = 0,padx = 10, pady = 10)
submit_button.grid(row= 0, column = 1, padx = 10, pady = 10, ipadx = 20)

#create radio button for text display
case_style = StringVar()
case_style.set("normal")
normal_button = tkinter.Radiobutton(input_frame, text= "Normal Case", variable = case_style, value = "normal", bg = input_color )
upper_button = tkinter.Radiobutton(input_frame, text = "Upper Case", variable = case_style, value = "upper", bg = input_color)
normal_button.grid(row = 1, column = 0, padx =2, pady =2 )
upper_button.grid(row= 1, column = 1, padx = 2, pady =2 )

# add an image
smile_image = ImageTk.PhotoImage(Image.open("smile.png"))
smile_label = tkinter.Label(output_frame, image = smile_image, bg= output_color)
smile_label.pack()

#run root windows
root.mainloop()







