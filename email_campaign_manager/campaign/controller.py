from .utils.message_publisher import MessagePublisher
import queue

class CampaignController:
    def publish_message_to_subscribers(self, campaign_data, subscribers):
        sub_queue = queue.Queue()
        for subscriber in subscribers:
            sub_queue.put(subscriber)

        publisher = MessagePublisher(campaign_data, sub_queue, 5)
        publisher.start_publishing()

        return campaign_data