import smtplib
import requests
import time

MY_GMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_app_password"

def position():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    print(f"ISS Position: ({latitude}, {longitude})")

    my_latitude = 29.53
    my_longitude = 76.61

    if (my_latitude - 5 <= latitude <= my_latitude + 5) and (my_longitude - 5 <= longitude <= my_longitude + 5):
        return True
    return False

while True:
    if position():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_GMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_GMAIL,
                to_addrs="Singhjigerjeet039@gmail.com",
                msg="Subject:Look Up!\n\nHEY!!!!\n\nSee in the sky—there's the ISS space station!"
            )
        print("Email sent!")
    time.sleep(60)
