import ssl
import smtplib

class MailUtility:
    """
        Utility class to setup smtp connection. using email and app-password
    """

    def __init__(self, sender: str , password: str) -> None:
        self.email_sender = sender
        self.email_password = password
        
    def get_smtp_obj(self):
        """
            Creates context required for smtp connection, connects to mail server
            and logged in the user

            returns:
                smtp connection instance 
        """
        context = ssl.create_default_context()
        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
        smtp.login(self.email_sender, self.email_password)

        return smtp
        

