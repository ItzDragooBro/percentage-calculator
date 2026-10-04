def get_marks():
    math = int(input("Enter Maths marks: "))
    science = int(input("Enter Science marks: "))
    english = int(input("Enter English marks: "))
    return math, science, english


def Total(math, science, english):
    return math + science + english


def percentage(total):
    return total/300*100


def result(percentage):
    if percentage >= 40:
        return "Pass"
    else:
        return "Fail"

def main():
    print(" Student Marks")

    math, science, english = get_marks()

    total = Total(math, science, english)
    percent = percentage(total)
    status = result(percent)

    print("\n Result")
    print("Total Marks:", total, "/ 300")
    print("Percentage:", percent, "%")
    print("Result:", status)

print(main())
