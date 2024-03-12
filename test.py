from functions import register_user

expected_result = register_user(first_name="Hellen", last_name="Adeniyi", email="hellenadeniyi29@gmail.com", password="jord", phone_number="6392954157", dob="05/25/2005", city="saskatoon", province="saskatchewan")
actual_result = "Registration is successful"
if expected_result != actual_result:
    print("Test case 1 failed")
    


read_player_data_from_csv(csvfilename)