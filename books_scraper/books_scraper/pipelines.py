import csv

class SaveToCSV:
    def open_spider(self, spider):
        """Initializes the CSV file and writes the header row."""
        self.file = open("books.csv", "w", newline="", encoding="utf-8")
        self.writer = csv.writer(self.file)
        self.writer.writerow(["Title", "Price", "Availability", "Image URL"])  # Column names

    def process_item(self, item, spider):
        """Writes book data into the CSV file."""
        self.writer.writerow([item["title"], item["price"], item["availability"], item["image_url"]])
        return item

    def close_spider(self, spider):
        """Closes the CSV file when the spider is done."""
        self.file.close()
