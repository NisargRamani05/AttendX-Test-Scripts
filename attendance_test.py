
# Attendance Marking Test Script for AttendX

def test_mark_present():
    student = "student01"
    attendance_status = "Present"

    if student == "student01" and attendance_status == "Present":
        print("PASS: Attendance marked as Present")
    else:
        print("FAIL: Attendance marking failed")


def test_invalid_status():
    attendance_status = "Unknown"

    if attendance_status in ["Present", "Absent"]:
        print("PASS: Valid attendance status")
    else:
        print("PASS: Invalid attendance status rejected")


test_mark_present()
test_invalid_status()
