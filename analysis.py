from productivity import performance_tag


def daily_analysis(sleep, study, screen_time, exercise, mood, stress,
                   tasks_planned, tasks_completed, score, breakdown):
    print()
    print("=" * 60)
    print("DAILY REPORT".center(60))
    print("=" * 60)
    print(f"\nProductivity Score: {score}/100 ({performance_tag(score)})")
    print("\nScore Breakdown")

    for label, points in breakdown.items():
        bar = "#" * int(points)
        print(f"  {label:<12} {points:>5}  {bar}")

    print("\nNotes")
    notes = []

    if sleep < 6:
        notes.append("Sleep duration was below the configured target.")
    if screen_time > 6:
        notes.append("Screen time was elevated in this entry.")
    if study < 3:
        notes.append("Study time was limited in this entry.")
    if stress >= 8 and mood <= 4:
        notes.append("High stress and low mood occurred together.")
    if tasks_planned > 0:
        completion = (tasks_completed / tasks_planned) * 100
        if completion < 50:
            notes.append("Task completion was below 50%.")

    if not notes:
        notes.append("No configured concern was detected for this entry.")

    for note in notes:
        print("  - " + note)

    print("-" * 60)
