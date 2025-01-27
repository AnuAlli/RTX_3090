# RTX 3090 Price Tracker

## Overview
RTX 3090 Price Tracker is a web scraping tool designed to monitor and track the prices of NVIDIA RTX 3090 graphics cards on eBay. The program automatically scans eBay listings at customizable intervals and sends real-time text message notifications using Twilio API when listings matching your criteria are found.

## Features
- Automated eBay scanning every 3 seconds (customizable interval)
- Real-time SMS notifications via Twilio
- Customizable price thresholds
- Condition-based filtering
- Direct eBay listing links in notifications
- Support for:
  - New listings
  - Used listings
  - Price ranges
  - Multiple search criteria

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Twilio account (for SMS notifications)
- Chrome/Firefox web browser

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/RTX_3090.git
cd RTX_3090
```
2. Install required packages
```bash
pip install -r requirements.txt
 ```

3. Configure Twilio
- Copy .env.example to .env
- Add your Twilio credentials to .env
- Set your phone number for notifications
## Configuration
### Price and Condition Settings
Edit config.yml to set your preferences:

```yaml
search_criteria:
  max_price: 2000
  min_price: 1000
  condition: ["new", "used"]
  
scan_interval: 3  # Scanning interval in seconds
 ```
```

### Twilio Setup
1. Sign up for a Twilio account
2. Get your Account SID and Auth Token
3. Add them to your .env file
4. Add your phone number to receive notifications
## Usage
1. Start the price tracker:
```bash
python main.py
 ```

The program will:

- Scan eBay every 3 seconds (configurable)
- Check for RTX 3090 listings matching your criteria
- Send SMS notifications for new matches
- Include direct eBay listing links in messages
## Notifications
You'll receive SMS notifications containing:

- Item price
- Condition
- Direct link to listing
- Basic item description
## Important Notes
- Adjust scanning intervals responsibly
- Respect eBay's terms of service
- Keep your Twilio credentials secure
```plaintex
This update includes clear information about the interval scanning feature and Twilio integration. Would you like me to add or modify any other sections?```