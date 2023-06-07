import io
import matplotlib.pyplot as plt
from flask import Blueprint, Flask, jsonify, request, send_file

from app.services.github_service import GithubService
from app.services.metrics_service import MetricsService

app = Flask(__name__)
bp = Blueprint('metrics', __name__)
github_service = GithubService()
metrics_service = MetricsService()


@bp.route("/metrics/average_time_between_pull_requests", methods=['POST'])
def average_time_between_pull_requests():
    data = request.get_json()
    if 'events' not in data:
        return jsonify({"error": "Missing events data"}), 400

    average_time = metrics_service.average_time_between_pull_requests(data['events'])
    return jsonify({"average_time_between_pull_requests": average_time})


@bp.route("/metrics/count_events_by_type", methods=['POST'])
def count_events_by_type():
    data = request.get_json()
    if 'events' not in data or 'event_type' not in data:
        return jsonify({"error": "Missing events or event_type data"}), 400

    count = metrics_service.count_events_by_type(data['events'], data['event_type'])
    return jsonify({"count": count})


@bp.route("/metrics/count_events_by_type/plot", methods=['POST', 'GET'])
def plot_count_events_by_type():
    data = request.get_json()
    if 'events' not in data:
        return jsonify({"error": "Missing events data"}), 400

    event_types = ['WatchEvent', 'PullRequestEvent', 'IssuesEvent']
    counts = [metrics_service.count_events_by_type(data['events'], event_type) for event_type in event_types]

    plt.figure(figsize=(10, 6))
    plt.bar(event_types, counts)
    plt.title("Count of events by type")
    plt.xlabel("Event type")
    plt.ylabel("Count")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return send_file(img, mimetype='image/png')
