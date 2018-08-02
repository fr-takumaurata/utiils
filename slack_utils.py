# -*- coding: utf-8 -*-
"""
@author: fr-takumaurata
@brief: utils for slack notify
@setting: set webhook url to your enviroment value
@reference: 
https://api.slack.com/incoming-webhooks

@example:
-------------------
import slack_utils
with slack_utils._notify('YOUR SCRIPT NAME'):
    your script
-------------------
"""

import os
import slackweb
import traceback
from contextlib import contextmanager

slack_fr_mypage_webhook_url = os.environ["SLACK_FR_MYPAGE_WEBHOOK_URL"]

@contextmanager
def _notify(text):
    print ('Slack Notify waiting...')
    slack = slackweb.Slack(url=slack_fr_mypage_webhook_url)
    try:
        yield
        traceback_text = traceback.format_exc()
        attachments = []
        attachment = {
                        "title": "{}".format(text),
                        "pretext": "*Success*",
                        "text": "```{}```".format(traceback_text),
                        "mrkdwn_in": ["pretext", "text"]
                        }
        attachments.append(attachment)
        slack.notify(attachments=attachments)
    except:
        traceback_text = traceback.format_exc()
        print (traceback_text)

        attachments = []
        attachment = {
                        "title": "{}".format(text),
                        "pretext": "*Failed*",
                        "text": "```{}```".format(traceback_text),
                        "mrkdwn_in": ["pretext", "text"]
                        }
        attachments.append(attachment)
        slack.notify(attachments=attachments)

    print ('Slack Notify sent message')


