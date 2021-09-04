import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-1855739368626-1852667049269-PPy9fFx8jPDC5mI8bFhEf0bM"
 
post_message(myToken,"#stock","test")
