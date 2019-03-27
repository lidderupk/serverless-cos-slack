#
#
# main() will be run when you invoke this action
#
# [@param](http://twitter.com/param) Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# [@return](http://twitter.com/return) The output of this action, which must be     a JSON object.
#
#
import json
import requests
import urllib

def main(params):
  
  try:
      print('start')
      post_message(params, params['CHANNEL'], params['sheet.nrows'])
      return { 'message': 'successfully posted message' }
  except Exception as e:
      print('error: ' + e)
      return { 'message': 'error. Check logs' }
  
  

def post_message(params,channel, text):
    print('post_message start')
    url = params['SLACK_MESSAGE_POST_URL']
    data = urllib.parse.urlencode(
        (
            ("token", params['SLACK_ACCESS_TOKEN']),
            ("channel", channel),
            ("text", text)
        )
    )
    data = data.encode("ascii")
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    request = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(request)
    print('Slack response: '+json.dumps(response.read().decode('utf-8'), indent=2))
    
    