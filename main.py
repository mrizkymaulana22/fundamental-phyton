import requests

print ('Hello World!')
r = requests.get('https://google.com')
print (r.status_code)
if r.status_code == 200 :
    print (r.text)