import tkinter as tk

win = tk.Tk()
win.title("Calculator")
win.geometry("400x400")

my_str = tk.StringVar()
my_str.set("")

def clean():
    my_str.set("")

def click(meghdar):
    current = my_str.get()
    my_str.set(current + meghdar)

def calculate():
    try:
        result = eval(my_str.get())
        my_str.set(str(result))
    except:
        my_str.set("Warning!")

# صفحه نمایش
bu_la = tk.Entry(win, width=20, font=("Arial", 26), justify="right", textvariable=my_str)
bu_la.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# دیکشنری برای تنظیمات دکمه‌ها
btn_style = {
    "width": 6,
    "height": 2,
    "font": ("Arial", 16),
    "bg": "#2d2f33",
    "fg": "white",
    "activebackground": "#61afef",
    "activeforeground": "black",
    "padx": 5,
    "pady": 5
}

# دکمه‌های اعداد
bu1 = tk.Button(text="1", command=lambda: click("1"), **btn_style)
bu1.grid(row=1, column=0)

bu2 = tk.Button(text="2", command=lambda: click("2"), **btn_style)
bu2.grid(row=1, column=1)

bu3 = tk.Button(text="3", command=lambda: click("3"), **btn_style)
bu3.grid(row=1, column=2)

bu4 = tk.Button(text="4", command=lambda: click("4"), **btn_style)
bu4.grid(row=2, column=0)

bu5 = tk.Button(text="5", command=lambda: click("5"), **btn_style)
bu5.grid(row=2, column=1)

bu6 = tk.Button(text="6", command=lambda: click("6"), **btn_style)
bu6.grid(row=2, column=2)

bu7 = tk.Button(text="7", command=lambda: click("7"), **btn_style)
bu7.grid(row=3, column=0)

bu8 = tk.Button(text="8", command=lambda: click("8"), **btn_style)
bu8.grid(row=3, column=1)

bu9 = tk.Button(text="9", command=lambda: click("9"), **btn_style)
bu9.grid(row=3, column=2)

bu0 = tk.Button(text="0", command=lambda: click("0"), **btn_style)
bu0.grid(row=4, column=1)

# دکمه +
bu_sum = tk.Button(text="+", command=lambda: click("+"), **btn_style)
bu_sum.grid(row=1, column=3)
# دکمه -
bu_min = tk.Button(text="-", command=lambda: click("-"), **btn_style)
bu_min.grid(row=2, column=3)
# دکمه *
bu_multy = tk.Button(text="x", command=lambda: click("*"), **btn_style)
bu_multy.grid(row=3, column=3)
# دکمه /
bu_div = tk.Button(text="÷", command=lambda: click("/"), **btn_style)
bu_div.grid(row=4, column=3)

# دکمه C با رنگ ویژه
bu_clear = tk.Button(text="C", command=clean,
                     width=6, height=2, font=("Arial", 16),
                     bg="#c0392b", fg="white",
                     activebackground="#e74c3c", activeforeground="black",
                     padx=5, pady=5)
bu_clear.grid(row=4, column=0)

# دکمه = با رنگ ویژه
bu_is = tk.Button(text="=", command=calculate,
                  width=6, height=2, font=("Arial", 16),
                  bg="#27ae60", fg="white",
                  activebackground="#2ecc71", activeforeground="black",
                  padx=5, pady=5)
bu_is.grid(row=4, column=2)

win.mainloop()
