import tkinter as tk

from arithmetic import calculate_expression


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x400")

        self.my_str = tk.StringVar()

        self.btn_style = {
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

        self.create_widgets()

    def clean(self):
        self.my_str.set("")

    def click(self, value):
        current = self.my_str.get()
        self.my_str.set(current + value)

    def calculate(self):
        try:
            result = calculate_expression(self.my_str.get())
            self.my_str.set(str(result))
        except (ArithmeticError, ValueError, SyntaxError):
            self.my_str.set("Warning!")

    def create_widgets(self):

        # Display
        entry = tk.Entry(
            self.root,
            width=20,
            font=("Arial", 26),
            justify="right",
            textvariable=self.my_str
        )
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

        # Number buttons
        numbers = [
            ("1", 1, 0), ("2", 1, 1), ("3", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2),
            ("0", 4, 1)
        ]

        for text, row, col in numbers:
            tk.Button(
                self.root,
                text=text,
                command=lambda t=text: self.click(t),
                **self.btn_style
            ).grid(row=row, column=col)

        # Operator buttons
        operators = [
            ("+", "+", 1, 3),
            ("-", "-", 2, 3),
            ("×", "*", 3, 3),
            ("÷", "/", 4, 3)
        ]

        for text, value, row, col in operators:
            tk.Button(
                self.root,
                text=text,
                command=lambda v=value: self.click(v),
                **self.btn_style
            ).grid(row=row, column=col)

        # Clear button
        tk.Button(
            self.root,
            text="C",
            command=self.clean,
            width=6,
            height=2,
            font=("Arial", 16),
            bg="#c0392b",
            fg="white",
            activebackground="#e74c3c",
            activeforeground="black"
        ).grid(row=4, column=0)

        # Equals button
        tk.Button(
            self.root,
            text="=",
            command=self.calculate,
            width=6,
            height=2,
            font=("Arial", 16),
            bg="#27ae60",
            fg="white",
            activebackground="#2ecc71",
            activeforeground="black"
        ).grid(row=4, column=2)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()