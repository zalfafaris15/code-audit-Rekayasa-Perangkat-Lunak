GRADE_THRESHOLDS = [
    (85, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
]
DEFAULT_GRADE = "E"

student_scores = []


def add_score(student_name: str, score: float, exam_type: str) -> dict:
    """Add a score entry for a student."""
    entry = {
        "student_name": student_name,
        "score": score,
        "exam_type": exam_type,
    }
    student_scores.append(entry)
    return entry


def display_all_scores():
    """Print all recorded student scores."""
    for entry in student_scores:
        print(entry["student_name"], entry["score"], entry["exam_type"])


def calculate_average(student_name: str) -> float:
    """Calculate the average score for a given student."""
    scores = [
        entry["score"]
        for entry in student_scores
        if entry["student_name"] == student_name
    ]
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def determine_grade(average: float) -> str:
    """Determine letter grade based on average score."""
    for threshold, grade in GRADE_THRESHOLDS:
        if average >= threshold:
            return grade
    return DEFAULT_GRADE


def print_student_result(student_name: str):
    """Print the average and grade for a student."""
    average = calculate_average(student_name)
    grade = determine_grade(average)
    print(f"{student_name} - Rata-rata: {average:.2f}, Grade: {grade}")


def get_unique_student_names() -> list:
    """Return a list of unique student names from score records."""
    return list({entry["student_name"] for entry in student_scores})


def process_all_students():
    """Calculate and display results for all students."""
    unique_names = get_unique_student_names()
    for name in unique_names:
        print_student_result(name)



add_score("Budi", 80, "UTS")
add_score("Budi", 90, "UAS")
add_score("Budi", 75, "Tugas")
add_score("Siti", 60, "UTS")
add_score("Siti", 70, "UAS")
add_score("Siti", 55, "Tugas")

display_all_scores()
process_all_students()
