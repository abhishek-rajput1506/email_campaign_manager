from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading
import time
import queue

from campaign.utils.mail_util import MailUtility

class MessagePublisher:
    def __init__(self, queue, no_of_threads = 4):
        self.campaign_queue = queue
        self.num_threads = min(no_of_threads,self.campaign_queue.qsize())
        self.email_sender = "abhishekrajput098765432@gmail.com"

    def start_publishing(self, recipients):
        threads = []
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self.publish_message, args=(recipients, ))
            thread.start()
            threads.append(thread)

        # Wait for all threads to finish
        for thread in threads:
            thread.join()
        # smtp_obj.quit()
        print("Campaign publishesd to all subscribers")

    def publish_message(self, recipients):
        while True:
            try:
                campaign_data = self.campaign_queue.get_nowait()  # Get an item from the queue
                self._publish_messages(campaign_data, recipients)         # Process the item
                self.campaign_queue.task_done()          # Mark the item as done
            except queue.Empty:
                break
    
    def _publish_messages(self, campaign_data, email_recievers):
        print(threading.current_thread().name, end=' -> ') # Here
        mail_utility = MailUtility(self.email_sender, "befsetqgncbyzznh")
        smtp_obj = mail_utility.get_smtp_obj()
        em = self.prepare_message_object(campaign_data, self.email_sender, email_recievers)
        smtp_obj.sendmail(self.email_sender, email_recievers, em.as_string())
        print(f"Sent the mail to {email_recievers}")
        time.sleep(1)

    def prepare_message_object(self, campaign_data, email_sender, email_recievers):
        msg = MIMEMultipart('mixed')
        msg['From'] = email_sender
        msg['To'] = ", ".join(email_recievers)
        msg['Subject'] = campaign_data.get('subject')
       
        subject = campaign_data.get('subject')
        preview_text = campaign_data.get('preview_text')
        article_url = campaign_data.get('article_url')
        html_content = campaign_data.get('html_content')
        plain_text_content = campaign_data.get('plain_text_content')
        published_date = campaign_data.get('published_date')

        email_body = f"""
        <html>
        <body>
            <h1>{subject}</h1>
            <p>{preview_text}</p>
            <p>Published Date: {published_date}</p>
            <p>Read the full article <a href="{article_url}">here</a></p>
            <hr>
            {html_content}
            <hr>
            {plain_text_content}
        </body>
        </html>
        """

        # Attach the HTML part
        msg.attach(MIMEText(email_body, 'html'))

        return msg
