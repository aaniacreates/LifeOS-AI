from data_manager import load_records
from utils import print_title, print_rule


def ai_insights():
    """Generate simple rule-based insights from the user's own data."""
    records = load_records()

    if len(records) < 3:
        print("\nAt least three logged days are required to identify trends.")
        return

    recent_records = records[-7:]
    low_sleep_days = 0
    high_screen_days = 0
    productive_days = 0

    for record in recent_records:
        sleep = float(record["Sleep"])
        screen_time = float(record["Screen_Time"])
        score = float(record["Productivity_Score"])

        if sleep < 6:
            low_sleep_days += 1
        if screen_time > 6:
            high_screen_days += 1
        if score >= 70:
            productive_days += 1

    print()
    print_title(f"TRENDS - LAST {len(recent_records)} DAYS")
    print(f"\n  Low-sleep days:          {low_sleep_days}")
    print(f"  High-screen-time days:  {high_screen_days}")
    print(f"  Productive days (70+):  {productive_days}")

    print_rule()
    print("Patterns")
    found_pattern = False

    if low_sleep_days >= 2 and high_screen_days >= 2:
        print("  - Low sleep and high screen time both appeared repeatedly.")
        found_pattern = True
    elif low_sleep_days >= 2:
        print("  - Sleep was short on several days.")
        found_pattern = True
    elif high_screen_days >= 2:
        print("  - Screen time was high on several days.")
        found_pattern = True

    if productive_days >= 4:
        print("  - Most days in this window reached the configured productive range.")
        found_pattern = True

    if not found_pattern:
        print("  - No strong recurring pattern has been identified yet.")

    print("\n  Note: These are patterns in logged numbers, not a diagnosis.")
    print_rule()
