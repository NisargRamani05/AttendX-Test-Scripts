
# Login Test Script for AttendX

def test_valid_login():
    username = "student01"
    password = "pass123"

    if username == "student01" and password == "pass123":
        print("PASS: Valid login successful")
    else:
        print("FAIL: Valid login unsuccessful")


def test_invalid_login():
    username = "student01"
    password = "wrongpass"

    if username == "student01" and password == "pass123":
        print("FAIL: Invalid login accepted")
    else:
        print("PASS: Invalid login rejected")


test_valid_login()
test_invalid_login()
