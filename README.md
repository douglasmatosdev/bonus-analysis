# bonus-analysis
Application that consumes databases in Excel spreadsheet format, and analyzes the data in order to find the employee who sold the most, when found an SMS will be sent.

### Dependencies
- pandas
- openpyxl
- twilio
- python-dotenv

### Install dependencies
```bash
pip install pandas openpyxl twilio python-dotenv
```

### Create Twilio account
https://www.twilio.com/

### Create `.env` file
```txt
// .env
ACCOUNT_SID='YOUR TWILIO ACCOUNT SID'
AUTH_TOKEN='YOUR TWILIO AUTH TOKEN'
TWILIO_PHONE_NUMBER='YOUR TWILIO PHONE NUMBER'
MY_PHONE_NUMBER='PHONE NUMBER TO SEN MESSAGE'
```
