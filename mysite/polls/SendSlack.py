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
    TOKEN = 'xoxp-980938038944-970840742289-980491059588-ab85c3dbcb369eeb21fc51b192a30931'
    client = WebClient(token=TOKEN)

    response = client.files_upload(
        channels='#google-trend',
        file=file
    )
    assert response["ok"]


# send_file_to_slack('figure.png')



