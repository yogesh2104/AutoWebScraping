# first we need to install autoscraper package
# !pip install autoscraper

from autoscraper import AutoScraper

# paste the link which you want to search on amazon or flipkart etc link should be the string 
# format

url = "https://www.amazon.in/s?k=iphone"
''' here i am searching iphone on amazon
    after the link make a list what you want to scrape
    like price, rating, discount etc.
'''
wanted_list = ["New Apple iPhone 12 (128GB) - Blue","3,119","4,670","80,230"]
# in wnated list you can select any one product and grouped them into list

scraper = AutoScraper()

# result = scraper.build(url, wanted_list)
# print(result)

# print(help(scraper.get_result_similar))

scraper.set_rule_aliases({'rule_wnb2':"Title"})
scraper.keep_rules(['rule_wnb2'])
scraper.save('amazon-search')


result = scraper.get_result_similar("https://www.amazon.in/s?k=realme+phones&rh=n%3A1389432031%2Cp_89%3Arealme&dc&qid=1623875809&rnid=3837712031&ref=sr_nr_p_89_1",group_by_alias=True)
result['Title']
print(result)
