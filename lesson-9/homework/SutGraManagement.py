import csv
from collections import defaultdict

grades_data = [
    ["Name", "Subject", "Grade"],
    ["Alice", "Math", 85],
    ["Bob", "Science", 78],
    ["Carol", "Math", 92],
    ["Dave", "History", 74]
]

with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(grades_data)


grades = []
with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Grade"] = int(row["Grade"])
        grades.append(row)

subject_grades = defaultdict(list)
for row in grades:
    subject_grades[row["Subject"]].append(row["Grade"])

average_grades = {subject: sum(grades) / len(grades) for subject, grades in subject_grades.items()}

with open("average_grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg in average_grades.items():
        writer.writerow([subject, round(avg, 2)])

