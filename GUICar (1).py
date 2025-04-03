import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

class Car:
    def __init__(self, car_id, make, model, year, price, color, car_type, count=1):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.color = color
        self.car_type = car_type
        self.count = count

    def __str__(self):
        return f"[{self.car_id}] {self.year} {self.make} {self.model} - ₹{self.price} ({self.color}, {self.car_type}) [Count: {self.count}]"

class Showroom:
    def __init__(self):
        self.inventory = []
        self.total_sales = 0.0
        self.total_commission = 0.0
        self.car_id_counter = 1

    def add_car(self, car):
        existing_cars = [c for c in self.inventory if (
            c.make == car.make and
            c.model == car.model and
            c.year == car.year and
            c.color == car.color and
            c.car_type == car.car_type
        )]

        if existing_cars:
            last_car = existing_cars[0]
            last_car.count += car.count
            car.car_id = f"{last_car.car_id[:-2]}_{last_car.count}"
        else:
            car.car_id = f"{self.car_id_counter}_1"
            self.inventory.append(car)
            self.car_id_counter += 1

    def view_inventory(self):
        return "\n".join(str(car) for car in self.inventory)

    def filter_inventory(self, criterion, value):
        filtered_cars = []
        if criterion == 'make':
            filtered_cars = [car for car in self.inventory if car.make.lower() == value.lower()]
        elif criterion == 'model':
            filtered_cars = [car for car in self.inventory if car.model.lower() == value.lower()]
        elif criterion == 'color':
            filtered_cars = [car for car in self.inventory if car.color.lower() == value.lower()]
        elif criterion == 'car_type':
            filtered_cars = [car for car in self.inventory if car.car_type.lower() == value.lower()]
        elif criterion == 'max_price':
            try:
                max_price = float(value)
                filtered_cars = [car for car in self.inventory if car.price <= max_price]
            except ValueError:
                return "Invalid price format."

        return "\n".join(str(car) for car in filtered_cars) if filtered_cars else "No cars found."

    def sell_car(self, car_id):
        car_to_sell = next((car for car in self.inventory if car.car_id == car_id), None)
        if car_to_sell:
            commission = self.calculate_commission(car_to_sell.price)
            if car_to_sell.count > 1:
                car_to_sell.count -= 1
                self.total_sales += car_to_sell.price
                self.total_commission += commission
                return f"Sold one unit of: {car_to_sell}. Commission earned: ₹{commission:.2f}"
            else:
                self.inventory.remove(car_to_sell)
                self.total_sales += car_to_sell.price
                self.total_commission += commission
                return f"Sold: {car_to_sell}. Commission earned: ₹{commission:.2f}"
        else:
            return "Car ID not found."

    def calculate_commission(self, price):
        if price < 500000:
            return price * 0.05
        elif price < 1500000:
            return price * 0.07
        else:
            return price * 0.10

class ShowroomApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Showroom Management System")
        self.root.configure(bg="#f0f0f0")

        self.showroom = Showroom()

        self.create_widgets()
        self.populate_sample_data()

    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(pady=10)

        self.inventory_text = ScrolledText(main_frame, height=15, width=80, bg="#ffffff", font=("Arial", 12))
        self.inventory_text.grid(row=0, column=0, columnspan=4, padx=10)

        btn_frame = tk.Frame(main_frame, bg="#f0f0f0")
        btn_frame.grid(row=1, column=0, pady=10)

        buttons_info = [
            ("View Inventory", self.view_inventory, "#4CAF50"),
            ("Filter Inventory", self.filter_inventory, "#2196F3"),
            ("Sell Car by ID", self.sell_car, "#FF5722"),
            ("Add Car", self.add_car, "#FFEB3B"),
            ("View Financials", self.view_financials, "#9C27B0"),
        ]

        for i, (text, command, color) in enumerate(buttons_info):
            btn = tk.Button(btn_frame, text=text, command=command, bg=color, fg="white", font=("Arial", 12))
            btn.grid(row=0, column=i, padx=5)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#e0e0e0"))
            btn.bind("<Leave>", lambda e, b=btn, c=color: b.config(bg=c))

    def populate_sample_data(self):
        sample_cars_data = [
            ("Maruti Suzuki", "Swift", 2023, 600000, "Blue", "Hatchback"),
            ("Hyundai", "Creta", 2023, 1500000, "Red", "SUV"),
            ("Tata", "Nexon", 2023, 800000, "Black", "SUV"),
            ("Honda", "City", 2022, 1200000, "White", "Sedan"),
            ("Kia", "Seltos", 2022, 1300000, "Gray", "SUV"),
            ("Toyota", "Innova Crysta", 2023, 2500000, "Silver", "MPV"),
            ("Mahindra", "Thar", 2023, 1500000, "Green", "SUV"),
            ("Nissan", "Magnite", 2022, 550000, "Yellow", "Hatchback"),
            ("Volkswagen", "Polo", 2022, 900000, "Blue", "Hatchback"),
            ("Renault", "Kiger", 2023, 600000, "Red", "Hatchback"),
            ("Skoda", "Kushaq", 2023, 1200000, "Brown", "SUV"),
            ("MG", "Hector", 2022, 2000000, "White", "SUV"),
            ("Hyundai", "i20", 2023, 750000, "Black", "Hatchback"),
            ("Ford", "EcoSport", 2022, 950000, "Orange", "SUV"),
            ("Tata", "Altroz", 2022, 700000, "Silver", "Hatchback"),
            ("Honda", "WR-V", 2023, 950000, "Navy Blue", "Crossover"),
            ("Kia", "Sonet", 2023, 800000, "Turquoise", "SUV"),
            ("Maruti Suzuki", "Baleno", 2023, 700000, "Red", "Hatchback"),
            ("Toyota", "Fortuner", 2023, 3500000, "Black", "SUV"),
            ("Tata", "Harrier", 2023, 1500000, "Blue", "SUV"),
            ("Mahindra", "XUV700", 2023, 2000000, "White", "SUV"),
            ("Nissan", "Kicks", 2022, 1200000, "Grey", "SUV"),
            ("Honda", "Jazz", 2022, 800000, "Silver", "Hatchback"),
        ]

        for make, model, year, price, color, car_type in sample_cars_data:
            car = Car(None, make, model, year, price, color, car_type, count=1)
            self.showroom.add_car(car)

    def view_inventory(self):
        inventory = self.showroom.view_inventory()
        self.inventory_text.delete(1.0, tk.END)
        self.inventory_text.insert(tk.END, inventory or "No cars in inventory.")

    def filter_inventory(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Filter Inventory")
        dialog.attributes('-topmost', True)
        self.center_dialog(dialog)

        criterion_label = tk.Label(dialog, text="Filter by (make, model, color, car_type, max_price):")
        criterion_label.pack(pady=5)

        criterion_entry = tk.Entry(dialog)
        criterion_entry.pack(pady=5)

        value_label = tk.Label(dialog, text="Enter value:")
        value_label.pack(pady=5)

        value_entry = tk.Entry(dialog)
        value_entry.pack(pady=5)

        def apply_filter():
            criterion = criterion_entry.get()
            value = value_entry.get()
            filtered_inventory = self.showroom.filter_inventory(criterion, value)
            self.inventory_text.delete(1.0, tk.END)
            self.inventory_text.insert(tk.END, filtered_inventory)
            dialog.destroy()

        filter_btn = tk.Button(dialog, text="Filter", command=apply_filter)
        filter_btn.pack(pady=10)

    def sell_car(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Sell Car")
        dialog.attributes('-topmost', True)
        self.center_dialog(dialog)

        car_id_label = tk.Label(dialog, text="Enter the car ID to sell:")
        car_id_label.pack(pady=5)

        car_id_entry = tk.Entry(dialog)
        car_id_entry.pack(pady=5)

        def sell():
            car_id = car_id_entry.get()
            if car_id:
                message = self.showroom.sell_car(car_id)
                messagebox.showinfo("Sell Car", message)
                dialog.destroy()
                self.view_inventory()

        sell_btn = tk.Button(dialog, text="Sell", command=sell)
        sell_btn.pack(pady=10)

    def add_car(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Car")
        dialog.attributes('-topmost', True)
        self.center_dialog(dialog)

        # Option selection
        option_label = tk.Label(dialog, text="Choose an option to add a car:")
        option_label.pack(pady=10)

        add_existing_btn = tk.Button(dialog, text="Add Existing Car by Main ID", command=lambda: self.add_existing_car(dialog))
        add_existing_btn.pack(pady=5)

        add_new_btn = tk.Button(dialog, text="Add New Car", command=lambda: self.add_new_car(dialog))
        add_new_btn.pack(pady=5)

    def add_existing_car(self, parent_dialog):
        parent_dialog.destroy()  # Close the main dialog

        dialog = tk.Toplevel(self.root)
        dialog.title("Add Existing Car")
        dialog.attributes('-topmost', True)
        self.center_dialog(dialog)

        main_id_label = tk.Label(dialog, text="Enter Main ID of the car:")
        main_id_label.pack(pady=5)

        main_id_entry = tk.Entry(dialog)
        main_id_entry.pack(pady=5)

        quantity_label = tk.Label(dialog, text="Enter quantity to add:")
        quantity_label.pack(pady=5)

        quantity_entry = tk.Entry(dialog)
        quantity_entry.pack(pady=5)

        def add_existing():
            main_id = main_id_entry.get()
            try:
                quantity = int(quantity_entry.get())
                if quantity <= 0:
                    raise ValueError

                # Find the car with the specified main_id
                car = next((c for c in self.showroom.inventory if c.car_id.startswith(main_id)), None)
                if car:
                    car.count += quantity
                    messagebox.showinfo("Add Existing Car", f"Added {quantity} to {car.make} {car.model}. New Count: {car.count}")
                    dialog.destroy()
                    self.view_inventory()
                else:
                    messagebox.showwarning("Car Not Found", "No car found with the specified Main ID.")
            except ValueError:
                messagebox.showwarning("Invalid Input", "Please enter a valid quantity.")

        add_btn = tk.Button(dialog, text="Add", command=add_existing)
        add_btn.pack(pady=10)

    def add_new_car(self, parent_dialog):
        parent_dialog.destroy()  # Close the main dialog

        dialog = tk.Toplevel(self.root)
        dialog.title("Add New Car")
        dialog.attributes('-topmost', True)
        self.center_dialog(dialog)

        fields = ["Make", "Model", "Year", "Price", "Color", "Car Type", "Quantity"]
        entries = {}

        for field in fields:
            label = tk.Label(dialog, text=f"Enter car {field}:")
            label.pack(pady=5)
            entry = tk.Entry(dialog)
            entry.pack(pady=5)
            entries[field] = entry

        def add_new():
            try:
                year = int(entries["Year"].get())
                price = float(entries["Price"].get())
                count = int(entries["Quantity"].get())
                car = Car(None, entries["Make"].get(), entries["Model"].get(), year, price, entries["Color"].get(), entries["Car Type"].get(), count)
                self.showroom.add_car(car)
                messagebox.showinfo("Add New Car", f"Car added successfully with ID: {car.car_id}")
                dialog.destroy()
                self.view_inventory()
            except ValueError:
                messagebox.showwarning("Invalid Input", "Please enter valid data.")

        add_btn = tk.Button(dialog, text="Add Car", command=add_new)
        add_btn.pack(pady=10)

    def view_financials(self):
        financials = (
            f"Total Sales: ₹{self.showroom.total_sales:.2f}\n"
            f"Total Commission Earned: ₹{self.showroom.total_commission:.2f}\n"
            f"Net Profit: ₹{self.showroom.total_sales - self.showroom.total_commission:.2f}"
        )
        messagebox.showinfo("Financial Report", financials)

    def center_dialog(self, dialog):
        self.root.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - (dialog.winfo_width() // 2)
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShowroomApp(root)
    root.mainloop()
