from twilio.rest import Client

account_sid = 'ACedaa566081f3f6092c29e26edc80b45b'
auth_token = '89b0697b2080c407c974ec9106757b70'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+14324652046',
  body='<ENTER MESSAGE HERE>',
  to='+27727097561'
)

print(message.sid)
