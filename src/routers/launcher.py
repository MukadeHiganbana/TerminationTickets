from fastapi import APIRouter

from methods.JIRA import JiraManager
from pub_sub.pubsub import PubSub

router = APIRouter()

VERSION = "v1"
TAG = "Termination"


@router.post("/" + VERSION + "/unassigned", tags=[TAG])
def unassigned(user_id: int):
    pubsub = PubSub()
    pubsub.publish({"user_id": user_id}, "unassigned")
    return {'result': 'All tickets unassigned'}
