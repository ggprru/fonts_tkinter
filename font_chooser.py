import tkinter
import tkinter.font as tkf

window = tkinter.Tk()
window.geometry('1920x1000+0+0')

def press(font):
    global bb
    bb['font']=(font,35)

sr='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
sr_en='abcdefghijklmnoprstuvwxyz'

bb = tkinter.Button(window, text = f'\'RU\' Образец {sr} \n {sr.upper()} \n \'EN\' Example {sr_en} \n {sr_en.upper()}', font=('Arial',35) )
bb.place(relx=0.5, y=850, anchor='center')

fonts = tkf.families()
a=[]
a_btns = []
fonts_per_column = 35
font_size = 12
width_column = 200
font_text_height = 20

for i in range(len(fonts)):
    a.append([])

for i, v in enumerate(fonts):
    xx = i//fonts_per_column
    a[xx].append(v)

for x in range(len(a)):
    a_btns.append([])
    for j,y in enumerate(a[x]): 
        b = tkinter.Button(window, text = y, font = (y, font_size))
        b.place(x=x*width_column, y=j*font_text_height, width=width_column, height=font_text_height)
        a_btns[x].append(b)
        a_btns[x][j]['command']= lambda btn_font=a_btns[x][j]['text'] : press(btn_font)

window.mainloop()