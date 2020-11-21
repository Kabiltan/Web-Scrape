from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import numpy as np



filename ="MoreRestaurants.csv"
f = open(filename, "w")
headers = "Restaurant Name, Number of Reviews, Rating\n"

f.write(headers)

pages = np.arange(0, 780, 30)

for page in pages:


	restaurant_url = 'https://www.tripadvisor.com/RestaurantSearch?Action=PAGE&ajax=1&availSearchEnabled=false&sortOrder=popularity&geo=60859&itags=10591&o=a' + str(page)
		                  

	#Open up site
	uClient = uReq(restaurant_url)
	page_html = uClient.read()
	uClient.close()

	#HTML Parsing
	page_soup = soup(page_html, "html.parser")

	#HTML Parsing


	#Find each container
	restaurant_container = page_soup.findAll('div' , {'class' : '_1llCuDZj'})

	for container in restaurant_container:
		extraText = container.find("a", "_15_ydu6b") # Gets h6 tag with restaurant name
		textInHeader = extraText.text # Takes just the text in h6
		split = textInHeader.split(". ") # Splits text to get just the name of the restaurant
		if(len(split) > 2):
			actualNameOfRestaurant = split[1] + split[2]# Stores name of restaurant in variable
		elif(len(split) > 1):
			actualNameOfRestaurant = split[1]
		else:
			actualNameOfRestaurant = split[0]	

		container2 = container.find("svg", "_3KcXyP0F") # Gets a tag with actual rating 
		container3 = container2["aria-label"]
		container4 = container3.split(" of")
		actualRating = container4[0]	
		

		ratingNumber = container.find("span", "w726Ki5B") # Gets the div container with the rating
		ratingText = ratingNumber.text # Gets the text which is the actual rating
		ratingTextSplit = ratingText.split(" ")
		realReviewText = ratingTextSplit[0]

		print("Name: " + actualNameOfRestaurant)
		print("Number of Reviews: " + realReviewText)
		print("Rating: " + actualRating)

		f.write(actualNameOfRestaurant + "," + realReviewText.replace(",", "") + "," + actualRating + "\n")

f.close()