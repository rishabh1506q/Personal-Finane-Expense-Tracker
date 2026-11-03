# 💰 Personal Finance & Expense Intelligence System

A desktop application that tracks income and expenses, enforces monthly budgets, and **analyses your spending to produce automatic insights**. Built with Python, OOP, SQLite, Pandas, Matplotlib and CustomTkinter.

> Built as a portfolio project to demonstrate clean, modular, well-tested Python.

---

## ✨ Features

| Area | What it does |
|---|---|
| **Accounts** | Register / login. Passwords are never stored in plain text (salted PBKDF2-SHA256). Each user only sees their own data. |
| **Income** | Add, edit, delete, search income by source (Salary, Freelance, ...). |
| **Expenses** | Add, edit, delete, view expenses with category, date, payment method and description. |
| **Search & filter** | Filter by keyword, category/source, date range and amount range. |
| **Budgets** | Set a monthly limit per category, copy last month's budgets, see live status. |
| **Budget alerts** | Pop-up warning right after saving an expense that reaches 80% or exceeds a budget. |
| **Analytics** | 5 interactive charts (pie, income vs expenses, category trend, month-vs-month comparison, daily spending) with hover tooltips and zoom/pan/save toolbar. |
| **Smart insights** | Computed from your data: savings rate, biggest category, categories that rose >20% vs last month, categories rising 3 months in a row, largest expense, month-end spending projection, budget problems. |
| **Reports** | Monthly and yearly reports shown in-app. |
| **Export** | Export reports or transactions to **CSV** and **JSON**. |
| **Validation** | Every input is validated (regex + real date checks). Errors show friendly messages; unexpected errors are logged to `data/app.log`. |

## 🧰 Technologies

Python 3.9+ · SQLite (`sqlite3`) · Pandas · Matplotlib · CustomTkinter · `hashlib` · `re` · `csv` / `json` · `unittest`

## 🚀 Installation

```bash
# 1. get the project
git clone https://github.com/<your-username>/FinanceTracker.git
cd FinanceTracker

# 2. (recommended) create a virtual environment
python -m venv venv
venv\Scripts\activate            # Windows
source venv/bin/activate         # macOS / Linux

# 3. install dependencies
pip install -r requirements.txt
```

> **Linux only:** Tkinter may need to be installed separately: `sudo apt install python3-tk`

## ▶️ How to run

```bash
python load_sample_data.py   # optional: creates demo user + 6 months of sample data
python main.py               # starts the app
```

Demo login: **username** `demo` · **password** `Demo@1234`

Tip: sample data is generated relative to today. Pick **last month** on the Dashboard to see the richest insights (rising categories, spending spikes, exceeded budgets).

Run the automated tests:

```bash
python -m unittest discover -v
```

## 📁 Folder structure

```
FinanceTracker/
├── main.py                  # entry point (logging + start GUI)
├── config.py                # paths, categories, thresholds
├── load_sample_data.py      # demo user + sample data loader
├── requirements.txt
├── core/                    # business logic (no GUI code)
│   ├── database.py          # SQLite connection + schema
│   ├── auth.py              # registration, login, password hashing
│   ├── models.py            # Transaction -> Income / Expense classes
│   ├── base_manager.py      # shared CRUD/search logic (parent class)
│   ├── income.py            # IncomeManager
│   ├── expense.py           # ExpenseManager
│   ├── budget.py            # budgets + alerts
│   ├── analytics.py         # Pandas analysis + insights
│   ├── reports.py           # reports + CSV/JSON export
│   ├── utils.py             # regex validators, date/money helpers
│   └── exceptions.py        # custom exceptions
├── ui/                      # CustomTkinter interface
│   ├── app.py               # main window + sidebar navigation
│   ├── login_screen.py
│   ├── dashboard_screen.py
│   ├── transaction_screen.py  # shared parent of the two screens below
│   ├── expense_screen.py
│   ├── income_screen.py
│   ├── budget_screen.py
│   ├── analytics_screen.py
│   ├── reports_screen.py
│   ├── charts.py            # Matplotlib drawing functions
│   └── widgets.py           # tables, cards, error-handling decorator
├── data/
│   └── sample_data.json     # demo data (finance.db is created on first run)
├── exports/                 # CSV / JSON exports land here
└── tests/
    └── test_core.py         # 20 automated tests
```

**How the parts fit together:** the UI never talks to SQLite directly. Screens call manager classes in `core/`, which validate input, run SQL, and return plain dictionaries / DataFrames. This separation is why the backend can be tested without opening a window.

## 🐍 Where each Python concept is used

| Concept | Where |
|---|---|
| Variables & data types | everywhere; `config.py` constants |
| Tuples / sets / dicts / lists | `config.py` (tuples), `base_manager.label_totals` (dict), `reports.py` (lists of dicts) |
| Conditionals & loops | `budget.get_status`, `analytics._category_insights` |
| Functions | `core/utils.py` validators and date helpers |
| Lambda, `map`, `filter`, comprehensions | `budget.alerts` (filter+lambda), `reports.yearly_report` (map), `analytics.generate_insights` (sort key), many comprehensions |
| OOP: classes & objects | managers, `Database`, `AuthService`, screens |
| Inheritance | `Transaction` → `Income`/`Expense`; `TransactionManager` → `ExpenseManager`/`IncomeManager`; `TransactionScreen` → `ExpenseScreen`/`IncomeScreen` |
| Encapsulation | validated properties in `models.py` (`_amount`, `_date`, ...) |
| Decorators | `handle_errors` in `ui/widgets.py` |
| Context managers | `Database.connection()` (commit / rollback / close) |
| File handling | CSV/JSON export in `reports.py`, sample data loading |
| Exception handling | custom exceptions + `handle_errors` + logging |
| Modules & packages | `core/` and `ui/` packages |
| Regular expressions | username, email, password rules, amount, date, month in `utils.py` |
| Date & time | `datetime`, `calendar`, `shift_month`, month projections |
| SQLite & SQL | schema, indexes, `GROUP BY`, `UNION ALL`, upsert (`ON CONFLICT`) |
| Data analysis | Pandas `groupby`, `pivot_table`, `reindex`, comparisons in `analytics.py` |
| Data visualisation | Matplotlib charts in `ui/charts.py`, embedded in the GUI |
| Security | PBKDF2 hashing, per-user salt, constant-time compare, parameterised SQL |
| Testing | `unittest` suite with an isolated temporary database |

## 🖼️ Screenshots

Add your own screenshots after running the app:

| Dashboard | Expenses |
|---|---|
| ![Dashboard](screenshots/dashboard.png) | ![Expenses](screenshots/expenses.png) |

| Budget | Analytics |
|---|---|
| ![Budget](screenshots/budget.png) | ![Analytics](screenshots/analytics.png) |

## ✅ Manual testing checklist

1. **Register** a new account (try weak password / duplicate username → friendly errors). **Login** with wrong password → error.
2. Run `load_sample_data.py`, login as `demo`.
3. **Expenses:** add one, edit it (double-click a row), delete it. Try amount `abc`, `-5`, date `2026-13-45`, future date → rejected.
4. **Filters:** search by text, category, date range, min/max amount; click Reset.
5. **Income:** add / edit / delete an income record.
6. **Budget:** set Food limit; add an expense that crosses 80% then 100% → alert pop-up each time. Try *Copy previous month*.
7. **Dashboard:** change month; cards and insights change. Pick last month to see warnings.
8. **Analytics:** switch all 5 charts, hover bars/slices, zoom with the toolbar, change *Compare with*.
9. **Reports:** generate monthly + yearly; export report CSV/JSON; export transactions; *Open exports folder*.
10. **Persistence:** close the app, reopen, login → all data still there.
11. **Security:** open `data/finance.db` in a SQLite viewer → `password_hash` is a hash, not your password.

## 🔮 Future improvements

- Recurring transactions and bill reminders
- Import transactions from bank CSV files
- Savings goals with progress tracking
- Multi-currency support
- Light / dark theme switch
- Package as a standalone `.exe` with PyInstaller
- Forecasting next month's spending with a simple regression model

## 📄 License

MIT
