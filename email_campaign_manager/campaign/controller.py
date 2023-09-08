from .utils.message_publisher import MessagePublisher
from .utils.mail_util import MailUtility
import queue

class CampaignController:
    def publish_message_to_subscribers(self, campaign_data_list, subscribers):
        sub_queue = queue.Queue()
        for campaign in campaign_data_list:
            sub_queue.put(campaign)
        publisher = MessagePublisher(sub_queue, 5)
        # publisher._publish_messages(campaign_data_list[0], ["abrajput1506@gmail.com", "abzerodha119@gmail.com"])
        publisher.start_publishing(subscribers)
        return campaign_data_list