# TheOrBotFan

import praw

# create the objects from the imported modules

# reddit api login
reddit = praw.Reddit(client_id='RV7Pwgsf_9wKLw',
                     client_secret='HA4ehmKBhXPCsjUHZwQGeQ4Q8mU',
                     username='TheOrBotFanBot',
                     password='g0g0g0banana',
                     user_agent="TheOrBot's #1 fan Bot")

# the subreddits you want your bot to live on
subreddit = reddit.subreddit('JustBlackMetalThings')

# phrase to activate the bot
tie = 'we tied, I got:'
win = 'I won, I got:'
lose = 'I lost, I got:'

# look for phrase and reply appropriately
for comment in subreddit.stream.comments():
    if tie in comment.body:
      print('great effort')
    else:
      if win in comment.body:
          print('proud of u')
        else:
          if lose in comment.body:
            print("that's okay you'll get better don't worry")
        
