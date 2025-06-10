import requests

response = requests.get('http://172-234-194-61.ip.linodeusercontent.com:8080/')

if response.status_code == 200:
    print('Application is running successfully!')
else:
    print('Application Down. Fix it!')






