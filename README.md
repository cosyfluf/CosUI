# CosUI 🚀

> **The Next-Generation GUI Framework for Python.**  
> Modern, lightweight, and pixel-perfect by default.

![Version](https://img.shields.io/pypi/v/cosui)
![License](https://img.shields.io/pypi/l/cosui)
![Python](https://img.shields.io/pypi/pyversions/cosui)

**CosUI** is designed to solve the biggest problem in the Python ecosystem: building user interfaces that don't look like they belong in Windows 95. Unlike Tkinter, CosUI uses a custom rendering engine (powered by Pygame) to draw modern, rounded, and anti-aliased widgets out of the box.

---

## ✨ Why CosUI?

- **🎨 Modern by Default:** Buttons and inputs come with rounded corners (`border-radius`) and hover effects instantly. No CSS required.
- **🌈 Hex Color Support:** Style your app using standard Hex codes (e.g., `#FF00FF`) just like in web development.
- **⚡ Fast & Responsive:** Built on a highly optimized rendering loop for smooth 60fps performance.
- **🐍 Pythonic API:** Simple, Object-Oriented design. If you know Python, you know CosUI.
- **📦 Zero Bloat:** No heavy Qt/GTK dependencies. Just pure Python and lightweight rendering.

---

## 📥 Installation

Get started in seconds:

```bash
pip install cosui
```
---

## 🛠️ How to Use

Here is a simple example showing how to create an app with a Button, a Label with custom colors, and an Input field.

```python
from cosui import App, Button, Label, Input

# 1. Define your actions
def on_submit():
    print("Button clicked!")

# 2. Initialize the App
app = App(title="My Modern App", width=800, height=600)

# 3. Add Widgets
# Labels support Hex colors
app.add(Label("Welcome to CosUI", x=50, y=50, size=24, color="#3C8CFF"))

# Inputs are interactive and rounded by default
app.add(Input(x=50, y=100, w=250, h=40))

# Buttons have built-in hover effects
app.add(Button(
    text="Submit", 
    x=50, 
    y=160, 
    w=120, 
    on_click=on_submit
))

# 4. Run the App
app.run()
```
## 🧩 Included Widgets

- * Button: Clickable, rounded, with hover states.

- * Input: Text entry field with focus handling.

- * Panel: Colored rectangles for backgrounds and cards.

- * Label: Text rendering with custom sizes and colors.

---

Built with ❤️ by cosyfluf