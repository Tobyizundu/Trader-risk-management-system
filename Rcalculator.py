import tkinter as tk
from tkinter import ttk, messagebox

class RiskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Risk Analysis Tool")
        self.root.geometry("600x500")
        self.root.configure(bg='#2c3e50')
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#2c3e50')
        self.style.configure('TLabel', background='#2c3e50', foreground='white', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10), padding=5)
        self.style.configure('Header.TLabel', font=('Arial', 14, 'bold'), foreground='#3498db')
        
        self.create_main_menu()
    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def create_main_menu(self):
        self.clear_frame()
        
        header = ttk.Label(self.root, text="Professional Risk Analysis Tool", style='Header.TLabel')
        header.pack(pady=20)
        
        desc = ttk.Label(self.root, text="Optimize your trading performance with professional risk management", 
                        font=('Arial', 11))
        desc.pack(pady=10)
        
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=30)
        
        buttons = [
            ("Calculate Trade Risk", self.view_risk_gui),
            ("Calculate Profit/Loss in R", self.calculate_R_gui),
            ("Pip/Lot Calculator", self.calculate_pip_gui)
        ]
        
        for text, command in buttons:
            btn = ttk.Button(button_frame, text=text, command=command, width=25)
            btn.pack(pady=10)
        
        exit_btn = ttk.Button(self.root, text="Exit", command=self.root.quit)
        exit_btn.pack(pady=20)
    
    def view_risk_gui(self):
        self.clear_frame()
        
        back_btn = ttk.Button(self.root, text="← Back to Menu", command=self.create_main_menu)
        back_btn.pack(anchor='nw', padx=10, pady=10)
        
        header = ttk.Label(self.root, text="Trade Risk Calculator", style='Header.TLabel')
        header.pack(pady=20)
        
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=20)
        
        ttk.Label(input_frame, text="Account Size:").grid(row=0, column=0, padx=5, pady=10, sticky='e')
        self.acc_var = tk.StringVar()
        acc_entry = ttk.Entry(input_frame, textvariable=self.acc_var, width=15)
        acc_entry.grid(row=0, column=1, padx=5, pady=10)
        ttk.Label(input_frame, text="USD").grid(row=0, column=2, padx=5, pady=10, sticky='w')
        
        ttk.Label(input_frame, text="Risk Percentage:").grid(row=1, column=0, padx=5, pady=10, sticky='e')
        self.risk_var = tk.StringVar(value="1%")
        risk_combo = ttk.Combobox(input_frame, textvariable=self.risk_var, 
                                 values=["0.5%", "1%", "1.5%", "2%"], state="readonly", width=12)
        risk_combo.grid(row=1, column=1, padx=5, pady=10)
        
        calc_btn = ttk.Button(input_frame, text="Calculate Risk", command=self.calculate_risk)
        calc_btn.grid(row=2, column=0, columnspan=3, pady=20)
        
        self.results_frame = ttk.Frame(self.root)
        self.results_frame.pack(pady=20)
    
    def calculate_risk(self):
        try:
            account_size = float(self.acc_var.get())
            risk_percent = float(self.risk_var.get().strip('%'))
            
            risk_amount = account_size * (risk_percent / 100)
            target_gain = risk_amount * 3
            
            for widget in self.results_frame.winfo_children():
                widget.destroy()
            
            ttk.Label(self.results_frame, text="Risk Analysis Results:", 
                     font=('Arial', 12, 'bold')).pack(pady=10)
            
            ttk.Label(self.results_frame, 
                     text=f"Maximum Risk Amount: ${risk_amount:,.2f}").pack(pady=5)
            ttk.Label(self.results_frame, 
                     text=f"Target Gain (1:3 R:R): ${target_gain:,.2f}").pack(pady=5)
            ttk.Label(self.results_frame, 
                     text=f"Risk Percentage: {risk_percent}% of ${account_size:,.2f}").pack(pady=5)
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers")
    
    def calculate_R_gui(self):
        self.clear_frame()
        
        back_btn = ttk.Button(self.root, text="← Back to Menu", command=self.create_main_menu)
        back_btn.pack(anchor='nw', padx=10, pady=10)
        
        header = ttk.Label(self.root, text="Profit/Loss R Calculator", style='Header.TLabel')
        header.pack(pady=20)
        
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=20)
        
        ttk.Label(input_frame, text="Account Size:").grid(row=0, column=0, padx=5, pady=10, sticky='e')
        self.acc_r_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.acc_r_var, width=15).grid(row=0, column=1, padx=5, pady=10)
        ttk.Label(input_frame, text="USD").grid(row=0, column=2, padx=5, pady=10, sticky='w')
        
        ttk.Label(input_frame, text="Trade Result:").grid(row=1, column=0, padx=5, pady=10, sticky='e')
        self.pl_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.pl_var, width=15).grid(row=1, column=1, padx=5, pady=10)
        ttk.Label(input_frame, text="USD").grid(row=1, column=2, padx=5, pady=10, sticky='w')
        
        ttk.Label(input_frame, text="Result Type:").grid(row=2, column=0, padx=5, pady=10, sticky='e')
        self.result_type = tk.StringVar(value="Profit")
        ttk.Radiobutton(input_frame, text="Profit", variable=self.result_type, value="Profit").grid(row=2, column=1, sticky='w')
        ttk.Radiobutton(input_frame, text="Loss", variable=self.result_type, value="Loss").grid(row=2, column=2, sticky='w')
        
        ttk.Button(input_frame, text="Calculate R Multiple", 
                  command=self.calculate_r_multiple).grid(row=3, column=0, columnspan=3, pady=20)
        
        self.r_results_frame = ttk.Frame(self.root)
        self.r_results_frame.pack(pady=20)
    
    def calculate_r_multiple(self):
        try:
            account_size = float(self.acc_r_var.get())
            pl_amount = float(self.pl_var.get())
            result_type = self.result_type.get()
            
            one_r = account_size * 0.01
            r_multiple = pl_amount / one_r
            
            for widget in self.r_results_frame.winfo_children():
                widget.destroy()
            
            color = "green" if result_type == "Profit" else "red"
            result_text = f"Trade Result: {r_multiple:.2f}R"
            
            result_label = ttk.Label(self.r_results_frame, text=result_text, 
                                   font=('Arial', 12, 'bold'), foreground=color)
            result_label.pack(pady=10)
            
            ttk.Label(self.r_results_frame, 
                     text=f"1R (1% of account) = ${one_r:,.2f}").pack(pady=5)
            ttk.Label(self.r_results_frame, 
                     text=f"Trade Amount = ${pl_amount:,.2f}").pack(pady=5)
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers")
    
    def calculate_pip_gui(self):
        self.clear_frame()
        
        back_btn = ttk.Button(self.root, text="← Back to Menu", command=self.create_main_menu)
        back_btn.pack(anchor='nw', padx=10, pady=10)
        
        header = ttk.Label(self.root, text="Pip/Lot Calculator", style='Header.TLabel')
        header.pack(pady=20)
        
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=20)
        
        fields = [
            ("Account Size (USD):", "pip_acc_var"),
            ("Stop Loss Pips:", "pip_sl_var"),
            ("Take Profit Pips:", "pip_tp_var"),
            ("Lot Size:", "lot_size_var")
        ]
        
        for i, (label, var_name) in enumerate(fields):
            ttk.Label(input_frame, text=label).grid(row=i, column=0, padx=5, pady=8, sticky='e')
            setattr(self, var_name, tk.StringVar())
            ttk.Entry(input_frame, textvariable=getattr(self, var_name), width=15).grid(row=i, column=1, padx=5, pady=8)
        
        ttk.Button(input_frame, text="Calculate Risk/Reward", 
                  command=self.calculate_pip_risk).grid(row=4, column=0, columnspan=2, pady=20)
        
        self.pip_results_frame = ttk.Frame(self.root)
        self.pip_results_frame.pack(pady=20)
    
    def calculate_pip_risk(self):
        try:
            account = float(self.pip_acc_var.get())
            pip_sl = float(self.pip_sl_var.get())
            pip_tp = float(self.pip_tp_var.get())
            lot_size = float(self.lot_size_var.get())
            
            risk_exposure = (lot_size * 100) * (pip_sl / 10)
            reward_potential = (lot_size * 100) * (pip_tp / 10)
            
            one_r = account * 0.01
            risk_r = risk_exposure / one_r
            reward_r = reward_potential / one_r
            
            for widget in self.pip_results_frame.winfo_children():
                widget.destroy()
            
            ttk.Label(self.pip_results_frame, text="Position Analysis:", 
                     font=('Arial', 12, 'bold')).pack(pady=10)
            
            ttk.Label(self.pip_results_frame, 
                     text=f"Risk Exposure: ${risk_exposure:,.2f} ({risk_r:.2f}R)").pack(pady=3)
            ttk.Label(self.pip_results_frame, 
                     text=f"Reward Potential: ${reward_potential:,.2f} ({reward_r:.2f}R)").pack(pady=3)
            ttk.Label(self.pip_results_frame, 
                     text=f"Risk-Reward Ratio: 1:{reward_potential/risk_exposure:.2f}").pack(pady=3)
            
            if risk_r > 2:
                ttk.Label(self.pip_results_frame, text="!!!! HIGH RISK: Exceeding 2R per trade!", 
                         foreground='red', font=('Arial', 10, 'bold')).pack(pady=10)
            elif risk_r > 1:
                ttk.Label(self.pip_results_frame, text=" !!Moderate Risk: Consider reducing position size", 
                         foreground='orange').pack(pady=5)
            else:
                ttk.Label(self.pip_results_frame, text="✓ Risk within acceptable range", 
                         foreground='green').pack(pady=5)
                
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers in all fields")

if __name__ == "__main__":
    root = tk.Tk()
    app = RiskManagerGUI(root)
    root.mainloop()