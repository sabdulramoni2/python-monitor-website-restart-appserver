import smtplib
import requests
import paramiko
import os
import linode_api4
import time
import schedule




EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')


def restart_server_and_container():
    # restart linode server
    print('Rebooting the server...')
    client = linode_api4.LinodeClient('61049d055573a940481eef5258be7f1dcb9cbe5d1e8c6fec7a17b4e4f4301808')
    nginx_server = client.load(linode_api4.Instance, 78380840)
    nginx_server.reboot()

    # restart the application
    while True:
        nginx_server = client.load(linode_api4.Instance, 78380840)
        if nginx_server.status == 'running':
            time.sleep(5)
            restart_container()
            break

def send_notification(email_msg):
    print('Sending an email...')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject: SITE DOWN\n\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)
def restart_container():
    print('Restarting the application.....')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname='172.234.194.61',
        username='root',
        key_filename='C:/Users/abdul/.ssh/id_rsa_new'
    )
    stdin, stdout, stderr = ssh.exec_command('docker start 12cf8a8c29b7')
    print(stdout.readlines())
    ssh.close()

def monitor_application():
    try:
        response = requests.get('http://172-234-194-61.ip.linodeusercontent.com:8080/')
        if response.status_code == 200:
            print('Application is running successfully!')
        else:
            print('Application Down. Fix it!')
            msg = f"Application returned {response.status_code}"
            send_notification(msg)
            restart_container()

            # restart the application
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(
                hostname='172.234.194.61',
                username='root',
                key_filename='C:/Users/abdul/.ssh/id_rsa_new'
            )
            stdin, stdout, stderr = ssh.exec_command('docker start 12cf8a8c29b7')
            print(stdout.readlines())
            ssh.close()
            print('Application restarted')

            ssh.exec_command('docker restart <container_name>')

    except Exception as ex:
        print(f'Connection error happened: {ex}')
        msg = f"Connection error happened: {ex}"
        send_notification(msg)
        restart_server_and_container()

schedule.every(5).seconds .do(monitor_application)


while True:
    schedule.run_pending()


















