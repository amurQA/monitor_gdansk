# Monitor gdansk

Monitor_Gdansk is a minimal viable product (MVP) for monitoring available dates and time slots for applying for Karta Pobuty in Gdansk, Poland. It periodically checks for available dates & times and sends notifications to a Telegram channel if there are any dates in the next 2 months.

# Prerequisites
Python 3.7 or higher
Required packages are listed in requirements.txt. Install them using the command: 

# pip install -r requirements.txt

# Getting Started

* Clone the repository: git clone https://github.com/amurQA/monitor_gdansk.git
* Change to the project directory: cd monitor_gdansk
* Install the required packages: pip install -r requirements.txt

# Configuration

Open main.py and provide your Telegram bot token, interval and channel ID in the respective fields at "main" function.

# Usage

Run the script: python main.py
The script will start monitoring for available dates and time slots.
If any dates or slots are found in the next 2 months, a notification will be sent to the configured Telegram channel.

# Contributing

Contributions to Monitor Gdansk are welcome! If you find a bug or have an idea for an improvement, please open an issue or submit a pull request.
