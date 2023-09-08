import threading
import time
import queue

class MessagePublisher:
    def __init__(self, message, queue, no_of_threads = 4):
        self.message_content = message
        self.subscriber_queue = queue
        self.num_threads = min(no_of_threads,self.subscriber_queue.qsize())

    def publish_message(self):
        while True:
            try:
                item = self.subscriber_queue.get_nowait()  # Get an item from the queue
                self._publish_messages(item)         # Process the item
                self.subscriber_queue.task_done()          # Mark the item as done
            except queue.Empty:
                break
    
    def _publish_messages(self, item):
        print(threading.current_thread().name, end=' -> ') # Here
        print(f"Processing item: {item}")
        time.sleep(1)

    def start_publishing(self):
        threads = []
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self.publish_message)
            thread.start()
            threads.append(thread)

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        print("All items processed.")


