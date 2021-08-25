# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk

window = tk.Tk()
window.title('嘿嘿')
window.geometry('200x100')

var=tk.StringVar()

l=tk.Label(window,textvariable=var,bg='red',font=('Arial,12'),width=20,height=2)
l.pack()    #在windoe上安置這個l,也可以用.place(),但就需要給具體位置,pack則不用


on_hit = True

def hit_me():
    global on_hit
    if on_hit == True:
        on_hit = False
        var.set('我又跳出來啦!')
    else:
        var.set('我又站回去啦!打我呀笨蛋')
        on_hit = True


b=tk.Button(window,text='打我呀',width=15,height=2,command=hit_me)

b.pack()
window.mainloop()  #使循環