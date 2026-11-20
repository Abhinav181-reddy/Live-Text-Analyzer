import re

# Sample text
text = """
Contact: abhinav@gmail.com
Phone: 9876543210
Website: https://example.com
Price: ₹4,999
Date: 20-11-2026
"""

# Extract email addresses
emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

# Extract phone numbers
phones = re.findall(r'\b[6-9]\d{9}\b', text)

# Extract URLs
urls = re.findall(r'https?://\S+', text)

# Extract prices
prices = re.findall(r'[₹$]\s?[\d,]+(?:\.\d{1,2})?', text)

# Extract dates
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)

print("Emails:", emails)
print("Phone numbers:", phones)
print("URLs:", urls)
print("Prices:", prices)
print("Dates:", dates)