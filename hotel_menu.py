import tkinter as tk
from tkinter import messagebox

# Menu items with prices
menu_items = {
    "Paneer Butter Masala": 150,
    "Veg Biryani": 120,
    "Chicken Curry": 180,
    "Butter Naan": 30,
    "Cold Drink": 40,
    "Gulab Jamun": 60
}

# Colors for UI
frame_colors = ['#FFB6C1', '#ADD8E6', '#90EE90', '#FFD700', '#FFA07A', "#9494B6"]

class HotelMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Menu - Colorful UI")  
        self.root.geometry("600x500")
        self.root.config(bg="#fff8f0")

        self.selected_items = {}

        title = tk.Label(root, text="🍽️ Welcome to Colorful Hotel Menu 🍽️", font=("Helvetica", 18, "bold"), bg="#fff8f0", fg="#333")
        title.pack(pady=15)

        self.menu_frame = tk.Frame(root, bg="#fff8f0")
        self.menu_frame.pack()

        for index, (item, price) in enumerate(menu_items.items()):
            self.add_menu_item(item, price, frame_colors[index % len(frame_colors)])

        btn_frame = tk.Frame(root, bg="#fff8f0")
        btn_frame.pack(pady=20)

        order_btn = tk.Button(btn_frame, text="Place Order", font=("Arial", 14), bg="#4CAF50", fg="white", command=self.show_order)
        order_btn.pack()

    def add_menu_item(self, item, price, color):
        frame = tk.Frame(self.menu_frame, bg=color, bd=2, relief="groove", padx=10, pady=10)
        frame.pack(padx=10, pady=5, fill="x")

        var = tk.IntVar()

        chk = tk.Checkbutton(frame, text=f"{item} - ₹{price}", font=("Arial", 14), bg=color, variable=var)
        chk.pack(side="left", anchor="w")

        qty_label = tk.Label(frame, text="Qty:", font=("Arial", 12), bg=color)
        qty_label.pack(side="left", padx=10)

        qty_entry = tk.Entry(frame, width=5)
        qty_entry.insert(0, "1")
        qty_entry.pack(side="left")

        self.selected_items[item] = (var, qty_entry, price)

    def show_order(self):
        total = 0
        order_details = ""

        for item, (var, qty_entry, price) in self.selected_items.items():
            if var.get():
                try:
                    qty = int(qty_entry.get())
                    amount = qty * price
                    total += amount
                    order_details += f"{item} x {qty} = ₹{amount}\n"
                except ValueError:
                    messagebox.showerror("Error", f"Invalid quantity for {item}")
                    return

        if not order_details:
            messagebox.showwarning("No Selection", "Please select at least one item.")
        else:
            order_details += f"\nTotal Amount: ₹{total}"
            messagebox.showinfo("Order Summary", order_details)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = HotelMenuApp(root)
    root.mainloop()
