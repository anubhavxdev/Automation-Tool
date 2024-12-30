import os
from dotenv import load_dotenv
from twilio.rest import Client
from datetime import datetime, timedelta
import time


load_dotenv()
account_sid = os.getenv("Account_SID")
auth_token = os.getenv("Auth_Token")


client = Client(account_sid, auth_token)

def send_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f"Message sent successfully. Message SID: {message.sid}")
    except Exception as e:
        print(f"Error occurred: {e}")


name = input("Enter the recipient name: ")
recipient_number = input("Enter the recipient number with country code: ")
message_body = input(f"Enter the message you want to send to {name}: ")

date_str = input("Enter the date you want to send the message in format (YYYY-MM-DD): ")
time_str = input("Enter the time you want to send the message in format (HH:MM): ")


schedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
current_datetime = datetime.now()
time_diff = schedule_datetime - current_datetime
delay_seconds = time_diff.total_seconds()

if delay_seconds <= 0:
    print("The specified time is in the past. Please enter a valid time in the future.")
else:
    print(f"Message will be sent to {name} on {date_str} at {schedule_datetime}.")
    time.sleep(delay_seconds)  
    send_message(recipient_number, message_body)
