names = ["Sita", "Ram", "Gita"]
marks = [[90, 85, 78], [45, 38, 60], [70, 65, 80]]


def get_average(marks):
    """Return the average of a list of marks, rounded to 2 places."""
    return round(sum(marks) / len(marks), 2)


def get_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"


def report(name, marks, pass_mark=40):
    """Print one student's summary and return the average."""
    average = get_average(marks)
    grade = get_grade(average)
    best = max(marks)
    worst = min(marks)
    passed_all = worst >= pass_mark

    print(f"{name}: avg {average}, grade {grade}")
    print(f"  Best: {best} | Worst: {worst}")
    print(f"  Passed all? {passed_all}")
    return average


averages = []
for name, std_marks in zip(names, marks):
    averages.append(report(name, std_marks))

for rank, avg in enumerate(sorted(averages, reverse=True), start=1):
    print(f"Rank {rank}: {avg}")