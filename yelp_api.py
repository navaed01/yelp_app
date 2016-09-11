

#Yelp example but adding dictionary

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())




def get(place):
	params = {
    'term': 'food',
    'lang': 'en',
    'limit': 3,
    'sort': 2
	}
	auth = Oauth1Authenticator(
    consumer_key=os.environ['CONSUMER_KEY'],
    consumer_secret=os.environ['CONSUMER_SECRET'],
    token=os.environ['TOKEN'],
    token_secret=os.environ['TOKEN_SECRET']
	)
	client = Client(auth)
	response = client.search(place, **params)
	businesses = [] 									
	for business in response.businesses: 			
		
		#here you are making the dictionary. You are nameing the fields that you want the data put into e.g. "name" but you can call it anything, sinc you are defining it. 
		businesses.append({"name": business.name, 
			"rating": business.rating,
			"phone": business.phone,
			"pic": business.image_url,

		}) 				
	
	return businesses					


