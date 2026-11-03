"""Load demo data (user 'demo', password 'Demo@1234') so every screen has something to show.

Run:  python load_sample_data.py
Dates are generated relative to today, so the demo always covers the last 6 months.
"""
import json
from datetime import date

from config import SAMPLE_DATA_PATH
from core.auth import AuthService
from core.budget import BudgetManager
from core.database import Database
from core.exceptions import AuthError, FinanceError
from core.expense import ExpenseManager
from core.income import IncomeManager
from core.utils import current_month, shift_month


def resolve_date(months_ago, day):
    """Turn (months_ago, day) into a real date string; returns None for future days."""
    month = shift_month(current_month(), -months_ago)
    day = min(day, 28)
    if months_ago == 0 and day > date.today().day:
        return None
    return f"{month}-{day:02d}"


def load_sample_data(db=None):
    db = db or Database()
    with open(SAMPLE_DATA_PATH, encoding="utf-8") as file:
        data = json.load(file)

    auth = AuthService(db)
    demo = data["demo_user"]
    try:
        user = auth.login(demo["username"], demo["password"])
    except AuthError:
        user = auth.register(demo["username"], demo["email"], demo["password"], demo["password"])

    incomes, expenses, budgets = IncomeManager(db), ExpenseManager(db), BudgetManager(db)
    if incomes.search(user["id"]) or expenses.search(user["id"]):
        print("Demo data is already loaded. Log in with demo / Demo@1234.")
        return user

    for item in data["income"]:
        when = resolve_date(item["months_ago"], item["day"])
        if when:
            incomes.add(user["id"], item["amount"], item["source"], item["description"], when)

    for item in data["expenses"]:
        when = resolve_date(item["months_ago"], item["day"])
        if when:
            expenses.add(user["id"], item["amount"], item["category"], item["description"],
                         when, item["payment_method"])

    for months_ago in data["budget_months_ago"]:
        month = shift_month(current_month(), -months_ago)
        for budget in data["budgets"]:
            budgets.set_budget(user["id"], budget["category"], month, budget["limit"])

    print("Sample data loaded. Log in with  username: demo  |  password: Demo@1234")
    return user


if __name__ == "__main__":
    try:
        load_sample_data()
    except FinanceError as error:
        print(f"Could not load sample data: {error}")
