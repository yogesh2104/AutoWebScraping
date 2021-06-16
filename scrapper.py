# first we need to install autoscraper package
# !pip install autoscraper

from autoscraper import AutoScraper

# paste the link which you want to search on amazon or flipkart etc link should be the string 
# format

url = "https://www.amazon.in/s?k=laptop"
''' here i am searching laptop on amazon
    after the link make a list what you want to scrape
    like price, rating, discount etc.
'''
wanted_list = ["ASUS VivoBook 14 (2020) Intel Quad Core Pentium Silver N5030, 14-inch (35.56 cms) FHD Thin and Light Laptop (4GB RAM/1TB HDD/Windows 10/Integrated Graphics/Transparent Silver/1.5 Kg), X415MA-EK101T","185","24,990","7,000"]
# in wnated list you can select any one product and grouped them into list

# scraper = AutoScraper()
# result = scraper.build(url, wanted_list)
# print(result)

