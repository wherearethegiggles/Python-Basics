def assign_grades():
    percentage = float(input("Enter the percentage of marks: "))

    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    elif percentage >= 50:
        grade = 'E'
    else:
        grade = 'F'

    print("Grade:", grade)

# Call the function
assign_grades()
