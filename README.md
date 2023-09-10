# email_campaign_manager
It is a campaign manager which could be used to send mail to active subscribes registered in builtin database provided with django with inforamtion of a campaign

Subscriber and Campaigns can be added through admin-panel
#To login admin panel
Go to '/admin'
Username: admin
password: admin


Three end-points are exposed
1./campaigns/unsubscirbe_user' : 
METHOD: PUT
INFO:  To unsubscribe an user for recieving mail
###
curl --location --request PUT 'http://127.0.0.1:8000/campaigns/unsubscirbe_user' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email":"abzerodha119@gmail.com"
}'
###


2./campaigns/send_campaign_messages/ : 
METHOD: GET
INFO: To send campaign detail email to active subscribers
###
curl --location 'http://127.0.0.1:8000/campaigns/send_campaign_messages/'
###

3./campaigns/subscriber
METHOD: POST
INFO: To add subscriber for mails
###
curl --location 'http://127.0.0.1:8000/campaigns/subscriber' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email":"karthik123@gmail.com",
    "first_name":"Karthik"
}'
###

#Move to /email_campaign_manager
#To install requirements RUN
pip install -r requirements.txt

#To run server RUN
python3 manage.py runserver
