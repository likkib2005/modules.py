def total_marks(marks):
    return sum(marks)
def average_marks(marks):
    return sum(marks)/len(marks)
def grade(avg):
    if avg>=90:
        return "A+"
    elif avg>=75:
        return "A"
    elif avg>=60:
        return "B"
    elif avg>=45:
        return "c"
    else:
        return "F"