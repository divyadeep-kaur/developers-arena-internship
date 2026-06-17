# Student Grade Calculator

# Function to determine grade and message
def get_grade_and_message(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep shining! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good job! Continue improving! 😊"
    elif marks >= 60:
        return "D", "You passed. Work a little harder next time! 📚"
    else:
        return "F", "Don't give up. Keep practicing and you'll improve! 💪"


# Taking student name
name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("❌ Marks must be between 0 and 100.")

    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")

# Getting grade and message
grade, message = get_grade_and_message(marks)

# Displaying result
print("\n📊 RESULT")
print("-" * 30)
print(f"Student Name: {name.upper()}")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")