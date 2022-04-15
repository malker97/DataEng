from confluent_kafka import Producer
import json
from datetime import date
import logging
from multiprocessing import Process
from operator import ge
import socket

def getjsonfile(filepath):
    with open(filepath, 'r') as f:
        temp = json.loads(f.read())
        print(temp)
getjsonfile('bcsample.json')


class myProducer(Process):
    def __init__(self,
                config=CONFIG,
                day=str(date.today()),
                topic='',
                data_dir='',):
        Process.__init__(self)
        self.config = config
        self.day = day
        self.data_dir = data_dir
        self.delivered_records = 0
        self.topic = topic
    def acked(err, msg):
        if err is not None:
            print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
        else:
            print("Message produced: %s" % (str(msg)))
    def produce(self, data):
        # construct producer
        producer = Producer(self.config)
        for iter in data:
            # prepare message
            recordKey = str(date.today())
            recordValue = json.dumps(iter)
            producer.produce(self.topic, key=recordKey, value=recordValue, on_delivery=self.acked)
            producer.poll(timeout=0)
        producer.flush()