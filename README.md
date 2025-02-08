# RTX 3090 Price Tracker

![image](https://github.com/user-attachments/assets/1fdf49e7-9de3-4847-a411-28b0e7d3ebdc)


## Project Background
With the rapid advancement of AI technology and the increasing demand for computational power, building a personal AI server has become more accessible. However, sourcing current-generation graphics cards at reasonable prices remains a significant challenge. This project was born from the need to find more affordable alternatives like the RTX 3090.


## Motivation
Manual monitoring of eBay listings is time-consuming and inefficient. This automated solution eliminates the need for constant manual checks by:
- Continuously monitoring eBay listings 24/7
- Sending instant notifications for matching deals
- Providing quick access to purchase opportunities
- Saving valuable time and effort in the GPU hunt

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

### Twilio Setup
1. Sign up for a Twilio account
2. Get your Account SID and Auth Token
3. Add them to your .env file
4. Add your phone number to receive notifications

![image](https://github.com/user-attachments/assets/41a1564a-77c0-4c16-b41f-0fc3a7dc7e7b)
![image](https://github.com/user-attachments/assets/72c4f8ac-a66d-4e26-80ff-3d5a0235a6da)
![image](https://github.com/user-attachments/assets/6970bfef-ab4d-4171-b091-470f07fa3ef2)








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

## ![SMS Notification Example]
![image](https://github.com/user-attachments/assets/1a916a76-387f-4727-9889-f90eac8a2c70)
![image](https://github.com/user-attachments/assets/0efef421-9c2a-401a-b064-44d2cab23ed9)






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

## Customization & Extensibility

This tool is highly customizable and can be adapted for various use cases:

### Different Products
The scraper can be modified to track any product on eBay, not just RTX 3090 cards. For example:
- Other GPU models (RTX 4090, RX 6900 XT, etc.)
- Gaming consoles
- Collectibles
- Any other eBay-listed items

### Different Marketplaces
While currently configured for eBay, the core functionality can be adapted for other e-commerce platforms:
- Amazon
- Best Buy
- Newegg
- Local marketplace websites

### Customizable Features
The script's modular design allows for easy modifications:
```python
# Example of modifying search criteria in ebay_scraper.py
SEARCH_TERMS = ["your-product-name"]  # Change what to search for
MAX_PRICE = 1500  # Adjust price threshold
REFRESH_INTERVAL = 5  # Modify scanning frequency
```

### Extended Functionality
You can enhance the tool by adding:
- Multiple marketplace monitoring
- Price history tracking
- Email notifications
- Discord bot integration
- Custom filtering logic
- Data analytics features

Check out the `ebay_scraper.py` file for the core scraping logic that you can modify according to your needs.

## Screenshots

The image below is just a visual representation of the program 
running successfully.

![image](https://github.com/user-attachments/assets/29127807-c03e-461c-8763-c4dad52d0947)


### Dashboard View
![image](https://github.com/user-attachments/assets/fc7712d7-2c86-4639-a62e-7097bcc0a10b)
![image](https://github.com/user-attachments/assets/3c71c431-17d5-42d2-9fe0-89d9a834a84c)



## Success Stories
Users have reported finding RTX 3090 cards at 20-30% below market prices using this tool. The instant notifications give you a competitive advantage in securing the best deals.


## Contact & Support
For questions, feature requests, or bug reports, please:
- Open an issue on GitHub
- Contact me directly at [anuajimafowoku@gmail.com]
- Join our Discord community [link]

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
