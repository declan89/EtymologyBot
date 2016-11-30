import time, praw, json, WordFrequency, pprint, OAuth2Util

# Change to 'None' for continuous tracking
countLimit = None
subreddit = 'all'
already_done_text = 'already_done.txt'
already_done=[]
CLIENT_ID = 'FJT8Xw6bluRwsg'
CLIENT_SECRET = 'SEpjNE4ynxRw9Uf7JwSIduiPiuI'

def get_already_done():
	with open(already_done_text) as file:
		return [line.rstrip('\n') for line in file.readlines()]

def update_already_done(comment):
	already_done.append(comment.id)
	with open(already_done_text, 'w') as file:
		for item in already_done:
			file.write("%s\n" % item)


def bot_action(wordMatch, comment, verbose=True, respond=False):
	if verbose:
		pprint.pprint(wordMatch[0]['Word'].encode('utf-8') + ': http://www.Reddit.com/comments/' + c.link_id.encode('utf-8').lstrip('t3_') + '/_/' + c.id.encode('utf-8')) 
	if respond:
		commentReply = (wordMatch[0]['Word'].encode('utf-8') +
			"\n\nDefinition: " + wordMatch[0]['Definition'].encode('utf-8') +
			"\n\nEtymology: " + wordMatch[0]['Etymology'].encode('utf-8'))

        c.reply(commentReply)
	
UA = 'Script to detail a few etymologies; trying to get people interested in words. Contact me at /u/Decuran'

r = praw.Reddit(user_agent='decuran',
                     client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET)
# o = OAuth2Util.OAuth2Util(r)
already_done = get_already_done()

print ('Successfully logged in as ' + str(r.user.me))
while True:
	try:
		for c in praw.helpers.comment_stream(r, subreddit, limit=countLimit):
			text = c.body
			tokens = text.split()
			wordMatch = WordFrequency.findInPersonalWordList(tokens)
			if (wordMatch and not c.author == r.user.me and c.id not in already_done):
				update_already_done(c)
				bot_action(wordMatch, c, respond=True)
	except praw.execptions.RateLimitExceeded as e:
		print('Rate limit exceeded: ' + str(e))
	time.sleep(360)


		
		