from statistics import mean
from data_manager import load_records
from utils import print_title, print_rule


def view_previous_data():
    records = load_records()

    if not records:
        print("\nNo entries have been recorded yet.")
        return

    print()
    print_title("HISTORY")

    for record in records:
        print(
            f"  {record['Date']} | "
            f"Sleep {record['Sleep']}h | "
            f"Study {record['Study']}h | "
            f"Screen {record['Screen_Time']}h | "
            f"Score {record['Productivity_Score']}/100"
        )
    print_rule()


def weekly_report():
    records = load_records()

    if not records:
        print("\nNo data is available yet. Please log at least one day.")
        return

    recent_records = records[-7:]

    sleep_values = [float(r["Sleep"]) for r in recent_records]
    study_values = [float(r["Study"]) for r in recent_records]
    screen_values = [float(r["Screen_Time"]) for r in recent_records]
    exercise_values = [float(r["Exercise"]) for r in recent_records]
    mood_values = [float(r["Mood"]) for r in recent_records]
    stress_values = [float(r["Stress"]) for r in recent_records]
    score_values = [float(r["Productivity_Score"]) for r in recent_records]

    print()
    print_title(f"WEEKLY REPORT - {len(recent_records)} DAYS")
    print(f"\n  Average Sleep        {mean(sleep_values):.2f} h")
    print(f"  Average Study        {mean(study_values):.2f} h")
    print(f"  Average Screen Time  {mean(screen_values):.2f} h")
    print(f"  Average Exercise     {mean(exercise_values):.2f} min")
    print(f"  Average Mood         {mean(mood_values):.2f}/10")
    print(f"  Average Stress       {mean(stress_values):.2f}/10")
    print(f"  Average Score        {mean(score_values):.2f}/100")

    print_rule()
    print("Focus Areas")

    focus_areas = []
    if mean(sleep_values) < 6:
        focus_areas.append("Prioritize more consistent sleep.")
    if mean(screen_values) > 6:
        focus_areas.append("Reduce non-essential screen time.")
    if mean(study_values) < 3:
        focus_areas.append("Allocate more dedicated study time.")
    if mean(exercise_values) < 20:
        focus_areas.append("Include regular physical activity.")

    if not focus_areas:
        print("  - No configured focus area was triggered.")
    else:
        for area in focus_areas:
            print("  - " + area)
    print_rule()
