import requests
import time
from typing import List, Dict


class GithubService:
    def __init__(self):
        self.base_url = "https://api.github.com/events"

    def get_events(self, event_type: str, num_attempts: int = 5, delay: int = 10) -> List[Dict]:
        """
        Get specific events from Github API

        :param event_type: The type of the event
        :param num_attempts: The number of attempts to make if the request fails
        :param delay: The delay (in seconds) between attempts
        :return: The list of events
        """
        for _ in range(num_attempts):
            response = requests.get(self.base_url)
            if response.status_code == 200:
                events = [event for event in response.json() if event['type'] == event_type]
                return events
            else:
                time.sleep(delay)
        return []
