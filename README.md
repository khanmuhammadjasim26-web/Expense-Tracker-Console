# 💰 Console-Based Expense Tracker

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey?style=for-the-badge)
![Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Standard%20Library)-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A clean, robust, and interactive console-based personal finance management application developed in Python. Engineered strictly around core computational fundamentals—utilizing loops, conditional routing, lists, and dictionary mappings to deliver intuitive real-time financial tracking and aggregation without external dependencies.

---

## 🌟 Key Features

| Feature | Description |
| :--- | :--- |
| ➕ **Granular Expense Logging** | Capture structured records with timestamp (`DD-MM-YYYY`), category, narrative description, and floating-point numeric valuation. |
| 📄 **Formatted Tabular Ledger** | Inspect recorded transactions in an aligned, readable fixed-width tabular console format. |
| 💵 **Real-Time Cumulative Total** | Instantaneous single-pass accumulation of total personal expenditure. |
| 📊 **Category Breakdown** | Dynamic dictionary-based category aggregation providing spending breakdown across categories (e.g., Food, Travel, Stay). |
| 🛡️ **Defensive Input Handling** | Built-in numeric sanitization preventing program crashes on invalid amount entries. |
| 🚪 **Graceful Session Termination** | Clean user-directed break out of execution loop. |

---

## 🏗️ Architecture & Core Concepts

The architecture adheres strictly to core Python programming constructs, demonstrating foundational data structure manipulation without relying on third-party frameworks or user-defined function abstractions.

```
       ┌───────────────────────────────┐
       │   CLI Application Entrance    │
       │    (Interactive REPL Loop)    │
       └──────────────┬────────────────┘
                      │
           ┌──────────▼──────────┐
           │     Select Menu     │
           │     Option [1-5]    │
           └────┬─────────┬──────┘
                │         │
    ┌───────────┴─┐     ┌─┴────────────┐
    │ 1. Log Entry│     │ 2. Read View │
    └──────┬──────┘     └──────┬───────┘
           │                   │
           ▼                   ▼
    ┌─────────────┐     ┌──────────────┐
    │ Dictionary  │     │ Format Fixed │
    │ Construction│     │ Width String │
    └──────┬──────┘     └──────────────┘
           │
           ▼
    ┌───────────────────────────┐
    │  In-Memory Ledger (List)  │ ◄── Primary State
    └──────┬────────────┬───────┘
           │            │
    ┌──────┴──────┐   ┌─┴──────────────┐
    │ 3. Aggregate│   │ 4. Categorize  │
    │  Sum Total  │   │ Dictionary Map │
    └─────────────┘   └────────────────┘
```

### Concept Implementation Matrix

| Concept | Purpose & Implementation |
| :--- | :--- |
| `while True` | Infinite execution loop running the interactive terminal menu until intentional user exit. |
| `if / elif / else` | Branching decision tree mapping menu choices and handling empty state edge cases. |
| `list` (`expenses = []`) | Dynamic in-memory array maintaining chronologically ordered expense records. |
| `dict` (`{...}`) | Key-value schema encapsulating transaction attributes (`date`, `category`, `description`, `amount`). |
| `for` loop | Linear traversal ($O(N)$) for table presentation, cumulative summing, and category clustering. |
| `input()` / `print()` | Formatted standard stream input/output handling user prompts and formatted report displays. |

---

## 🚀 Quickstart & Usage

### Prerequisites
- Python 3.8 or higher installed on your system.

### Running the Application

1. Clone or download this repository:
   ```bash
   git clone https://github.com/khanmuhammadjasim26-web/Expense-Tracker-Console.git
   cd Expense-Tracker-Console
   ```

2. Launch the script directly using Python:
   ```bash
   python expense_tracker.py
   ```

---

## 💻 Visual Walkthrough & Sample Run

### 1. Interactive Menu
```text
==================================================
           WELCOME TO EXPENSE TRACKER
==================================================

====================== MENU ======================
  1. Add Expense
  2. View Recorded Expenses
  3. View Total Spending
  4. View Expenses by Category
  5. Exit
==================================================
Enter your choice (1-5): 1
```

### 2. Adding Expenses
```text
--- [ Add New Expense ] ---
Enter date (DD-MM-YYYY): 26-09-2026
Enter category (e.g., Food, Travel, Stay, Shopping): Travel
Enter short description: Triund Trek
Enter amount (INR): 2000

>> Expense added successfully!
```

### 3. Viewing Recorded Ledger
```text
----------------------------------------------------------------------
                       RECORDED EXPENSES
----------------------------------------------------------------------
 1. Date: 26-09-2026 | Category: Travel       | Desc: Triund Trek        | Amount: INR  2000.00
 2. Date: 28-09-2026 | Category: Food         | Desc: Camp meal          | Amount: INR   500.00
 3. Date: 29-09-2026 | Category: Stay         | Desc: Guest House        | Amount: INR  1000.00
----------------------------------------------------------------------
```

### 4. Summary & Category Breakdown
```text
-----------------------------------
  Total Spending: INR 3,500.00
-----------------------------------

----------------------------------------
          EXPENSES BY CATEGORY
----------------------------------------
  * Travel           : INR  2000.00
  * Food             : INR   500.00
  * Stay             : INR  1000.00
----------------------------------------
```

---

## 📁 Repository Structure

```
Expense-Tracker-Console/
├── expense_tracker.py    # Main executable Python application
├── README.md             # Project documentation and specifications
├── LICENSE               # MIT License
└── .gitignore            # Git exclusion rules
```

---

## 👤 Author

- **Mohd Jasim Khan**
- GitHub: [@khanmuhammadjasim26-web](https://github.com/khanmuhammadjasim26-web)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.
