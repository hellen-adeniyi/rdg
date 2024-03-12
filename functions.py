import csv
from datetime import datetime, timedelta


with open("users.csv", mode='w', newline='') as f:
    fieldnames = ['first_name', 'last_name', 'email', 'password', 'phone_number', 'dob', 'city', 'province', 'play_status', 'last_time_played']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()


# sign up
def register_user(first_name, last_name, email, password, phone_number, dob, city, province, last_time_played="never played"):
    with open("users.csv", mode="a", newline="") as f:
        register_writer = csv.writer(f, delimiter=",") # writes to the csv file
        register_writer.writerow([first_name, last_name, email, password, phone_number, dob, city, province])
        print("Registration is successful")
        return first_name, last_name, province, last_time_played
       

# register_user(first_name="Hellen", last_name="Adeniyi", email="hellenadeniyi29@gmail.com", password="jord", phone_number="6392954157", dob="05/25/2005", city="saskatoon", province="saskatchewan")


    # sign in 
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

def read_player_from_csv(csv_filename):
    """
    This function reads player data from csv file and returns a dictionary with email as the key

    """
    csv_filename = "users_2.csv"
    player_data = {}
    with open(csv_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email = row["email"]
            player_data[email] = {"last_played": row["last_time_played"], 
                                  "play_status": int(row["play_status"]),}
            return player_data
        



def write_player_data_to_csv(csv_filename, player_data):
    """
    Writes player data back to the CSV file
    """
    with open(csv_filename, "w", newline="") as csvfile:
        fieldnames = ["first_name", "last_name", "email", "password", "phone_number", "dob", "city", "province", "play_status", "last_time_played"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for email, data in player_data.items():
            writer.writerow({
                "email": email,
                "last_time_played": data["last_played"],
                "play_status": data["play_status"],
            })





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
    player_data = read_player_from_csv(csv_filename="users.csv")
    if email in player_data:
        last_played_time = player_data[email]["last_played"]
        if last_played_time:
            # player has  played before
            current_time = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            last_played_datetime = datetime.strptime(last_played_time, "%m-%d-%Y %H:%M:%S")
            elapsed_time = (datetime.strptime(current_time, "%m-%d-%Y %H:%M:%S")-last_played_datetime).total_seconds()
            if elapsed_time < 24*60*60:
                #less than 24 hours, player cannot play yet
                return 0
            # player hasnt played or its been more than 24 hours
            # update last_played time to current time
            player_data[email]["last_played"] = current_time
            write_player_data_to_csv(csv_filename="users.csv", player_data)

            return 1
    else:
        #player is not signed in
        # Implement sign in logic here (prompt user to sign in)
        confirm_user(email, password=password)
        return 0 


     
    

    


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














