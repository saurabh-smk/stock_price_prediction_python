from datetime import datetime
from KafkaProducerPy import KafkaProducer
import time

class CollectDataScheduler():
    def scheduleKafkaProducer(self):
        now = datetime.now()
        startTime = now.replace(hour=14, minute=30, second=0, microsecond=0)
        endTime = now.replace(hour=21, minute=30, second=0, microsecond=0)
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            current_day = now.strftime("%A")
            if startTime <= current_time <= endTime and current_day in ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday']:
                print("Collect data for: ", current_time)
                KafkaProducer()
                time.sleep(60)

schedule = CollectDataScheduler()
schedule.scheduleKafkaProducer()