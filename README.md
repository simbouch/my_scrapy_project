# my_scrapy_project
 
📌 Overview
This project uses Scrapy to scrape book data from Books to Scrape and saves the extracted information in a CSV file.

🚀 Features
✅ Scrapes book title, price, availability, and image URL
✅ Handles pagination to scrape all pages
✅ Saves data into a CSV file

🛠 Setup & Usage
1️⃣ Install Dependencies
bash
Copy
Edit
pip install scrapy
2️⃣ Run the Scraper
bash
Copy
Edit
scrapy crawl books -o books.csv
📁 Extracted Data Format
Title	Price	Availability	Image URL
Example Book	£10.99	In stock	http://image-url.jpg
