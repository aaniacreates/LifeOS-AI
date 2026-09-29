import csv
import os
from datetime import date

DATA_FILE = "daily_data.csv"

EXPECTED_HEADERS = [
    "Date", "Sleep", "Study", "Screen_Time", "Exercise",
    "Mood", "Stress", "Tasks_Planned", "Tasks_Completed",
    "Productivity_Score"
]


def create_data_file():
    """Create the CSV data file if it does not exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="") as file:
            csv.writer(file).writerow(EXPECTED_HEADERS)
        return

    with open(DATA_FILE, "r", newline="") as file:
        existing_headers = next(csv.reader(file), [])

    if existing_headers != EXPECTED_HEADERS:
        backup_name = DATA_FILE.replace(".csv", "_old.csv")
        os.replace(DATA_FILE, backup_name)
        with open(DATA_FILE, "w", newline="") as file:
            csv.writer(file).writerow(EXPECTED_HEADERS)


def save_daily_record(record):
    """Append one validated daily record to CSV storage."""
    create_data_file()
    with open(DATA_FILE, "a", newline="") as file:
        csv.writer(file).writerow([
            date.today(),
            record["Sleep"],
            record["Study"],
            record["Screen_Time"],
            record["Exercise"],
            record["Mood"],
            record["Stress"],
            record["Tasks_Planned"],
            record["Tasks_Completed"],
            record["Productivity_Score"],
        ])


def load_records():
    """Return all saved records as dictionaries."""
    create_data_file()
    with open(DATA_FILE, "r", newline="") as file:
        return list(csv.DictReader(file))
