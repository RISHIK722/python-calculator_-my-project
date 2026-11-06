import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Standard Calculator")
        self.root.geometry("320x450")
        self.root.resizable(False, False)
        
        self.expression = ""
        self.display_var = tk.StringVar()
        
        # Display Screen Frame
        display_frame = tk.Frame(self.root, bg="#222")
        display_frame.pack(expand=True, fill="both")
        
        self.display = tk.Entry(
            display_frame, 
            font=("Arial", 24), 
            textvariable=self.display_var, 
            justify="right", 
            bd=0, 
            bg="#222", 
            fg="white"
        )
        self.display.pack(expand=True, fill="both", padx=10, pady=20)
        
        # Keypad Frame
        btn_frame = tk.Frame(self.root, bg="#333")
        btn_frame.pack(expand=True, fill="both")
        
        buttons = [
            ('C', 1, 0), ('(', 1, 1), (')', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2)
        ]
        
        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(
                    btn_frame, text=text, font=("Arial", 18), 
                    bg="#654CAF", fg="white", bd=0,
                    command=self.evaluate
                )
                btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=1, pady=1)
            elif text == 'C':
                btn = tk.Button(
                    btn_frame, text=text, font=("Arial", 18), 
                    bg="#36f48b", fg="white", bd=0,
                    command=self.clear
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)
            else:
                btn = tk.Button(
                    btn_frame, text=text, font=("Arial", 18), 
                    bg="#444", fg="white", bd=0,
                    command=lambda t=text: self.click(t)
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)
                
        # Configure grid weights for responsive scaling
        for i in range(6):
            btn_frame.rowconfigure(i, weight=1)
        for i in range(4):
            btn_frame.columnconfigure(i, weight=1)
            
    def click(self, item):
        self.expression += str(item)
        self.display_var.set(self.expression)
        
    def clear(self):
        self.expression = ""
        self.display_var.set("")
        
    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.expression = result
        except Exception:
            self.display_var.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
