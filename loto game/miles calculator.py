import tkinter as tk


def convert():
    miles= float(enter_miles.get())
    kilometers=miles*1.60934
    label_result.config(text=f"{miles}miles is equal to{kilometers}kilometers.")


root=tk.Tk()
root.title("miles to kilometers converter")
    

label_miles=tk.Label(root,text="enter distance in miles:")
enter_miles=tk.Entry(root)
button_convert=tk.Button(root,text="convert",command=convert)
label_result=tk.Label(root,text="")

label_miles.grid(row=0,column=0,padx=10,pady=10)
enter_miles.grid(row=0,column=1,padx=10,pady=10)
button_convert.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
label_result.grid(row=2,column=0,columnspan=2)

root.mainloop()






