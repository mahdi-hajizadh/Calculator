import tkinter as tk
import math


class Calculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")

        self.expression = tk.StringVar()

        self.style = {
            "width": 8,
            "height": 2,
            "font": ("Arial", 14, "bold"),
            "bg": "#2d2f33",
            "fg": "white",
            "activebackground": "#61afef",
            "activeforeground": "black",
            "relief": "flat",
            "bd": 0
        }

        self.create_widgets()

    def click(self, value):
        self.expression.set(self.expression.get() + value)

    def clear(self):
        self.expression.set("")

    def backspace(self):
        self.expression.set(self.expression.get()[:-1])

    def square(self):
        try:
            value = eval(self.expression.get())
            self.expression.set(str(value ** 2))
        except:
            self.expression.set("Error")

    def sqrt(self):
        try:
            value = eval(self.expression.get())
            if value < 0:
                self.expression.set("Error")
            else:
                self.expression.set(str(math.sqrt(value)))
        except:
            self.expression.set("Error")

    def percent(self):
        try:
            value = eval(self.expression.get())
            self.expression.set(str(value / 100))
        except:
            self.expression.set("Error")

    def calculate(self):
        try:
            result = eval(self.expression.get())
            # نمایش نتیجه به صورت عدد صحیح در صورت امکان
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression.set(str(result))
        except:
            self.expression.set("Error")

    def create_button(self, text, row, col, command=None, color=None, colspan=1):

        bg = self.style["bg"] if color is None else color

        btn = tk.Button(
            self.root,
            text=text,
            command=command,
            width=self.style["width"],
            height=self.style["height"],
            font=self.style["font"],
            bg=bg,
            fg=self.style["fg"],
            activebackground=self.style["activebackground"],
            activeforeground=self.style["activeforeground"],
            relief=self.style["relief"],
            bd=self.style["bd"]
        )

        btn.grid(row=row, column=col, columnspan=colspan, padx=3, pady=3, sticky="nsew")

    def create_widgets(self):
        # تنظیم وزن ستون‌ها برای انعطاف‌پذیری
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        
        # تنظیم وزن ردیف‌ها
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)

        # صفحه نمایش بزرگتر با پس‌زمینه تیره
        entry = tk.Entry(
            self.root,
            textvariable=self.expression,
            font=("Arial", 28, "bold"),
            justify="right",
            bg="#1e1e1e",
            fg="#61afef",
            bd=0,
            highlightthickness=0
        )

        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=(20, 10), sticky="nsew")
        
        # خط جداکننده
        separator = tk.Frame(self.root, height=2, bg="#3d3f43")
        separator.grid(row=1, column=0, columnspan=4, sticky="ew", padx=10, pady=5)

        # ردیف اول - دکمه‌های عملیاتی
        self.create_button("C", 2, 0, self.clear, "#c0392b")
        self.create_button("⌫", 2, 1, self.backspace, "#d35400")
        self.create_button("(", 2, 2, lambda: self.click("("), "#3d3f43")
        self.create_button(")", 2, 3, lambda: self.click(")"), "#3d3f43")

        # ردیف دوم - اعداد و تقسیم
        self.create_button("7", 3, 0, lambda: self.click("7"))
        self.create_button("8", 3, 1, lambda: self.click("8"))
        self.create_button("9", 3, 2, lambda: self.click("9"))
        self.create_button("÷", 3, 3, lambda: self.click("/"), "#e67e22")

        # ردیف سوم
        self.create_button("4", 4, 0, lambda: self.click("4"))
        self.create_button("5", 4, 1, lambda: self.click("5"))
        self.create_button("6", 4, 2, lambda: self.click("6"))
        self.create_button("×", 4, 3, lambda: self.click("*"), "#e67e22")

        # ردیف چهارم
        self.create_button("1", 5, 0, lambda: self.click("1"))
        self.create_button("2", 5, 1, lambda: self.click("2"))
        self.create_button("3", 5, 2, lambda: self.click("3"))
        self.create_button("-", 5, 3, lambda: self.click("-"), "#e67e22")

        # ردیف پنجم
        self.create_button("0", 6, 0, lambda: self.click("0"))
        self.create_button(".", 6, 1, lambda: self.click("."), "#3d3f43")
        self.create_button("%", 6, 2, self.percent, "#3d3f43")
        self.create_button("+", 6, 3, lambda: self.click("+"), "#e67e22")

        # ردیف ششم - دکمه‌های ریاضی و مساوی
        self.create_button("√", 7, 0, self.sqrt, "#2980b9")
        self.create_button("x²", 7, 1, self.square, "#2980b9")
        self.create_button("=", 7, 2, self.calculate, "#27ae60", 2)


root = tk.Tk()
Calculator(root)
root.mainloop()