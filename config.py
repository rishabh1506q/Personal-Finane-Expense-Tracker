"""Central configuration for the Personal Finance & Expense Intelligence System.

Keeping every constant in one place means categories, thresholds and file
locations can be changed without touching the rest of the code.
"""
from pathlib import Path

APP_NAME = "Personal Finance & Expense Intelligence System"

# ---- File locations ---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
EXPORT_DIR = BASE_DIR / "exports"
DB_PATH = DATA_DIR / "finance.db"
LOG_PATH = DATA_DIR / "app.log"
SAMPLE_DATA_PATH = DATA_DIR / "sample_data.json"

# ---- Display ----------------------------------------------------------------
CURRENCY = "₹"

# ---- Fixed choices (tuples because they must never change at runtime) -------
EXPENSE_CATEGORIES = (
    "Food", "Transport", "Rent", "Utilities", "Shopping",
    "Entertainment", "Health", "Education", "Travel", "Other",
)
INCOME_SOURCES = ("Salary", "Freelance", "Business", "Investment", "Gift", "Other")
PAYMENT_METHODS = ("Cash", "UPI", "Credit Card", "Debit Card", "Net Banking")

# ---- Business rules ---------------------------------------------------------
BUDGET_ALERT_THRESHOLD = 0.80   # warn when 80% of a category budget is used
INSIGHT_MIN_CHANGE = 500        # ignore month-to-month changes smaller than this
MAX_DESCRIPTION_LENGTH = 100
