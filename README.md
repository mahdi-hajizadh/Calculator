# 🧮 Calculator

A simple desktop calculator built with **Python** and **Tkinter**, developed progressively from a basic procedural implementation to an object-oriented calculator with additional mathematical operations and an improved graphical interface.

## ✨ Features

### Version 1.0

* Basic arithmetic operations
* Addition `+`
* Subtraction `-`
* Multiplication `×`
* Division `÷`
* Clear button
* Basic graphical interface
* Expression evaluation using Python

### Version 1.1 — OOP

Version 1.1 refactors the calculator using **Object-Oriented Programming**.

* `Calculator` class
* Encapsulated calculator logic
* Dynamic button creation
* Organized number and operator definitions
* Improved code structure
* Cleaner and more maintainable implementation

### Version 1.2

The latest version adds a more complete calculator interface and additional mathematical operations.

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* `%` Percentage
* `√` Square root
* `x²` Square
* `.` Decimal numbers
* `(` and `)` Parentheses
* `⌫` Backspace
* `C` Clear
* Improved dark interface
* Responsive grid layout
* Integer result formatting when possible
* Fixed-size calculator window

---

## 🖥️ Interface

Version 1.2 uses a dark-themed graphical interface with dedicated buttons for arithmetic and mathematical operations.

```text
┌──────────────────────────────┐
│                       123 + 5 │
├──────────────────────────────┤
│  C     ⌫      (       )       │
│  7     8      9       ÷       │
│  4     5      6       ×       │
│  1     2      3       -       │
│  0     .      %       +       │
│  √     x²     =               │
└──────────────────────────────┘
```

---

## 🛠️ Technologies

* **Python 3**
* **Tkinter**
* **math**
* Object-Oriented Programming (OOP)

No external Python packages are required.

---

## 📁 Project Structure

```text
Calculator/
│
├── claculator1.0.py
├── Calculator1.1(class).py
├── Calculator1.2.py
└── .gitignore
```

### Version history

| File                      | Description                                                    |
| ------------------------- | -------------------------------------------------------------- |
| `claculator1.0.py`        | Initial procedural calculator                                  |
| `Calculator1.1(class).py` | OOP refactoring                                                |
| `Calculator1.2.py`        | Extended calculator with additional operations and improved UI |

---

## 🚀 Run the Calculator

Install Python 3 with Tk support. Run `python -m tkinter` to check that Tk is available.

Clone the repository:

```bash
git clone https://github.com/mahdi-hajizadh/Calculator.git
cd Calculator
```

Run the latest version:

```bash
python Calculator1.2.py
```

To run the previous versions:

```bash
python "claculator1.0.py"
```

```bash
python "Calculator1.1(class).py"
```

---

## 🧠 What This Project Demonstrates

This project was developed as a learning progression in Python.

### 1. Procedural Programming

Version 1.0 focuses on basic Python functions, Tkinter widgets, callbacks, and event handling.

### 2. Object-Oriented Programming

Version 1.1 introduces a `Calculator` class and moves the application logic into methods and object state.

### 3. Code Organization

Version 1.2 further improves the structure by introducing reusable button creation through:

```python
create_button()
```

This reduces duplicated GUI code and makes the interface easier to maintain.

---

## Tests

Run `python -m unittest discover -s tests -v` from the repository root to test arithmetic evaluation without opening the GUI.

## Expression input

The calculator accepts decimal arithmetic, parentheses, and unary plus and minus. The parser evaluates these operations directly and rejects Python names and calls. Version 1.2 also provides square root, square, and percentage buttons.

## 🔮 Future Improvements

Possible improvements for future versions:

* [ ] Keyboard input support
* [ ] Calculation history
* [ ] Scientific calculator mode
* [ ] Memory functions (`M+`, `M-`, `MR`, `MC`)
* [ ] Better expression validation
* [ ] Light/Dark theme switching
* [ ] Windows `.exe` release
* [ ] Application icon
* [ ] More advanced mathematical functions

---

## 👨‍💻 Author

**Mahdi Hajizadh**

GitHub: [@mahdi-hajizadh](https://github.com/mahdi-hajizadh)

---

## 📄 License

This project is currently provided as a personal learning project.

