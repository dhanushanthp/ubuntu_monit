#!/usr/bin/env python
import sys
from slacker import Slacker

def update_slack(user, channel, message, slack):
    slack.chat.post_message('#%s' % channel, message, username=user)

if __name__ == "__main__":
	if len(sys.argv) > 2:
		user = sys.argv[1]
		channel = sys.argv[2]
		message = sys.argv[3]
		slack = Slacker(sys.argv[4])
		update_slack(user, channel, message, slack)
	else:
		print "Please run the script with <user> <Channel> <Message> <Slack Token>arguments"
