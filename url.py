import tkinter as tk
import pyshorteners

def shorten_url():
    original_url = entry.get()
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(original_url)

    # Create a new window to display the shortened URL
    new_window = tk.Toplevel(app)
    new_window.title("Shortened URL")

    # Label to display the shortened URL
    result_label = tk.Label(new_window, text=f"Shortened URL: {shortened_url}", fg="blue")
    result_label.pack(padx=20, pady=20)

# Create the main application window
app = tk.Tk()
app.title("URL Shortener")

# Input field for URL
entry = tk.Entry(app, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

# Button to trigger URL shortening
shorten_button = tk.Button(app, text="Shorten", command=shorten_url)
shorten_button.grid(row=0, column=1, padx=10, pady=10)

# Run the application
app.mainloop()
