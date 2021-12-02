import tkinter as tk

window = tk.Tk()
window.title('挖ㄟwindow')
window.geometry('400x200')

def insert_point():
    var=e.get()
    t.insert('insert',var)
def insert_end():
    var = e.get()
    t.insert('end', var)


e=tk.Entry(window)
e.pack() 

b1 = tk.Button(window,text='insert point',command=insert_point,bg='yellow',bd=8)
b1.pack()
b2 = tk.Button(window,text='insert end',command=insert_end,bg='pink')
b2.pack()

t = tk.Text(window,height=2)
t.pack()

window.mainloop()  #沒有這行視窗就不會跳出來