import tkinter as tk

def a_hello():
    label2.config(text="hello, random user :).....!!!")
root=tk.Tk()
root.title("Greeting app")
root.geometry("500x500")
root.config(bg="purple")
label1=tk.Label(root,text="click the button",fg="blue",bg="green",font=("Arial",16))
label1.pack()

button=tk.Button(root, text="greet",command=a_hello)
button.pack(pady=40)
label2=tk.Label(root,text="")
label2.pack(pady=40)
root.mainloop()