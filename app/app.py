from flask import Flask
import json
import uuid
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from confluent_kafka import Producer

access_token = "1116371784452988929-eBdkBwSAdIoiEgFMJBVPPO8bmUO7ob"
access_token_secret = "EYVNcLXenrUPw5guEjpHx714RFjbQboxJCrlCaAeOz196"
consumer_key = "G4KDnbk8f6UoRopP5wxyNrytq"
consumer_secret = "SfstbI5jYgP6gnkt92gIpBm73IdVbDMmh4vlnME2FO49JHVJB6"

# create_app wraps the other functions to set up the project


def create_app(config=None, testing=False, cli=True):
    """
    Application factory, used to create application
    """
    app = Flask(__name__, static_folder=None)

    @app.route("/")
    def hello():
        return "Hello World!"

    kafka_produce()

    return app


def kafka_produce():
    kafkaProducer = Producer({"bootstrap.servers": "localhost:9092"})

    class StdOutListener(StreamListener):
        def on_data(self, data):
            try:
                data = json.loads(data)
                if data["lang"] == "en":
                    data = json.dumps({"content": data["text"].replace("'", '"')})
                    kafkaProducer.produce(
                        "content_curator_twitter", key=str(uuid.uuid4()), value=data
                    )
                    kafkaProducer.flush()
                    print("ADDED:", data)

                return True
            except Exception as e:
                print("ERROR: %s", e)

        def on_error(self, status):
            print("ERROR: ", status)

    tweet_listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, tweet_listener)
    stream.filter(track="content_curator_twitter")
