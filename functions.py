import csv
import time


with open("users.csv", mode='w', newline='') as f:
    fieldnames = ['first_name', 'last_name', 'email', 'password', 'phone_number', 'dob', 'city', 'province', 'play_status', 'last_time_played']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()



def register_user(first_name, last_name, email, password, phone_number, dob, city, province, last_time_played="never played"):
    with open("users.csv", mode="a", newline="") as f:
        register_writer = csv.writer(f, delimiter=",") # writes to the csv file
        register_writer.writerow([first_name, last_name, email, password, phone_number, dob, city, province])
        print("Registration is successful")
        return first_name, last_name, province, last_time_played
       

# register_user(first_name="Hellen", last_name="Adeniyi", email="hellenadeniyi29@gmail.com", password="jord", phone_number="6392954157", dob="05/25/2005", city="saskatoon", province="saskatchewan")


    
def confirm_user(email, password):
    with open('users.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['email'] == email:
                if row['password'] == password:
                    # Correct email and password
                    print("welcome !!!")
                    return {
                        'First Name': row['first_name'],
                        'Last Name': row['last_name'],
                        'Email': row['email'],
                        'City': row['city'],
                        # 'Last Time Played': row['Last Play Timestamp']
                    }
                else:
                    # Incorrect password
                    print("Incorect password !!!")
                    return 'Incorrect password'

    # Email not found in users.csv
    print("User does not exist !")
    return "User does not exist, sign up instead"



# confirm_user(email="hellenadeniyi29@gmail.com", password='jord')

def check_play_status(email):
    """
    Purpose: To check the play status of a player, a player can play only once in 24 hours
        Need to check if they are signed in first, if they are not they need to sign in and if they are
        the function proceeds to check 
        if they have played in the last 24 hours.
        If they have, they cannot play, they  have to wait.
        If they havent, they can play
        If they have never played, they can play

    Pre-conditions: email
    Post-conditions: none
    return: 1 for the satus of can play and 0 if player cannot play yet 
    """
    last_time_played="never played"
    play_status = 0
    password = password
    if confirm_user(email, password) != "User does not exist, sign up instead":
        return "You need to Sign Up first"
        # check if they have never played
    elif last_time_played =="never played":
        play_status = 1
    elif last_time_played < 


    # 
    

    


def get_remaining_time():
    """
    
    """
    pass

def get_gift():
    pass

def send_loosing_email():
    pass

def shuffle_gifts():
    """
    
    """
    pass

# update last time played only if users can play

def send_email_to_nick():
    """
    
    """
    pass














