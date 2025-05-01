import os
import requests
import json


class SlackUtils:
    @staticmethod
    def send_slack_message(message):
        base_url = "https://hooks.slack.com/services"
        json_body = {"text": message}
        bot_hook_url = os.environ.get("botHookUrl")
        headers = {"Content-Type": "application/json"}

        response = requests.post(base_url + bot_hook_url, headers=headers, data=json.dumps(json_body))

        if response.status_code != 200:
            raise Exception(
                f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")
