# from tweepy.streaming import StreamListener
# from tweepy import OAuthHandler
# from tweepy import Stream
# from kafka import SimpleProducer, KafkaClient

# access_token = "1116371784452988929-eBdkBwSAdIoiEgFMJBVPPO8bmUO7ob"
# access_token_secret =  "EYVNcLXenrUPw5guEjpHx714RFjbQboxJCrlCaAeOz196"
# consumer_key =  "G4KDnbk8f6UoRopP5wxyNrytq"
# consumer_secret =  "SfstbI5jYgP6gnkt92gIpBm73IdVbDMmh4vlnME2FO49JHVJB6"

# class StdOutListener(StreamListener):
#     def on_data(self, data):
#         producer.send_messages("wizards", data.encode('utf-8'))
#         print (data)
#         return True
#     def on_error(self, status):
#         print (status)

# kafka = KafkaClient("kafka:9092")
# producer = SimpleProducer(kafka)
# l = StdOutListener()
# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# stream = Stream(auth, l)
# stream.filter(track="wizards")