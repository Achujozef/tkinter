import tkinter as tk

def click(event):
    current =display.get()
    text= event.widget.cget('text')
    
    if text == "=":
        result =eval(current)
        display.delete(0,tk.END)
        display.insert(tk.END,result)
    elif text == "C":
        display.delete(0,tk.END)
    else:
        display.insert(tk.END,text)


window =tk.Tk()
window.title("Calculator")

display = tk.Entry(window,font=("Airal",25),justify="right")
display.pack(fill=tk.X,padx=10, pady=10, ipady=10)

btn_frame =tk.Frame(window)
btn_frame.pack()


button_labels =[
    "7","8","9","/",
    "4","5","6","-",
    "1","2","3","*",
    "C","0","=","+",
]

i=0
for label in button_labels:
    button = tk.Button(btn_frame, text=label, font=("Arial",18),padx=20,pady=20)
    button.grid(row=i//4,column=i%4,padx=10,pady=10)
    button.bind("<Button-1>",click)
    i+=1


window.mainloop()



# button7 =tk.Button(btn_frame,text="7",font=("Arial",20))
# button7.grid(row=0, column=0)

# button7 =tk.Button(btn_frame,text="8",font=("Arial",20))
# button7.grid(row=0, column=1)


# button7 =tk.Button(btn_frame,text="9",font=("Arial",20))
# button7.grid(row=0, column=2)


# button7 =tk.Button(btn_frame,text="+",font=("Arial",20))
# button7.grid(row=0, column=3)
