import json
import concurrent
from google.cloud import pubsub_v1
from config import Config


class PubSub:
    def __init__(self):
        self.config = Config()
        self.topic_name = 'projects/{project_id}/topics/{topic_name}'.format(
            project_id=self.config["PUB_SUB"]["project_id"],
            topic_name=self.config["PUB_SUB"]["topic_name"],
        )

    def publish(self, data: dict, type_msg: str):
        publisher = pubsub_v1.PublisherClient()
        data = json.dumps(data).encode("utf-8")
        future = publisher.publish(self.topic_name, data, etl=type_msg)
        return future.result()

    def subscribe(self, handler):
        subscription_name = 'projects/{project_id}/subscriptions/{subscription_name}'.format(
            project_id=self.config["PUB_SUB"]["project_id"],
            subscription_name=self.config["PUB_SUB"]["subscription_name"],
        )
        with pubsub_v1.SubscriberClient() as subscriber:
            while True:
                future = subscriber.subscribe(subscription_name, handler)
                try:
                    future.result(5)  # The number of seconds to wait for the result if the future isn't done
                except concurrent.futures._base.TimeoutError:
                    future.cancel()  # Stops pulling messages and shutdowns the background thread consuming messages
                    future.result()  # Return the result of the call that the future represents
