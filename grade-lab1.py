def calculate_grade(scores):
    # 1. เช็คกรณีลิสต์ว่าง เพื่อป้องกัน ZeroDivisionError
    if not scores:
        return "N/A", 0

    # 2. ใช้ sum() แทนการเขียน loop บวกเอง
    total = sum(scores)
    average = total / len(scores)
    
    # 3. ตรรกะการตัดเกรด (ถูกต้องอยู่แล้ว)
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return grade, average

# ทดสอบใช้งาน
scores = [85, 92, 78, 88, 95]
grade, avg = calculate_grade(scores)
print(f"Grade: {grade}, Average: {avg:.2f}")

# ทดสอบกรณีลิสต์ว่าง
print(calculate_grade([]))
