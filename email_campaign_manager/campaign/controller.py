from .utils.message_publisher import MessagePublisher
from .models import Subscriber
import queue

class CampaignController:
    def publish_message_to_subscribers(self, campaign_data_list, subscribers):
        sub_queue = queue.Queue()
        for campaign in campaign_data_list:
            sub_queue.put(campaign)
        publisher = MessagePublisher(sub_queue, 5)
        publisher.start_publishing(subscribers)
        return campaign_data_list
    
class SubscriberController:
    def add_subscriber(self, user_details):
        email = user_details.get("email")
        first_name = user_details.get("first_name")

        if not first_name or not email:
            missing_details_response = {
                "Status": "Failure",
                "Message": f"Missing details",
            }

            return None , missing_details_response
        
        try:
            subscriber = Subscriber()
            subscriber.first_name = first_name
            subscriber.email = email
            subscriber.active = 1
            subscriber.save()
        except Exception as e:
            error = {
                "Status": "Failure",
                "Message": f"{e}",
            }
            return None, error

        response = {
            "Status": "SUCCESS",
            "Message": f"Added subscriber {first_name} with email id : {email}",
        }

        return response, None

    def unsubscribe_user(self, user_email):

        subscriber = Subscriber.objects.filter(email = user_email, active=1).first()
        if subscriber:
            subscriber.active = 0
            subscriber.save()
        
            return {
                'status' : "SUCCESS",
                'message' : f"Unsubscribed mails for user with email - {user_email}."
            }
        
        return {
            'status': "FAILURE",
            'message': f"No user found for email :{user_email} or user already unsubscribed."
        }

