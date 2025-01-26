import tkinter as tk
from tkinter import ttk
import math
from ttkthemes import ThemedTk
import datetime

class ModernCalculator:
    def __init__(self):
        # Create main window
        self.root = ThemedTk(theme="arc")  # Using a lighter theme
        self.root.title("calculat⚡r")
        self.root.geometry("380x600")
        self.root.configure(bg='#f0f0f0')  # Light background
        
        # Color scheme - Pastel colors
        self.colors = {
            'bg': '#f0f0f0',           # Light background
            'display_bg': '#ffffff',    # White display
            'accent1': '#a5d8ff',       # Soft blue
            'accent2': '#ffd6e6',       # Soft pink
            'accent3': '#c3fae8',       # Soft mint
            'text': '#2b2b2b'          # Dark text
        }
        
        # Initialize variables
        self.current_calculation = tk.StringVar(value="0")
        self.expression = ""
        
        # Create UI
        self.create_ui()

    def create_ui(self):
        # Main frame with padding and rounded corners
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Display frame with white background and rounded corners
        display_frame = tk.Frame(
            main_frame, 
            bg=self.colors['display_bg'],
            relief='flat',
            bd=0
        )
        display_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Add some aesthetic padding
        tk.Frame(display_frame, height=10, bg=self.colors['display_bg']).pack()

        # Main display with custom font and styling
        self.display = tk.Entry(
            display_frame,
            textvariable=self.current_calculation,
            font=('Product Sans', 40, 'bold'),  # Modern font
            justify='right',
            bd=0,  # No border
            bg=self.colors['display_bg'],
            fg=self.colors['text'],
            insertbackground=self.colors['text']
        )
        self.display.pack(fill=tk.X, padx=20, pady=(0, 5))

        # Expression display
        self.expression_label = tk.Label(
            display_frame,
            text="",
            font=('Product Sans', 14),
            anchor='e',
            bg=self.colors['display_bg'],
            fg='#666666'
        )
        self.expression_label.pack(fill=tk.X, padx=20, pady=(0, 10))

        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        buttons_frame.pack(fill=tk.BOTH, expand=True)

        # Button layout
        buttons = [
            ('C', '⌫', '%', '÷'),
            ('7', '8', '9', '×'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('±', '0', '.', '=')
        ]

        # Create buttons with modern styling
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                # Choose button color based on type
                if text in ['÷', '×', '-', '+', '=']:
                    bg_color = self.colors['accent1']
                elif text in ['C', '⌫', '%']:
                    bg_color = self.colors['accent2']
                else:
                    bg_color = self.colors['accent3']

                # Create button with rounded corners and hover effect
                btn = tk.Button(
                    buttons_frame,
                    text=text,
                    font=('Product Sans', 18),
                    bg=bg_color,
                    fg=self.colors['text'],
                    relief='flat',
                    bd=0,
                    width=4,
                    height=2,
                    command=lambda t=text: self.button_click(t)
                )
                btn.grid(row=i, column=j, padx=5, pady=5, sticky='nsew')
                
                # Add hover effect
                btn.bind('<Enter>', lambda e, btn=btn, color=bg_color: self.on_hover(btn, color))
                btn.bind('<Leave>', lambda e, btn=btn, color=bg_color: self.on_leave(btn, color))

        # Configure grid weights
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)

        # Add date and time display with custom font
        self.time_label = tk.Label(
            main_frame,
            font=('Product Sans', 12),
            bg=self.colors['bg'],
            fg='#666666'
        )
        self.time_label.pack(side=tk.BOTTOM, pady=(10, 0))
        self.update_time()

    def on_hover(self, button, original_color):
        """Lighten button on hover"""
        button.configure(bg=self.lighten_color(original_color))

    def on_leave(self, button, original_color):
        """Restore original button color"""
        button.configure(bg=original_color)

    def lighten_color(self, color):
        """Make a color lighter"""
        # Convert color to RGB
        rgb = self.root.winfo_rgb(color)
        # Lighten each component
        lighter = tuple(min(65535, int(1.1 * c)) for c in rgb)
        # Convert back to hex
        return '#{:04x}{:04x}{:04x}'.format(*lighter)

    def update_time(self):
        """Update the time display"""
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=f"⌚ {current_time}")
        self.root.after(1000, self.update_time)

    def button_click(self, value):
        current = self.current_calculation.get()

        if value == 'C':
            self.current_calculation.set('0')
            self.expression = ""
            self.expression_label.config(text="")
        
        elif value == '⌫':
            self.current_calculation.set(current[:-1] if len(current) > 1 else '0')
        
        elif value == '=':
            try:
                expr = self.expression.replace('×', '*').replace('÷', '/')
                result = eval(expr)
                self.current_calculation.set(str(result))
                self.expression_label.config(text=self.expression + " =")
                self.expression = str(result)
            except:
                self.current_calculation.set("Error")
                self.expression = ""
        
        elif value == '±':
            try:
                num = float(current)
                self.current_calculation.set(str(-num))
                self.expression = str(-num)
            except:
                self.current_calculation.set("Error")
                self.expression = ""
        
        elif value == '%':
            try:
                result = float(current) / 100
                self.current_calculation.set(str(result))
                self.expression = str(result)
            except:
                self.current_calculation.set("Error")
                self.expression = ""
        
        else:
            if current == '0' or current == "Error":
                self.current_calculation.set(value)
                self.expression = value
            else:
                self.current_calculation.set(current + value)
                self.expression += value

    def run(self):
        # Center the window on the screen
        self.root.update()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        self.root.mainloop()

if __name__ == "__main__":
    calc = ModernCalculator()
    calc.run()
