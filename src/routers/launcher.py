from fastapi import APIRouter

from methods.JIRA import JiraManager


router = APIRouter()

VERSION = "v1"
TAG = "Termination"


@router.post("/" + VERSION + "/unassigned", tags=[TAG])
def unassigned(user_id: int):
    jira = JiraManager()
    jira.unassigned(user_id)
    return {'result': 'All tickets unassigned'}
