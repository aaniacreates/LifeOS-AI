from data_manager import create_data_file, save_daily_record
from productivity import calculate_productivity
from analysis import daily_analysis
from reports import view_previous_data, weekly_report
from insights import ai_insights
from utils import print_title, get_number


def enter_daily_data():
    print("\n--- Daily Data Entry ---")

    sleep = get_number("Sleep hours: ", 0, 24)
    study = get_number("Study hours: ", 0, 24)
    screen_time = get_number("Screen time hours: ", 0, 24)
    exercise = get_number("Exercise minutes: ", 0, 1440)
    mood = get_number("Mood (1-10): ", 1, 10)
    stress = get_number("Stress (1-10): ", 1, 10)
    tasks_planned = get_number("Tasks planned: ", 0)
    tasks_completed = get_number("Tasks completed: ", 0)

    if tasks_completed > tasks_planned:
        print("\nTasks completed cannot exceed tasks planned. Entry not saved.")
        return

    score, breakdown = calculate_productivity(
        sleep, study, screen_time, exercise, mood, stress,
        tasks_planned, tasks_completed
    )

    daily_analysis(
        sleep, study, screen_time, exercise, mood, stress,
        tasks_planned, tasks_completed, score, breakdown
    )

    save_daily_record({
        "Sleep": sleep,
        "Study": study,
        "Screen_Time": screen_time,
        "Exercise": exercise,
        "Mood": mood,
        "Stress": stress,
        "Tasks_Planned": tasks_planned,
        "Tasks_Completed": tasks_completed,
        "Productivity_Score": score,
    })

    print("\nEntry saved successfully.")


def main():
    create_data_file()

    while True:
        print()
        print_title("LIFEOS AI - PERSONAL STUDENT LIFE ANALYZER")
        print("  1. Enter Today's Data")
        print("  2. View Previous Data")
        print("  3. Weekly Report")
        print("  4. AI Insights")
        print("  5. Exit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            enter_daily_data()
        elif choice == "2":
            view_previous_data()
        elif choice == "3":
            weekly_report()
        elif choice == "4":
            ai_insights()
        elif choice == "5":
            print("\nThank you for using LifeOS AI. See you tomorrow!")
            break
        else:
            print("\nPlease enter a valid option between 1 and 5.")


if __name__ == "__main__":
    main()
