from django.db import models
from django.utils import timezone
import json

# Read file 
#f = open('path_to_file.json')
#json_string = f.read()
#f.close()

# Convert json string to python object
#import json
#data = json.loads(json_string)

# Create model instances for each item
#items = []
#for item in data:
   # create model instances...
#   item = Ticket(*item)
 #  items.append(item)

# Create all in one query
#Tickets.objects.bulk_create(items)

class Ticket(models.Model):
    user_id = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)


class RaffleWinner(models.Model):

	# unique identifier for tweet
    tweet_id = models.CharField(max_length=200)

    # store win date so that tweet can win raffle again after specific time period
    win_date = models.DateTimeField(default=timezone.now) 

def __str__(self):
    return self.title    

