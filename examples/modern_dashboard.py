import cosui
from cosui.theme import Colors

# 1. App Setup
app = cosui.App(title="CosUI Dashboard", width=1000, height=700)

# --- SIDEBAR (Left) ---
# Dark strip on the left
# Color converted to Hex: (40, 40, 45) -> #28282D
sidebar_bg = cosui.Panel(x=0, y=0, w=250, h=700, color="#28282D")
app.add(sidebar_bg)

# Title in the Sidebar (Y coordinate adjusted for top-left origin)
logo = cosui.Label("COSUI", x=40, y=40, size=28, color=Colors.PRIMARY)
app.add(logo)

# Sidebar Buttons (Simulated Navigation)
def nav_click():
    print("Navigating...")

# Buttons stacked from top to bottom
btn1 = cosui.Button("Dashboard", x=25, y=120, w=200, on_click=nav_click)
btn2 = cosui.Button("Analytics", x=25, y=180, w=200, on_click=nav_click)
btn3 = cosui.Button("Settings", x=25, y=240, w=200, on_click=nav_click)

app.add(btn1)
app.add(btn2)
app.add(btn3)

# --- MAIN CONTENT (Right) ---

# Header Area
header_text = cosui.Label("Overview", x=290, y=40, size=24)
app.add(header_text)

# Statistics Card 1
# Color: (50, 50, 60) -> #32323C
card1 = cosui.Panel(x=290, y=100, w=300, h=150, color="#32323C")
app.add(card1)

# Labels relative to card position
# Color: (150,150,150) -> #969696
app.add(cosui.Label("Total Users", x=310, y=120, size=14, color="#969696"))
app.add(cosui.Label("12,450", x=310, y=160, size=32, color=Colors.PRIMARY))

# Statistics Card 2
card2 = cosui.Panel(x=620, y=100, w=300, h=150, color="#32323C")
app.add(card2)

app.add(cosui.Label("Revenue", x=640, y=120, size=14, color="#969696"))
# Color Green: (100, 255, 100) -> #64FF64
app.add(cosui.Label("$ 84,300", x=640, y=160, size=32, color="#64FF64"))

# New Feature: Input Field for Search
app.add(cosui.Label("Search User:", x=290, y=280, size=16))
search_input = cosui.Input(x=290, y=310, w=300, h=40)
app.add(search_input)

# Interactive Button in Content
def refresh_data():
    print(f"Refreshed! Searching for: {search_input.text}")

refresh_btn = cosui.Button("Refresh Data", x=290, y=380, w=150, on_click=refresh_data)
app.add(refresh_btn)

# Start App
if __name__ == "__main__":
    app.run()