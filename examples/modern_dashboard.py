import cosui
from cosui.theme import Colors

# 1. App Setup
app = cosui.App(title="CosUI Dashboard", width=1000, height=700)

# --- SIDEBAR (Links) ---
# Ein dunkler Streifen links
sidebar_bg = cosui.Panel(x=0, y=0, w=250, h=700, color=(40, 40, 45))
app.add(sidebar_bg)

# Titel in der Sidebar
logo = cosui.Label("COSUI", x=40, y=640, size=28, color=Colors.PRIMARY)
app.add(logo)

# Sidebar Buttons (Simulation einer Navigation)
def nav_click():
    print("Navigiere...")

btn1 = cosui.Button("Dashboard", x=25, y=550, w=200, on_click=nav_click)
btn2 = cosui.Button("Analytics", x=25, y=490, w=200, on_click=nav_click)
btn3 = cosui.Button("Settings", x=25, y=430, w=200, on_click=nav_click)

app.add(btn1)
app.add(btn2)
app.add(btn3)

# --- MAIN CONTENT (Rechts) ---

# Header Bereich
header_text = cosui.Label("Overview", x=290, y=640, size=24)
app.add(header_text)

# Eine "Statistik Karte" 1
card1 = cosui.Panel(x=290, y=450, w=300, h=150, color=(50, 50, 60))
app.add(card1)
app.add(cosui.Label("Total Users", x=310, y=550, size=14, color=(150,150,150)))
app.add(cosui.Label("12,450", x=310, y=500, size=32, color=Colors.PRIMARY))

# Eine "Statistik Karte" 2
card2 = cosui.Panel(x=620, y=450, w=300, h=150, color=(50, 50, 60))
app.add(card2)
app.add(cosui.Label("Revenue", x=640, y=550, size=14, color=(150,150,150)))
app.add(cosui.Label("$ 84,300", x=640, y=500, size=32, color=(100, 255, 100))) # Grün

# Interaktiver Button im Content
def refresh_data():
    print("Daten werden aktualisiert...")

refresh_btn = cosui.Button("Refresh Data", x=290, y=380, w=150, on_click=refresh_data)
app.add(refresh_btn)

# App starten
if __name__ == "__main__":
    app.run()
