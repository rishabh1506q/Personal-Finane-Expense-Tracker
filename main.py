"""Entry point:  python main.py"""
import logging
import sys

from config import DATA_DIR, LOG_PATH


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(filename=LOG_PATH, level=logging.WARNING,
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    try:
        from ui.app import FinanceApp
    except ImportError as error:
        print(f"Missing dependency: {error}\nInstall everything with:  pip install -r requirements.txt")
        sys.exit(1)
    FinanceApp().mainloop()


if __name__ == "__main__":
    main()
