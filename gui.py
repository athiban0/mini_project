import tkinter as tk
from tkinter import Text, messagebox
from syntax_checker import SyntaxChecker
from themes import ThemeManager

class SyntaxSlayerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Syntax Slayer")
        self.syntax_checker = SyntaxChecker()
        self.theme_manager = ThemeManager()
        self.current_theme = self.theme_manager.get_theme('anime')

        # GUI Components
        self.text_area = Text(self.root, bg=self.current_theme['bg'], fg=self.current_theme['fg'])
        self.text_area.pack(expand=True, fill='both')

        self.check_button = tk.Button(self.root, text="Check Syntax", command=self.check_code)
        self.check_button.pack()

    def run(self):
        self.root.mainloop()

    def check_code(self):
        code = self.text_area.get("1.0", tk.END)
        errors = self.syntax_checker.check_syntax(code)
        
        if errors:
            self.show_errors(errors)
        else:
            messagebox.showinfo("Syntax Slayer", "No syntax errors detected! Great job!")

    def show_errors(self, errors):
        error_message = "\n".join([f"Line {line}: {msg}" for line, msg in errors])
        messagebox.showerror("Syntax Errors Found", error_message)
