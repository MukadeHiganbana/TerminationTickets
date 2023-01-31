import json
from pub_sub.pubsub import PubSub
from methods.JIRA import JiraManager


def unassigned(item):
    jira = JiraManager()
    jira.unassigned(item["user_id"])
    return {"result": True}


def callback(message):
    print(message)
    if message.attributes["etl"] == "unassigned":
        unassigned(json.loads(message.data.decode("utf-8")))
    print("ready")
    message.ack()


if __name__ == "__main__":
    print("INFO: Application startup complete.")
    pubsub = PubSub()
    pubsub.subscribe(callback)
