import random
from models import RaffleWinner
from datetime import datetime, timedelta
from django.utils import timezone


class Raffle:

	def __init__(self, users):
		self.tweeters = users


	# Return whether or not the tweet id has recently won 
	def hasWonBefore(self, tweetID):
		for raffleWinner in RaffleWinner.objects.all():
			#print raffleWinner.win_date, raffleWinner.tweet_id
			if raffleWinner.tweet_id == tweetID:
				return True

		return False


	# delete entries older than the specified number of hours
	def deleteOldEntries(self, numberOfHours):
		RaffleWinner.objects.filter(win_date__lte=datetime.now()-timedelta(hours=numberOfHours)).delete()


	# Generate a winner from the tweets that included the specified hashtag and add them to the
	# database of winning tweets so they don't win again too quickly, this database will be used
	# to compare new winners with tweets that already won to make sure this tweet hasn't won
	# too recently 
	# Return the name of the winner who tweeted the chosen tweet
	def generateRaffle(self):

		# delete winners from over 1 hour ago so they're eligible to win again
		self.deleteOldEntries(1)

		# get list of tweet ids
		userIDs = list(self.tweeters)

		# pick a winner id at random
		winnerID = random.choice(userIDs)

		# keep picking a winner id at random until you get a person that hasn't won
		while self.hasWonBefore(winnerID):
			winnerID = random.choice(userIDs)

		# get the name associated with the winner id
		winnerName = self.tweeters[winnerID]

		# remove the raffle winner from the list of contestants
		del self.tweeters[winnerID]

		# save a reference to the
		p = RaffleWinner(tweet_id=winnerID)
		p.save()

		return winnerName