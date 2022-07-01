student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
    }

for student in student_scores:
    grade = student_scores[student]
    if grade > 90:
        print(f"{student} is Outstanding")
    elif grade > 80:
        print(f"{student} is Exceed Expectations")
    elif grade > 70:
        print(f"{student} is Acceptable")
    else:
        print(f"{student} is Fail")



# Nested diccionaries
travel_log = {
            "France": {"cities":["Paris","Lille","Djion"],"total":12},
            "Germany": "Berlin"
}


















