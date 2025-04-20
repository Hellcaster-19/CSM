# GUI Car Showroom Management System

A Python-based desktop application built using **Tkinter** for managing car inventories in a virtual showroom. This GUI app allows users to **view, add, filter, and sell cars**, while automatically tracking **sales and commission**.



##  Features

-  **View Inventory** – Displays all available cars with details.  
-  **Filter Cars** – Search inventory by make, model, color, car type, or price.  
-  **Add Cars** – Add new car models or increase count of existing models.  
-  **Sell Cars** – Sell cars by ID with real-time inventory updates.  
-  **Financial Overview** – Track total sales, commission earned, and net profit.  
-  **User-Friendly GUI** – Built with Tkinter featuring buttons, dialogs, and scrolled views.



## Technologies Used

- **Python 3**
- **Tkinter** (Standard GUI library)
- **OOP Principles** (Encapsulated `Car` and `Showroom` classes)



## Use Cases

- Small dealerships managing offline inventory  
- Learning resource for students studying **GUI development** and **object-oriented design**  
- Demonstration of basic **inventory management system**



## How It Works

- **Cars** are stored in a list with attributes like `make`, `model`, `year`, `price`, etc.  
- Each car is assigned a **unique ID** and **count** to handle inventory.  
- **Cosmetic events** (like hover effects) are added to buttons for better UX.  
- Financials are automatically updated after each sale, including **commission calculation**:
  - `< ₹5L` → 5%  
  - `₹5L – ₹15L` → 7%  
  - `> ₹15L` → 10%



##  Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gui-car-showroom.git
   cd gui-car-showroom
   ```

2. Run the program:
   ```bash
   python GUICar.py
   ```

> Make sure you have **Python 3** installed.

##  Future Improvements

- Add persistent storage (e.g., SQLite, JSON)  
- Implement search by multiple filters  
- Improve UI design with `ttk` or custom themes  
- Export financial reports  
- Add user authentication

## 📄 License

MIT License – Free to use, modify, and distribute.

