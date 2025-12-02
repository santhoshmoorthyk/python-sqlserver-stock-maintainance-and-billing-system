# Python Stock Management & Billing System (SQL Server)

This project is a **console-based stock management and billing system** built using **Python**, **SQL Server**, and **pyodbc**.  
It provides a complete workflow for:

- Adding and updating products  
- Maintaining live inventory  
- Auto-updating extended price (via SQL trigger)  
- Billing operations without breaking the inventory logic  
- Recording sales logs automatically  

---

## Features

### **1. Product Management Module**
Python module that interacts with the **products** table:
- Add new stock  
- Update price  
- Update quantity (instock)  
- Delete products  
- View entire stock data  
- SQL trigger automatically updates extended price whenever price or instock changes  

### **2. Billing Module**
A separate Python module that:
- Accepts product ID input  
- Fetches price & stock name from SQL Server  
- Calculates billing totals (`qty × price`)  
- Updates stock quantity in **products** table  
- Inserts every sale into the **sales** table  

---

##  Database Structure

### **Table 1: products**
| Column        | Type        | Description |
|--------------|-------------|-------------|
| sid          | INT (PK)    | Auto increment product ID |
| stockname    | VARCHAR     | Name of the product |
| instock      | INT         | Current available quantity |
| price        | INT         | Price per unit |
| extendedprice | AS (price * instock) | Auto-updated using SQL trigger |

###  Trigger  
A SQL Server trigger updates `extendedprice` whenever:
- `price` changes  
- `instock` changes  

---

### **Table 2: sales**
| Column     | Type        | Description |
|------------|-------------|-------------|
| id         | INT (PK)    | Auto increment sale ID |
| sdate      | DATETIME    | Auto-filled using GETDATE() |
| p          | VARCHAR(50) | Product name sold |
| quantity   | INT         | Quantity sold |
| totalamt   | INT         | Total amount (price × qty) |

Example row:
```
id: 2
sdate: 2025-12-02 19:51:06.723
stockname: Rice bag
qty: 1
totalprice: 50
```

---

##  Project Modules Overview

### **1. pr1.py (Stock Management Module)**
Contains functions:
- `a1()` → Add new product  
- `a2()` → Update instock  
- `a3()` → Update price  
- `a4()` → Delete stock  
- `a5()` → Show all stock  

Uses `pyodbc` connection and commits updates only on user confirmation.

---

### **2. main.py (Application Entry Point)**
- Displays menu  
- Detects key input using `msvcrt.getch()`  
- Calls functions from `pr1.py`

---

### **3. billing.py (Billing Module)**
- Runs a loop until user presses **ESC**  
- Accepts stock ID  
- Retrieves price + name  
- Calculates extended price  
- Updates instock  
- Inserts record into **sales** table  
- Stores purchase summary in dictionary  
- Prints formatted bill at the end  

---

##  Requirements

- Python 3.x  
- SQL Server  
- ODBC Driver 17 for SQL Server  
- pyodbc module  
- Windows OS (msvcrt input detection)  

Install pyodbc:
```bash
pip install pyodbc
```

---

##  Database Connection String
```python
pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=YOUR_SERVER_NAME;"
    "DATABASE=sk;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)
```

---

##  Example Output (Billing Summary)
```
sid   stockname   price   qty   extendedprice
1     Rice bag      50     1        50
2     Sugar         40     3       120
```

---

##  Notes
- Billing module **updates instock automatically**.  
- Extended price is fully managed by SQL Server trigger.  
- No ORM is used; **raw SQL queries** for full control.  

---

##  License
Open-source – free to modify and use.

---

##  Author
Santhosh K  
Python + SQL Server Stock/Billing System
