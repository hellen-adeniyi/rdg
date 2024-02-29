import csv


with open("users.csv", mode='w', newline='') as f:
    fieldnames = ['first_name', 'last_name', 'email', 'password', 'phone_number', 'dob', 'city', 'province']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()



def register_user():
    with open("users.csv", mode="a", newline="") as f:
        register_writer = csv.writer(f, delimiter=",") # writes to the csv file
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name: ")
        email = input("Please enter your email: ")
        password = input("Please enter you password: ")
        password_checker = input("Please enter your password again: ")
        phone_number = input("Please enter your phone number: ")
        dob = input("Please enter your date of birth in the format dd/mm/yyyy: ")
        city = input("Please enter your city: ")
        province = input("Please enter your province: ")
        if password == password_checker:
            register_writer.writerow([first_name, last_name, email, password, phone_number, dob, city, province])
            print("Registration is successful")
        else:
            print("Please try again.")


register_user()

def user_login():
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    with open("users.csv", mode="r", newline="") as f:
        reader = csv.reader(f,delimiter=",")
        for row in reader:
            if row == [email, password]:
                print("You are logged in!")
                return True
    print("Please try again.")
    return False
