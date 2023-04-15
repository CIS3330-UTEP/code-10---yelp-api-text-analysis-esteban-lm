from yelpapi import YelpAPI
import pandas as pd

api_key = 'jv730cgOE1UCjdhDt5I9A1MGKE7ntdXDQnB-oXo2eOnDikN-qAB2CmCv1kzGirTsFR9C1UKbOohXgHi_6yv-QfdcKd6qHr_IdywfQk6sYIM89sTRJjPE7F3PKBUZZHYx'

yelp_api = YelpAPI(api_key)

#search query 
 
search_term = 'pizza'
search_location = 'Chicago, IL'
search_sort_by = 'rating' #best_match, rating, review_count, distance
search_limit = 20

search_results = yelp_api.search_query(term=search_term,location=search_location,sort_by=search_sort_by,limit=search_limit)

print(search_results)
'''
for business in search_results['businesses']:
    print(business['name'])
'''
result_df = pd.DataFrame.from_dict(search_results['businesses'])
print(result_df['alias'])

id_for_reviews = 'montis-chicago'

#reviews result

reviews_result = yelp_api.reviews_query(id=id_for_reviews)
print(reviews_result)

'''
for review in reviews_result['reviews']:
'''

reviews_df = pd.DataFrame.from_dict(reviews_result['reviews'])
print(reviews_df['text'])