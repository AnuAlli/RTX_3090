import os
import time
import logging
from datetime import datetime
from typing import Dict, List

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler
from sqlalchemy import create_engine, Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)

# Database setup
Base = declarative_base()

class Listing(Base):
    __tablename__ = 'listings'
    
    id = Column(String, primary_key=True)
    title = Column(String)
    price = Column(Float)
    link = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# Initialize database
engine = create_engine('sqlite:///listings.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class EbayScraperBot:
    def __init__(self):
        self.search_url = "https://www.ebay.com/sch/i.html?_nkw=rtx+3090&LH_BIN=1&_sop=15"
        self.session = requests.Session()
        self.ua = UserAgent()
        self.db_session = Session()
        
        # Twilio setup
        self.twilio_client = Client(
            os.getenv('TWILIO_ACCOUNT_SID'),
            os.getenv('TWILIO_AUTH_TOKEN')
        )
        self.twilio_from = os.getenv('TWILIO_FROM_NUMBER')
        self.twilio_to = os.getenv('TWILIO_TO_NUMBER')
    
    def get_headers(self) -> Dict:
        """Generate random headers for requests"""
        return {
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }
    
    def parse_price(self, price_str: str) -> float:
        """Convert price string to float"""
        try:
            return float(price_str.replace('$', '').replace(',', '').strip())
        except ValueError:
            return float('inf')
    
    def scrape_listings(self) -> List[Dict]:
        """Scrape RTX 3090 listings from eBay"""
        try:
            response = self.session.get(
                self.search_url,
                headers=self.get_headers(),
                timeout=30
            )
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'lxml')
            items = soup.select('.s-item')
            
            listings = []
            for item in items:
                title_elem = item.select_one('.s-item__title')
                price_elem = item.select_one('.s-item__price')
                link_elem = item.select_one('.s-item__link')
                
                if not all([title_elem, price_elem, link_elem]):
                    continue
                
                price = self.parse_price(price_elem.text)
                if price >= 900:
                    continue
                
                listings.append({
                    'id': link_elem['href'].split('itm/')[-1].split('?')[0],
                    'title': title_elem.text,
                    'price': price,
                    'link': link_elem['href']
                })
            
            return listings
        
        except Exception as e:
            logging.error(f'Error scraping listings: {str(e)}')
            return []
    
    def send_sms_alert(self, listing: Dict) -> None:
        """Send SMS alert for new listing"""
        try:
            message = f"New RTX 3090 Deal!\n{listing['title']}\nPrice: ${listing['price']}\nLink: {listing['link']}"
            
            self.twilio_client.messages.create(
                body=message,
                from_=self.twilio_from,
                to=self.twilio_to
            )
            
            logging.info(f"SMS alert sent for listing {listing['id']}")
        
        except Exception as e:
            logging.error(f'Error sending SMS: {str(e)}')
    
    def process_listings(self) -> None:
        """Process new listings and send alerts"""
        listings = self.scrape_listings()
        
        for listing in listings:
            # Check if listing already exists in database
            existing = self.db_session.query(Listing).filter_by(id=listing['id']).first()
            if existing:
                continue
            
            # Add new listing to database
            new_listing = Listing(**listing)
            self.db_session.add(new_listing)
            
            # Send SMS alert
            self.send_sms_alert(listing)
        
        self.db_session.commit()
    
    def run(self) -> None:
        """Run the scraper with scheduling"""
        logging.info('Starting eBay RTX 3090 Scraper Bot')
        
        scheduler = BlockingScheduler()
        scheduler.add_job(self.process_listings, 'interval', seconds=3)
        
        try:
            scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            logging.info('Stopping scraper bot')
            self.db_session.close()

if __name__ == '__main__':
    bot = EbayScraperBot()
    # Send test message first
    test_listing = {
        'id': 'test',
        'title': 'Test Message',
        'price': 0.0,
        'link': 'https://www.ebay.com'
    }
    bot.send_sms_alert(test_listing)
    logging.info('Test message sent. Starting the bot...')
    bot.run()