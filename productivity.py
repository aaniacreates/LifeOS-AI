def performance_tag(score):
    if score >= 80:
        return "EXCELLENT"
    if score >= 65:
        return "GOOD"
    if score >= 50:
        return "AVERAGE"
    return "NEEDS IMPROVEMENT"


def calculate_productivity(
    sleep, study, screen_time, exercise, mood, stress,
    tasks_planned, tasks_completed
):
    """Calculate a 100-point rule-based productivity score."""
    breakdown = {}

    if sleep >= 7:
        breakdown["Sleep"] = 20
    elif sleep >= 6:
        breakdown["Sleep"] = 15
    elif sleep >= 5:
        breakdown["Sleep"] = 10
    else:
        breakdown["Sleep"] = 5

    if study >= 6:
        breakdown["Study"] = 25
    elif study >= 4:
        breakdown["Study"] = 20
    elif study >= 2:
        breakdown["Study"] = 12
    else:
        breakdown["Study"] = 5

    if screen_time <= 4:
        breakdown["Screen Time"] = 15
    elif screen_time <= 6:
        breakdown["Screen Time"] = 10
    elif screen_time <= 8:
        breakdown["Screen Time"] = 5
    else:
        breakdown["Screen Time"] = 2

    if exercise >= 30:
        breakdown["Exercise"] = 10
    elif exercise >= 15:
        breakdown["Exercise"] = 7
    else:
        breakdown["Exercise"] = 3

    breakdown["Mood"] = mood

    if stress <= 3:
        breakdown["Stress"] = 10
    elif stress <= 6:
        breakdown["Stress"] = 7
    elif stress <= 8:
        breakdown["Stress"] = 4
    else:
        breakdown["Stress"] = 1

    if tasks_planned == 0:
        breakdown["Tasks"] = 0
    else:
        completion = (tasks_completed / tasks_planned) * 100
        if completion >= 90:
            breakdown["Tasks"] = 10
        elif completion >= 75:
            breakdown["Tasks"] = 8
        elif completion >= 50:
            breakdown["Tasks"] = 6
        else:
            breakdown["Tasks"] = 3

    return sum(breakdown.values()), breakdown
