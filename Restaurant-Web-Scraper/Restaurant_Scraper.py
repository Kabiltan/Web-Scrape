from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

pages = [1, 2, 3, 4, 5, 6, 7, 8] 

filename ="Restaurants.csv"
f = open(filename, "w")
headers = "Restaurant Name, Number of Reviews, Rating\n"

f.write(headers)

for number in pages: 
	restaurant_url = 'https://www.opentable.com/nearby/restaurants-near-me-madison?prices=&cuisines=&corrid=6a19c0ad-0f5d-4346-8411-abef95c94dc2&page=' + str(number)
	                  

	# Get permission to open URL


	#Open up site
	uClient = uReq(restaurant_url)
	page_html = uClient.read()
	uClient.close()

	#HTML Parsing
	page_soup = soup(page_html, "html.parser")

	#Find each container
	restaurant_container = page_soup.findAll('div' , {'class' : '_3uVfVbI1iLfMbszbU6KoOL'})

	for container in restaurant_container:
		extraText = container.find("h6", "k8o46Bca35RzHNtQFy3bH") # Gets h6 tag with restaurant name
		textInHeader = extraText.text # Takes just the text in h6
		split = textInHeader.split(". ") # Splits text to get just the name of the restaurant
		actualNameOfRestaurant = split[1] # Stores name of restaurant in variable

		reviewNumber = container.find("a", "_37NqKSTDkDYtsJrAU287ai") # Gets a tag with number of reviews	
		reviewText = reviewNumber.text # Gets the text with the number of reviews
		realReviewText = reviewText.translate(str.maketrans({'(': '', ')': ''})) # Removes the parentheses characters

		ratingNumber = container.find("div", "_2s6ofZ_eiTKuvNHV3mVnaG") # Gets the div container with the rating
		actualRating = ratingNumber.text # Gets the text which is the actual rating

		print("Name: " + actualNameOfRestaurant)
		print("Number of Reviews: " + realReviewText)
		print("Rating: " + actualRating)

		f.write(actualNameOfRestaurant + "," + realReviewText + "," + actualRating + "\n")

f.close()