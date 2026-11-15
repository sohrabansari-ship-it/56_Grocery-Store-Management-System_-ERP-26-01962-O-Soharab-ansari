# Grocery Store Management System (PS No. 56)

A Python 3 console-based billing and inventory management application built for a grocery store.

## Features
- **Inventory Management:** Stores item prices and stock quantities using Python dictionaries.
- **Interactive Billing Cart:** Uses Python lists to collect customer items and validate stock in real time.
- **Automated Calculations:**
  - Applies a **10% discount** automatically when the subtotal is **Rs. 1000 or more**.
  - Calculates **5% GST** on the post-discount amount.
- **Stock Deduction & File Persistence:** Automatically updates remaining inventory after checkout and appends every finalized receipt to `bills.txt`.

## Initial Inventory
| Item | Price | Initial Stock |
| :--- | :--- | :--- |
| Rice | Rs. 50 / kg | 100 |
| Sugar | Rs. 45 / kg | 50 |
| Milk | Rs. 30 / L | 40 |
| Oil | Rs. 150 / L | 20 |

## How to Run
1. Ensure Python 3 is installed on your system.
2. Navigate to the `Codebase` directory in your terminal.
3. Run the script:
   ```bash
   python grocery_billing.py
