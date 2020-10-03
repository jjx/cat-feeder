from __future__ import absolute_import

import os
from slackclient import SlackClient

CHANNEL_GENERAL = '#general'


class Slack(object):

    def __init__(self):
        self.client = SlackClient(os.getenv('SLACK_TOKEN'))

    def message_channel(self, message, channel):
        self.client.api_call('chat.postMessage', text=message, channel=channel)

    @classmethod
    def general(cls, message):
        Slack().message_channel(message=message, channel=CHANNEL_GENERAL)
