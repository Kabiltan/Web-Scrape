from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import numpy as np


#Creates CSV file
filename ="MoreRestaurants.csv"
f = open(filename, "w")
headers = "Restaurant Name, Number of Reviews, Rating\n"

f.write(headers) # Writes headers to CSV file

pages = np.arange(0, 780, 30) # Each page has 30 restuarants so increment to 780 in spaces of 30

for page in pages:


	restaurant_url = 'https://www.tripadvisor.com/RestaurantSearch?Action=PAGE&ajax=1&availSearchEnabled=false&sortOrder=popularity&geo=60859&itags=10591&o=a' + str(page)
		                  

	#Open up site
	uClient = uReq(restaurant_url)
	page_html = uClient.read()
	uClient.close()

	#HTML Parsing
	page_soup = soup(page_html, "html.parser")


	#Find each container
	restaurant_container = page_soup.findAll('div' , {'class' : '_1llCuDZj'})

	for container in restaurant_container:
		extraText = container.find("a", "_15_ydu6b") # Gets h6 tag with restaurant name
		textInHeader = extraText.text # Takes just the text in h6
		split = textInHeader.split(". ") # Splits text to get just the name of the restaurant
		if(len(split) > 2): # Stores name of restaurant in variable
			actualNameOfRestaurant = split[1] + split[2]
		elif(len(split) > 1):
			actualNameOfRestaurant = split[1]
		else:
			actualNameOfRestaurant = split[0]	

		container2 = container.find("svg", "_3KcXyP0F") # Gets a svg tag with actual rating 
		container3 = container2["aria-label"] # Gets the aria-label attribute within the svg tag
		container4 = container3.split(" of") # Splits rating into just the rating number and other text
		actualRating = container4[0] # Stores just the rating value
		

		ratingNumber = container.find("span", "w726Ki5B") # Gets the span tag with the number of reviews
		ratingText = ratingNumber.text  # Takes just the text in span
		ratingTextSplit = ratingText.split(" ") # Splits text to get just the number of reviews
		realReviewText = ratingTextSplit[0] # Stores just the number of reviews 

		print("Name: " + actualNameOfRestaurant) # Prints results to console 
		print("Number of Reviews: " + realReviewText)
		print("Rating: " + actualRating)

		f.write(actualNameOfRestaurant + "," + realReviewText.replace(",", "") + "," + actualRating + "\n") # Writes to CSV file

f.close()