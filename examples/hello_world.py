import cosui

def on_button_click():
    print("Welcome to the future of GUI!")

# Initialize the App
app = cosui.App(title="CosUI Demo", width=800, height=600)

# Create a modern button with hover effects included
# Y=275 is roughly center in a 600px window (works for both coord systems essentially)
btn = cosui.Button(
    text="Click Me", 
    x=350, 
    y=275, 
    on_click=on_button_click
)

# Add widgets to the app
app.add(btn)

# Run the render loop
app.run()