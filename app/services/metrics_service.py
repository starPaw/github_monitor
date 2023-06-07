import pandas as pd
from typing import List, Dict


class MetricsService:
    def __init__(self):
        pass

    def average_time_between_pull_requests(self, events: List[Dict]) -> float:
        """
        Calculate the average time between pull requests for a given repository.

        :param events: A list of events
        :return: The average time between pull requests
        """
        # Filter the PullRequestEvent events
        pull_requests = [event for event in events if event['type'] == 'PullRequestEvent']

        # If there are less than 2 pull requests, we cannot calculate the average time between them
        if len(pull_requests) < 2:
            return None

        # Convert the event creation times to datetime
        times = pd.to_datetime([pr['created_at'] for pr in pull_requests])

        # Calculate the time differences between consecutive pull requests
        time_diffs = times.diff()

        # Return the average time difference
        return time_diffs.mean().total_seconds()

    def count_events_by_type(self, events: List[Dict], event_type: str) -> int:
        """
        Return the total number of events of a given type.

        :param events: A list of events
        :param event_type: The type of the event
        :return: The total number of events of the given type
        """
        return len([event for event in events if event['type'] == event_type])
