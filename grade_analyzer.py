
def process_scores(students):
    averages = {}

    for name, scores in students.items():
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg

    return averages

def classify_grades(averages):
    classified = {}

    grade_A = 90
    grade_B = 75
    grade_C = 60

    for name, avg in averages.items():
        if avg >= grade_A:
            grade = "A"
        elif avg >= grade_B:
            grade = "B"
        elif avg >= grade_C:
            grade = "C"
        else:
            grade = "F"

        classified[name] = (avg, grade)

    return classified

def generate_report(classified, passing_avg=70):
    total = len(classified)
    passed = 0

    print("===== Student Grade Report =====")

    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed += 1

        print(f"{name:<10} | Avg: {avg:.2f} | Grade: {grade} | Status: {status}")

    failed = total - passed

    print("================================")
    print(f"Total Students : {total}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")

    return passed

if __name__ == "__main__":

    students = {
        "Alice": [85, 90, 84],
        "Bob": [60, 65, 62],
        "Clara": [95, 97, 97]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)
