from flask import Blueprint, Flask, jsonify
from app.services.github_service import GithubService

app = Flask(__name__)
bp = Blueprint('events', __name__)
github_service = GithubService()


@bp.route("/events/<string:event_type>")
def get_events(event_type):
    events = github_service.get_events(event_type)
    return jsonify(events)
