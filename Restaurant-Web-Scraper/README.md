This files contains a two python scripts for extracting the name, number of reviews, and rating for each restaurant from a website.

For Restaurant_Scraper.py:
The data was extracted from the following website:
https://www.opentable.com/nearby/restaurants-near-me-madison?prices=&cuisines=&corrid=4744de3d-be10-4790-a45e-da353493ad8c&page=1
The data is stored in Restaurants.csv


For Large_Restaurant_Scraper.py:
The data was extracted from the following website:
https://www.tripadvisor.com/Restaurants-g60859-Madison_Wisconsin.html
The data is stored in MoreRestaurants.csv

Large_Restaurants_Scraper.py is similar to Restaurants_Scraper.py except it operates on a much larger data set (72 restaurants compared to 694 restaurants).
BeautifulSoup was the python library used to parse html in both scripts.
