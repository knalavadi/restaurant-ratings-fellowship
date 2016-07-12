# # your code goes here
# open scores.txt
# initialize empty dictionary
# read split scores to get rid of newlines
# outputs list of restaurant score, restaurant score, etc
# split again over ":" to get key value pairs separated

# for loop
# if index of split_list is 0 or index % 2 == 0, that is a key

# dict[key] = split_list[key + 1] 
# then sort based on key
# close file
# print dict
# call function

from operator import itemgetter

def alphabetize_dict(filename):
    """ print alpabetized restaurants with score"""

    file_to_parse = open(filename)

    restaurants_scores = {}

    for file_line in file_to_parse:
        # NOTE: rsplit() should have worked in place of replace
        entry = file_line.replace("\n", "")
        restaurant_name = entry.split(":")

        restaurant, score = restaurant_name
        
        restaurants_scores[restaurant] = score

    itemized_restaurants_scores = restaurants_scores.items()

    sorted_restaurants_scores = sorted(itemized_restaurants_scores,key = itemgetter(0))

    for restaurant, score in sorted_restaurants_scores:
        print "{} is rated at {}".format(restaurant, score)      

    file_to_parse.close()

alphabetize_dict("scores.txt")
