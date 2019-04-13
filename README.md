# ingest-twitter

# Dev set up:
 ```
 $ make clean install dev-install
 $ source venv/bin/activate
 $ make lint test scan
 ```

 Start Zooper and Kafka from the Kafka install directory:bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties

Create a topic. We will create the topic “trump” as obviously there are a lot of Tweets about the President.
 bin/kafka-topics.sh --create --zookeeper localhost:2181 --repl

Download

 http://mirror.ox.ac.uk/sites/rsync.apache.org/kafka/2.2.0/kafka_2.12-2.2.0.tgz

