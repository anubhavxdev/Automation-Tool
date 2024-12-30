# WhatsApp Message Scheduler

This project allows you to schedule WhatsApp messages to be sent at a specified date and time using the Twilio API.

## Prerequisites

- Python 3.x
- Twilio account
- Twilio phone number
- `python-dotenv` package

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/whatsapp-message-scheduler.git
    cd whatsapp-message-scheduler
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a [.env](http://_vscodecontentref_/0) file in the project directory and add your Twilio account SID and auth token:

    ```plaintext
    ACCOUNT_SID=your_account_sid_here
    AUTH_TOKEN=your_auth_token_here
    ```

## Usage

1. Run the script:

    ```bash
    python main.py
    ```

2. Follow the prompts to enter the recipient's name, phone number, message, and the date and time to send the message.

## Example

```plaintext
Enter the recipient name: John Doe
Enter the recipient number with country code: +1234567890
Enter the message you want to send to John Doe: Hello, this is a scheduled message!
Enter the date you want to send the message in format (YYYY-MM-DD): 2023-12-31
Enter the time you want to send the message in format (HH:MM): 23:59
Message will be sent to John Doe on 2023-12-31 at 2023-12-31 23:59:00.
```

License
This project is licensed under the MIT License.

```

Make sure to replace `yourusername` with your actual GitHub username and `your_account_sid_here` and `your_auth_token_here` with your actual Twilio credentials.
Make sure to replace `yourusername` with your actual GitHub username and `your_account_sid_here` and `your_auth_token_here` with your actual Twilio credentials.
'''
