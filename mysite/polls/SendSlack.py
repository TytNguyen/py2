import string
import time
import pandas as pd
from pytrends.request import TrendReq
# from TypeOfTrend import TypeOfTrend
from slack import WebClient



# Posting to a Slack channel
def send_message_to_slack(text):
    from urllib import request, parse
    import json

    URL = "https://hooks.slack.com/services/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"
    post = {"text": "{0}".format(text)}

    try:
        json_data = json.dumps(post)
        req = request.Request(URL, data=json_data.encode('ascii'), headers={'Content-Type': 'application/json'})
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))

def send_file_to_slack(file):
    TOKEN = 'xoxp-980938038944-970840742289-998295696933-9ef2b8ca7d2fb747f5aabc6218fc6dfa'
    client = WebClient(token=TOKEN)

    response = client.files_upload(
        channels='#google-trend',
        file=file
    )
    assert response["ok"]


# send_file_to_slack('figure.png')



