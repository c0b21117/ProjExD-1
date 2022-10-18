import tkinter as tk

def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Left":
        cx -= 20
    elif key == "Right":
        cx += 20   
    canv.coords("tori",cx, cy)         
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canv = tk.Canvas(root,width = 1500,height = 900, bg= "black")
    canv.pack()

    tori = tk.PhotoImage(file="fig/6.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag = "tori") 

    key = "" #グローバル変数keyは、現在押されているキーを表す変数である #練習4

    root.bind("<KeyPress>",key_down) #練習5

    root.bind("<KeyRelease>", key_up) #練習6

    main_proc()
    root.mainloop()