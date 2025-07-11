# **python-monitor-website-restart-appserver**

## **Project Overview**
ThiThe purpose of this project is to write a scheduled Python program to automatically monitor the status of a nginx server. If the server receives a HTTP response code other than 200, the Python program will send an email notification to IT staff and restart the container. If the server is not accessible to users at all, an email notification to IT staff wil be sent and both the server and the container will be restarte

---
  
## **Feature**
- Create Server on Linode
- Install Docker 
- Run nginx container

### **Diagrammatic Presentation**
- Create Server on Linode
  
  -  This section outlines creating a Linux server in the Akamai Linode cloud platform. This section concludes with establishing an SSH session into the server
        <img width="975" height="317" alt="image" src="https://github.com/user-attachments/assets/4f5afbe3-db22-421a-82a1-ddc1ae5e1178" />
  
  - On the Linodes/Create screen, ensure the Distributions tab is selected. From the Choose a Distribution section, accept the default image as Debian 11 from the dropdown. In the Region section, select the datacenter           location closest to the end users (Chicago, IL is selected for this project).  In the Linode Plan section, click on the Shared CPU tab and select the Linode 2GB option.
        <img width="975" height="603" alt="image" src="https://github.com/user-attachments/assets/a0dcbf85-e725-4557-abd1-21488a1c1685" />
  - Scroll to the bottom of the screen and enter the root password.
        <img width="911" height="255" alt="image" src="https://github.com/user-attachments/assets/8b950580-786a-45a5-a101-9b9c350785e8" />

  - In the SSH Keys section, click the Add an SSH Key button.
        <img width="975" height="285" alt="image" src="https://github.com/user-attachments/assets/48904185-fca8-43eb-85be-c96cd31e9fab" />
        
  - In the Add SSH Key pane, specify the label as “python-monitoring.” Minimize the web browser. Open PowerShell and type the following command to display the public SSH Key as output. Copy the key to the clipboard
    ```
          type ~/.ssh/id_rsa.pub
    ```

          <img width="975" height="295" alt="image" src="https://github.com/user-attachments/assets/e1da3890-2d0e-4470-b14f-bae834261b6b" />
    
  - Scroll to the bottom of the page and click the Create Linode button.

          <img width="975" height="150" alt="image" src="https://github.com/user-attachments/assets/44023ac5-0a21-4f02-90de-78730fcabb88" />
          

  - The server will now be in the provisioning state.

          <img width="975" height="301" alt="image" src="https://github.com/user-attachments/assets/fba1a676-d402-4596-bd7d-3e72746d5b97" />
    
  - Restore PowerShell and paste the SSH command from the clipboard. When prompted to continue connecting, type yes and press Enter.
          <img width="975" height="416" alt="image" src="https://github.com/user-attachments/assets/bca197e6-6ff2-4b09-a1c3-5984d57274ab" />
          
    The SSH session into the Linode server is established.

- Install Docker
    
  - This section installs Docker on the Linode-hosted Linux server.
    Inside the SSH session, confirm the Linux distribution is Debian by entering the following command:
    ```
           cat /etc/os-release
    ```
     Confirm the value for NAME is listed as Debian.
          <img width="784" height="342" alt="image" src="https://github.com/user-attachments/assets/7302c55a-1101-42b4-98d6-e0a6c337ccf1" />
          
  - Navigate to the official Docker documentation for installing the Docker Engine on Debian Linux (https://docs.docker.com/engine/install/debian/).  This project walkthrough will use the apt installation method.
  - Restore the SSH session and enter the following command to update the Docker’s Apt repository. As the root user is logged in, sudo commands are omitted.
    ```
          apt-get update
    ```
  - Run the following command to install ca-certificates, the curl command line tool, and gnupg (GNU Privacy Guard).
    ```
          apt-get install ca-certificates curl gnupg
    ```
  - Install to the /etc/apt/keyrings directory (-d) with permissions (-m) set as 0755. The 0755 permission sets full control to the owner, as well as read and execute permissions to the group and everyone else
    ```
          install -m 0755 -d /etc/apt/keyrings
    ```
  - The curl command downloads the official Docker GPG key from the official Docker site. The --dearmor option for the gpg command line tool unshields PEM armors and writes (-o) to the /etc/apt/keyrings/docker.gpg            directory. (https://www.gnupg.org/documentation/manuals/gnupg/Operational-GPG-Commands.html).
    ```
          curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    ```  
  - Grant all users read permission to /etc/apt/keyrings/docker.gpg
    ```
          chmod a+r /etc/apt/keyrings/docker.gpg
    ```
  - Add the “stable” Docker repository to Apt and update apt-get to prepare Docker for installation:
    ```
          echo \
          "deb [arch="$(dpkg --print-architecture)" signed by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
          "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
          tee /etc/apt/sources.list.d/docker.list > /dev/null
          apt-get update
    ```
  - Install the Docker engine and all relevant plugins (e.g. docker-compose).
    ```
          apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```
  - Confirm docker is now available to use by issuing the following command:
    ```
          docker -v
    ```
    <img width="705" height="163" alt="image" src="https://github.com/user-attachments/assets/d1f76dbc-192c-4280-b96b-60ad5e6ae641" />

- Run nginx container
  - This section uses Docker to create a nginx container on the Linode-hosted Linux server.
    In the SSH session, execute the following command to run a nginx container. The -d option runs the container in detached mode, and the -p option specifies the port (8080 being the container port and 80 being the host     port)
    ```
          docker run -d -p 8080:80 nginx
    ```
    <img width="975" height="281" alt="image" src="https://github.com/user-attachments/assets/8de53e2a-fac8-4861-bda0-959bb336c92b" />
    
  - Navigate back to the Akamai Linode web portal. Copy and paste the public IP address to the clipboard.
    <img width="975" height="286" alt="image" src="https://github.com/user-attachments/assets/8710d753-54bf-49d3-8308-a146868a64fe" />
  - Back on the Akamai Linode web portal tab, click inside the new Linux server instance to get more detailed information. Click on the Network Tab and copy the value for Reverse DNS to the clipboard.
    <img width="975" height="172" alt="image" src="https://github.com/user-attachments/assets/39c711aa-3aee-48fd-9845-3fdece778c9c" />
  - Open a new browser tab and paste the DNS name into the address bar, adding :8080 as the port.
    <img width="975" height="411" alt="image" src="https://github.com/user-attachments/assets/4429c23d-b9e8-400c-b5c6-7d2297026f5d" />

- Python Project Creation
  - This schedule outlines the process of creating the Python project in JetBrains PyCharm and pushing the project to the GitLab repository.
  - Open the JetBrains PyCharm code editor. In the upper lefthand corner, click the Hamburger Menu (≡) > File > New Project.
    <img width="811" height="430" alt="image" src="https://github.com/user-attachments/assets/ee78fc6d-e688-4e0a-8377-216f56d5adf4" />
  - Add a blank README.md file by right-clicking the root of the project folder > New > File. Name the file README.md.
    <img width="975" height="416" alt="image" src="https://github.com/user-attachments/assets/b72043af-0ef2-44a1-96ac-844aaf59ed61" />
  - Note: Although the installation of Git on Windows 11 is outside the scope of this project walkthrough, the Git installer can be found here: https://git-scm.com/download/win.
  - Initalize the Git repository
    <img width="975" height="177" alt="image" src="https://github.com/user-attachments/assets/b394928b-0c57-4ec7-a63a-023730824a17" />

  - Add changes and set an initial commit message:
    <img width="975" height="532" alt="image" src="https://github.com/user-attachments/assets/861a299d-b703-4d7d-96cc-b7de3a6ff3a0" />
    <img width="975" height="378" alt="image" src="https://github.com/user-attachments/assets/19cfbb3b-8ff5-4c9d-a5b9-c1a6ed62cf50" />


- Python Program: monitor-website.py
  - This section provides a comprehensive walkthrough of writing the monitor-website.py Python program. First, the Python file is created in JetBrains PyCharm. Second, logic is written for a website request where an         if/else statement is evaluated based on whether the HTTP status code is 200. Next, an email notification is sent to IT staff in the event the HTTP status code is a value other than 200. Then, exception handling is       integrated into the Python program. This section continues with writing logic for restarting the nginx container and server. For code that repeats in the program, the logic for sending email, restarting the              container, and restarting the server is converted into functions. A time library is incorporated into the project for adding additional time between the server's running state and starting the nginx container.           Finally, the program uses the schedule library to automatically run on a scheduled cadence.
    
  - Website Request
    - The purpose of the following Python logic is to programmatically access the nginx website from Python by DNS name. This mirrors a user browsing out to the nginx website in a web browser.
    - In the terminal window, use the pip command to install the requests library from PyPi.
      ```
             pip install requests
      ```
      
      <img width="975" height="243" alt="image" src="https://github.com/user-attachments/assets/c9d1d59c-a2eb-493e-ab28-b1076655ce51" />
      
    - Confirm the requests library is installed by expanding the External Libraries folder > < Python 3.11 > site-packages. The requests library will now be present.
      <img width="744" height="978" alt="image" src="https://github.com/user-attachments/assets/ca45deb7-077a-4e3c-acca-049cd2d7f470" />


    - With the requests library installed, begin the monitor-website.py file by importing the requests library:
      ```
             import requests
      ```
      The remainder of code in this section pertaining to the requests library references the following documentation (https://pypi.org/project/requests/).

    - Restore the Linode web portal and copy the DNS name of the Linux server to the clipboard. This is shown in Section I.C "Run nginx Container," Step 5 above.
    - Use the get function of the requests module. Paste the URL from Step 5 as a parameter to the get function, enclosed in parentheses and single quotes
      ```
             requests.get('http://172-234-194-61.ip.linodeusercontent.com:8080/')
      ```
    - Set the get function of the requests module as a variable called response.
      ```
             response = requests.get('http://66-228-39-99.ip.linodeusercontent.com:8080/')
      ```
    - Use the built-in print function to print the response from the nginx application.
      ``` print(response)
      ```
    - Run the program by right-clicking the monitor-website-py tab > Run ‘monitor-website.
    - A Run pane will display at the bottom of PyCharm. Confirm the response is OK, as denoted by the 200 HTTP response code. For more information about HTTP response codes, reference the following link:                       https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
      <img width="975" height="211" alt="image" src="https://github.com/user-attachments/assets/814cc294-88dc-4e36-b8a8-fbd8abc550c7" />
  
    - To see the HTML displayed in the Run window, in the print statement, call the text function on the response variable:
      ```
            print(response.text)
      ```
    - Rerun the Python program. The output is displayed below:
      <img width="975" height="466" alt="image" src="https://github.com/user-attachments/assets/8e0f530f-877d-4804-8227-467b886721ab" />

      
    - To display the numeric value of the HTTP response code 200, in the print statement, replace calling the text function with calling the status_code function:
      ```
            print(response.status_code)
      ```
    - Rerun the Python program. The output is displayed below showing the 200 HTTP response code:
      <img width="975" height="128" alt="image" src="https://github.com/user-attachments/assets/663e09b3-ea3e-4a2d-b225-dc4e4bbabd45" />
      
    - Printing the output of response.status_code from Step 12 provides the foundation to formulate a conditional if/else statement for printing different output based on the HTTP status code.
    - First, delete the following print statement:
      ```
            print(response.status_code)
      ```

    - If the HTTP status code is 200, use an if statement to display output on the screen that the application is running successfully:
      ```
            if response.status_code == 200:
            print(‘Application is running successfully!’)
      ```
      <img width="975" height="202" alt="image" src="https://github.com/user-attachments/assets/d4d0fe86-21bd-47ea-813d-3aaafa413e34" />

    - If the HTTP status code is a value other than 200, use an else statement to print that the application is down.
      ```
            else:
            print(‘Application Down. Fix it!’)
      ```
    - The monitor-website.py program up to this point is shown below:
      ```
              import requests

              response = requests.get('http://66-228-39-99.ip.linodeusercontent.com:8080/')

              if response.status_code == 200:
                  print('Application is running successfully!')
              else:
                  print('Application Down. Fix it!')
      ```

  - Email Notification
    - If the HTTP status code renders a value other than 200, there is a problem with the nginx web application and user access is unavailable. In this section, the Python program will introduce logic to automatically         send an email notification whenever the web application is down.
    - Begin by importing the built-in smtplib library. Add the import statement underneath the existing import requests statement.
      ```
              import smtplib
      ```     
      Note: Refer to the official Python documentation for more information about the smtplib library (https://docs.python.org/3/library/smtplib.html).

    - Next, the SMTP server and port will be specified in the Python program.
      In this project scenario, Gmail is used. The below screenshot is taken from official Google documentation and shows the SMTP server address and associated port (https://support.google.com/a/answer/176600?hl=en):
      <img width="482" height="125" alt="image" src="https://github.com/user-attachments/assets/eef9f204-08ac-4e2a-9a67-b7a95fbcc52b" />

      Using this information, locate the else statement written in monitor-website.py. Under the print statement, enter a couple carriage returns. Then, use the SMTP function to specify the use of Gmail's SMTP server on       port 587:
      ```
            smtplib.SMTP('smtp.gmail.com', 587)
      ```
    - As Gmail is an external application, a with statement will be needed for exception handling. Exceptions for Gmail may include login or connection-related errors, both of which are outside the control of the Python       application.
      Use the following syntax to incorporate smtplib.SMTP('smtp.gmail.com', 587) from Step 2 as part of the with statement. The as keyword stores the smtplib.SMTP function as a variable called smtp:
      ```
             with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
      ```
    - Inside the with statement block, call the starttls function on the smtp variable to ensure the connection between Gmail and the monitor-website.py Python program is encrypted
      ```
              smtp.starttls()
      ```
    - Inside the with statement block and under smtp.starttls(), enter a couple carriage returns. Call the ehlo() function on the smtp variable in order for Gmail to recognize the monitor-website.py Python program.
      ```
            smtp.ehlo()
      ```
    - For enhanced security, this program assumes that 2-Step Verification is turned on in the Google account. Before the smtp.login statement can be written in the with block, an application password will be generated        in the Google account. The application password provides permission to the Python program to act on the sender’s behalf.
    - Open a web browser and navigate to https://myaccount.google.com. In the search bar, type in app and select App passwords in the search results.
      <img width="496" height="140" alt="image" src="https://github.com/user-attachments/assets/80ab45a5-e5bc-4f1c-9eea-6c2a05a4c650" />
      
    - On the App passwords screen, enter website-monitor as the app name and click the Create button.
      <img width="463" height="452" alt="image" src="https://github.com/user-attachments/assets/f3a05fed-9a83-4882-bdf2-46ce3d96adb4" />

    - On the Generated app password dialog box, the app password will display on the screen. Copy the password to the clipboard and temporarily paste it in a text editor of choice. Click the Done button.
      <img width="897" height="716" alt="image" src="https://github.com/user-attachments/assets/341c4fc9-45d5-40a1-b271-6de9a5a049de" />

    - Return to the monitor-website.py Python program in the PyCharm editor. At the top of the program under the other import statements, import the built-in os library. More information about the os library can be            found here (https://docs.python.org/3/library/os.html).
      ```
            import os
      ```
    - With security in mind, the os library will be used to store the email username and password as environment variables so the credentials are not hardcoded in the program. Call the environ function of the os module        and get the value of the environment variables. Set both as variables natively in Python:
      ```
            EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
            EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
      ```
      Note: EMAIL_ADDRESS and EMAIL_PASSWORD are known as constants, as they are set once and do not change. Constants should be in all caps to distinguish them from other native Python variables
   
    - In the with statement, under smtp.ehlo(), call the login function on the smtp variable and pass EMAIL_ADDRESS, and EMAIL_PASSWORD as parameters.
      ```
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
      ```

    - In the upper righthand corner of PyCharm, click Current > Edit Configurations…
    - On the Run/Debug Configurations screen, click the + button.
    - In the Add New Configuration pane, select Python.
    - Name the configuration the same as the Python program (monitor-website). In the Run section, leave the script dropdown selected. Browse out to the absolute path of the monitor-website.py program (i.e. C:\python-         monitor-website-restart-appserver\monitor-website.py). Set the working directory to the root path of the project folder (C:\python-monitor-website-restart-appserver).
    - On the same screen as above, click the icon in the Environment variables textbox.
    - On the Environment Variables dialog box, click the + sign and add EMAIL_ADDRESS and EMAIL_PASSWORD as environment variables. From Step 8, paste the application password from the text editor as the value for              EMAIL_PASSWORD. Click OK.
      <img width="875" height="839" alt="image" src="https://github.com/user-attachments/assets/6d5e2fae-d474-4945-a98b-becdb6578c6f" />
    - Back on the Run/Debug Configurations screen, click OK to return to the editor.
    - Before the last function can be called to send an email, set a variable for the message. The \n in Python starts a new line, but in this case, also functions to separate the subject from the message body.
      ```
            msg = "Subject: SITE DOWN\nFix the issue! Restart the application."
      ```
    - Last, call the sendmail function on the smtp variable and pass 3 parameters: the sender’s email address, the recipient's email address, and the message. For this project's use case, assume the sender and receiver        are the same.
      ```
            smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
      ```
    - In the right hand corner of PyCharm, click the monitor-website dropdown. Next to the application name, click the green triangle icon to run the application.
    - As the nginx container is currently in the running state, the monitor-website application executes the if logic of the program which prints output that the application is running successfully.
      <img width="975" height="202" alt="image" src="https://github.com/user-attachments/assets/5ef15b64-493f-4fc6-9c71-b7ce611f0ae6" />
    - To simulate the application being down, comment out the existing if statement. Add another if statement, setting it to False, to trigger the else statement to execute. Rerun the program.
      ```
            # if response.status_code == 200:
            if False:
                print('Application is running successfully!')
      ```

      The output from the Run pane confirms the else statement is executed.
      <img width="975" height="220" alt="image" src="https://github.com/user-attachments/assets/60828cb8-9cd1-45ff-8d7f-cf805f68f005" />


    - Check Gmail and confirm the email is received. Notice the email message mirrors exactly what is set as the msg variable.
        <img width="975" height="300" alt="image" src="https://github.com/user-attachments/assets/d0ebf371-0140-46a2-8dfc-a0e07412551e" />

    - With testing complete, return to the PyCharm code editor and delete the if False: line of code from Step 24. Uncomment the original if statement.
      
  - Exception Handling
    - Issue: The Python program thus far does not account for instances when no response is returned. In these cases, the following line of code (the response) throws an exception:
      ```
            response = requests.get('http://172-234-194-61.ip.linodeusercontent.com:8080/')
      ```
      An exception can occur if the connection is refused, there is a request timeout, or the nginx container is stopped. If the program is run in these cases, the if/else logic will not be executed at all. This issue         will be simulated in the following steps:
      - SSH into the Linux host where the nginx container resides.
      - Execute the following command to identify the container ID of the nginx container:
        ```
                docker ps
        ```
      - Copy the container ID to the clipboard and execute the following command to stop the nginx container:
        ```
              docker stop <container-id>
        ```

        <img width="975" height="211" alt="image" src="https://github.com/user-attachments/assets/95bed693-f613-4266-a220-c925e2c5403a" />

      - With the nginx container stopped, return to PyCharm and rerun the program. Sample output from the exception is shown below:
        <img width="975" height="105" alt="image" src="https://github.com/user-attachments/assets/6affe314-edc8-4130-8135-b966a60f438b" />

      - Resolution: For handling exceptions, a try/except block will be incorporated into the Python program. First, the code will be tested to ensure the except block works as expected. Then, an email notification will         be sent in the event an exception occurs.
        - Begin by adding a try block underneath the response variable. Indent the entire if/else logic inside the try block as shown below. Move the response variable inside the try block and above the if/else                    statement. The try block will attempt to execute the if/else statement if a response is returned:
          ```
                try:
                      response = requests.get('http://66-228-39-99.ip.linodeusercontent.com:8080/')
                      if response.status_code == 200:
                          print('Application is running successfully!')
                      else:
                          print('Application Down. Fix it!')
                          # send email to me
                          with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                              smtp.starttls()
                              smtp.ehlo()
                              smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                              msg = "Subject: SITE DOWN\nFix the issue! Restart the application."
                              smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
          ```


          - At the same indentation level as the try block, create an except block. The except block will execute if no response from the requests.get function is returned. As shown in the graphic below, hover the mouse             cursor over the word Exception and notice this is a base class for all non-exit exceptions. Much like smtp is a variable in the with statement, ex functions the same as a variable in the except statement:
          - Inside the except block, write a print statement that displays a connection error occurred and print out the ex variable that shows the exception. The f' denotes the variable will be included inline in the               string:
            ```
                  print(f'Connection error happened: {ex}')
            ```
          - Rerun the program and notice from the output the except block is executed. The HTTPCoonectionPool exception message is displayed below:
            <img width="975" height="259" alt="image" src="https://github.com/user-attachments/assets/55e4417e-f52f-4310-abec-434be039f2f5" />

            With the except block confirmed to be functional, the next section covers additional logic in the except block to send an email alert to IT staff.

    - send_notification Function
      - Recall the existing else statement includes a with block with logic to send email. The same logic for sending email needs to be used in the except block to notify IT staff whenever an exception occurs. First,            this section demonstrates code duplication when sending an email in both the else and except blocks. Then, a function is implemented to eliminate the need to write duplicate logic.
        - First, copy the with block from the else statement to the clipboard. Paste the with block into the except block as shown below:
          ```
                except Exception as ex:
                    print(f'Connection error happened: {ex}')
                    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                        msg = "Subject: SITE DOWN\nFix the issue! Restart the application."
                        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
          ```
        - In the else statement, modify the message in the with block as follows to include the response.status_code variable. Doing so will include the HTTP status code in the email. Once again, the f" formats the                string so that the variable can be included inline in a clean manner:
          ```
                msg = f"Subject: SITE DOWN\nApplication returned {response.status_code}. Fix the issue! Restart the application."
          ```
        - In the except statement, modify the value of the msg variable in the with block to indicate the application is not accessible at all. This also indicates that no HTTP response code is returned.
          ```
                   msg = "Subject: SITE DOWN\nApplication not accessible at all."
          ```
          Now that the duplicate code has been demonstrated, a function will be introduced to remove the code duplication.
          - First, under the EMAIL_ADDRESS and EMAIL_PASSWORD constants, define a function called send_notification as follows:
            ```
                   def send_notification():
            ```
         - Inside the send_notification function, write a print statement to display output to the user that an email is being sent.
           ```
                    print('Sending an email...') 
           ```
           
          - Copy one of the with blocks from the except or else blocks and paste it underneath the print statement as shown below:
            ```
                     def send_notification():
                         print('Sending an email...') 
                         with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                                   smtp.starttls()
                                   smtp.ehlo()
                                   smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                                   msg = f"Subject: SITE DOWN\nApplication returned {response.status_code}. Fix the issue! Restart the application."
                                   smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
            ```


          - In the else statement of the try block, delete the first with block and replace it by calling the send_notification function. Delete the “send email to me” comment.
            ```
                    else:
                          print('Application Down. Fix it!')
                          send_notification()
            ```

          - As the message body is the only thing that changes in the with blocks, the message body will be passed as a parameter in the send_notification function. Assume the subject will stay the same, but the message             body will change based on whether the else or except statement is executed. Replace the message body with the newly passed email_msg parameter:
            ```
                      def send_notification(email_msg):
                      ...
                      msg = f"Subject: SITE DOWN\n{email_msg}"
            ```
          - In the else statement of the try block, reinsert the message variable by setting it to the message body (e.g. Application returned HTTP status code). Place the message variable between the print statement                and send_notification() function call.
            ```
                    msg = f'Application returned {response.status_code}'
            ```
          - Pass the message variable as a parameter to the function call.
            ```
                  send_notification(msg) 
            ```
           - In the except block, modify the message variable so that it is only set to the message body, as done in Step 6. The subject should not be included as it is already accounted for in the function.
             ```
                     msg = f'Application is not accessible at all.'
             ```
           - Delete the entire with block and call the send_notification again, passing the message variable as a parameter.
             ```
                     send_notification(msg)
             ```
           - The following shadows name warning will appear in the PyCharm editor:
             <img width="690" height="113" alt="image" src="https://github.com/user-attachments/assets/04f5280d-f429-4ce8-95f5-c6984dd9a235" />
             
           - This error is caused by the message variable being the same in the function (globally) as it is in the context of the if/else statement. To remedy this issue, in the send_notification function, rename the                msg variable to message as shown below:
             
             ```
                     message = f"Subject: SITE DOWN\n{email_msg}"
             ```
        
           - Also, in the sendmail function call on the smtp module, rename the msg variable that is passed as a parameter:
             
             ```
                     smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)
             ```
           - With the nginx docker container still in a stopped state, rerun the Python program. The following output shows the except statement is executed.
             
             <img width="525" height="67" alt="image" src="https://github.com/user-attachments/assets/c759ac52-5d11-48dc-a1da-b9cc69f6e6b6" />
             
           - Check Gmail and notice the message body is the same as the msg variable in the except statement.
             <img width="975" height="316" alt="image" src="https://github.com/user-attachments/assets/1af7ac78-3db7-46dd-a129-156edf74c087" />
             
           - With IT staff now receiving email notifications that there is an issue with the application, it is time to take action to remedy the issue.


    - Restart the nginx Container
      - In the event the application code returns a value other than 200, one potential fix is to restart the nginx container. The following logic will be written in the else block and will leverage the Paramiko                 library. The Paramiko library will allow the program to SSH into the Linode server and run the docker start command.
        - In the lefthand corner of PyCharm, click the Terminal icon to open PowerShell in the bottom pane.
        - In the PowerShell window of the PyCharm editor, use pip to install the Paramiko library. This library will provide the ability to SSH into the Linode server and run Linux commands. The remainder of this                  section references the official Paramiko documentation located here: https://docs.paramiko.org/en/3.3/api/client.html.
          
          ```
                   pip install paramiko
          ```
        - Confirm the Paramiko library is successfully installed by observing the terminal output:
          <img width="975" height="150" alt="image" src="https://github.com/user-attachments/assets/c4b0a53b-3383-42e9-93eb-5945995b6887" />

        - At the top of the monitor-website.py file, import the Paramiko library.
          ```
                import paramiko
          ```
        - Right after the send_notification function call in the else statement, enter a couple carriage returns. Write a comment to indicate the following logic will restart the application.
          ```
                # restart the application
          ```
        - Under the comment, call the SSHClient function on the Paramiko module to initialize a SSH client in the Python program. Set the function call to a variable named ssh.
          ```
                ssh = paramiko.SSHClient()
          ```
          
        - Under the SSHClient function call, call the set_missing_host_key_policy function on the ssh variable. Pass the AutoAddPolicy function as a parameter within the function to dynamically add the local                       workstations’ missing host key to the Linode server. This will eliminate the need to interactively type Y when accessing the server by SSH for the first time.
          ```
                  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())               
          ```
          
        - Under the set_missing_host_key_policy function call, write a line of code to call the connect function on the ssh variable to establish a SSH connection. Specify three named parameters: hostname, username, and           key_filename. The hostname is the IP address of the Linode server and the username is root. The key_filename is the absolute path of the workstation’s private SSH key.
          ```
                 ssh.connect(hostname='66.228.39.99', username='root', key_filename='C:/Users/Joseph/.ssh/id_rsa')
          ```
                 
          Note: the named port parameter is intentionally omitted as it is understood to use the default (port 22).
          Note: When the ssh command is issued in a terminal, the -i option is not required if the default location of the private SSH key (~/.ssh/id_rsa) is used. Regardless, the Python program requires the absolute              path to the private SSH key no matter where the private SSH key resides.
          
        - Under the connect function fall, write a line of code to call the exec_command function on the ssh variable to issue Linux commands. For testing purposes, the Linux command that will be issued is the docker ps           command. Set the docker execution command to standard input, standard output, and standard error variables.
          ```
                  stdin, stdout, stderr = ssh.exec_command('docker ps')
          ```
          Note: Standard input is what the engineer types on their keyboard inside the terminal. Standard output is the results that display on the screen. Standard error is output that is shown if an error occurs.
          
        - For testing, add an if False: line of code to bypass the if statement and run the else logic. For now, comment out the initial if statement.
          ```
                  if False:
                  # if response.status_code == 200:
          ```
        - Under the stdin, stdout, and stderr variables, print out the standard output.
          ```
                  print(stdout)
          ```
       
        - Rerun the program and notice from the output that Paramiko generates a file.
        - To read what is inside the ChannelFile, modify the print statement from Step 11 by calling the readlines function on the stdout variable.
          ```
                  print(stdout.readlines())
          ```
        
        - Rerun the program and notice the docker ps command displays output as expected.
          <img width="975" height="103" alt="image" src="https://github.com/user-attachments/assets/7129c6f9-80bc-4462-8b30-14a02f44556e" />
          
        - On the terminal window, scroll over and notice the container ID is displayed. Copy the container ID to the clipboard. Modify the docker command from step 9 to start the container
          ```
                  stdin, stdout, stderr = ssh.exec_command('docker start ID')
          ```
        - Under the print statement that displays stdout, close the SSH session by calling the close function on the ssh variable.
          ```
                  ssh.close()
          ```
        - After closing the SSH session, add a final line to display output to the user that the application has restarted
          ```
                  print('Application restarted')
          ```      
        - Delete the if False: statement and uncomment the original if statement
       
          
    - Restart the Server
      - Recall the except block handles the scenario where no response is returned because the server is not accessible to users. In this scenario, restarting the server itself will act to remedy the issue. This section         introduces the linode_api4 library to interface with Linode resource.
        - In the lefthand corner of PyCharm, click the Terminal icon to open PowerShell in the bottom pane.
        - In the PowerShell window of the PyCharm editor, use pip to install the Linode library. This library will provide the ability to interact with Linode resources (e.g. reboot a Linode server). The remainder of              this section references the official Linode documentation located here: https://pypi.org/project/linode-api4/.
          ```
                  pip install linode-api4
          ```
        - Confirm the Linode library is successfully installed by observing the terminal output:
          <img width="975" height="127" alt="image" src="https://github.com/user-attachments/assets/b35d3804-d791-473d-b4c8-34734e76b193" />
          
        - At the top of the monitor-website.py file, import the Linode library.
          ```
                import linode_api4
          ```
        - In the except block after the send_notification function call, enter a couple carriage returns and write a comment to denote that logic will be written to restart the Linode server:
          ```
                  # restart Linode server
          ```
        - Under the restart Linode server comment, write a print statement to display output to the user the server is rebooting.
          ```
                   print('Rebooting the server...')
          ```
        - Under the restart Linode server comment, call theLinodeClient function on the linode_api4 module to establish a connection to the Linode account. Set the function call to a variable named client.
          ```
                  client = linode_api4.LinodeClient()
          ```
        - If the mouse hovers over the LinodeClient function, a warning appears that a token is missing. The token is required for authentication to the Linode account.
          <img width="462" height="78" alt="image" src="https://github.com/user-attachments/assets/6a3cfa7f-b731-4b4b-8a60-a96afb20ff8e" />
          
        - Minimize the PyCharm editor and login to the Linode web portal. In the righthand corner, click the username of the account. In the My Profile section, click API tokens.
          <img width="477" height="648" alt="image" src="https://github.com/user-attachments/assets/f60fad91-f0a1-41f0-bc92-ed19f5b4f337" />
          
        - Click the Create a Personal Access Token button.
        - In the Add Personal Access Token pane, label the token as “python.” In the Select All row, select the Read/Write radio button. Click the Create Token button.
        - This is the one and only time the API token will be viewable. Copy the Personal Access Token to the clipboard and temporarily store it in a text editor of choice. Click the I Have Saved My Personal Access                Token button.
          <img width="975" height="614" alt="image" src="https://github.com/user-attachments/assets/c13c24e7-5dfa-4d7b-ab5a-9db694d86d22" />
        - Confirm the python token now appears in the Personal Access Tokens section. Minimize the Linode web portal.
        - Restore the PyCharm editor. For security reasons, the os library will again be used to store the API token as an environment variable so as to not be hardcoded into the program. Under the other constants,                create a new constant called LINODE_TOKEN. As with EMAIL_ADDRESS and EMAIL_PASSWORD, use the environ function on the os module to get the environment variable. Set the function call as a Python variable named            LINODE_TOKEN as shown below:
          ```
                  LINODE_TOKEN = os.environ.get('LINODE_TOKEN')
          ```
        
        - Return to the except block. Locate the restart Linode server comment. For the client variable, pass LINODE_TOKEN as a parameter to the LinodeClient function call on the linode_api4 module.
          ```
                  client = linode_api4.LinodeClient(LINODE_TOKEN)
          ```

       - At the top right of PyCharm, click the monitor-website dropdown > Edit Configurations...
       - On the Run/Debug Configurations screen, click the icon next to the Environment variables textbox.
       - Click the + button and add LINODE_TOKEN as an environment variable, pasting the API token as the value from the text editor. Click the OK button.
         <img width="972" height="789" alt="image" src="https://github.com/user-attachments/assets/8e14c510-c3c8-4d56-9ef1-7bf8d56c5886" />
         
       - Restore the Linode web portal. Click on Linodes in the left menu. In the right pane, click on the Linode instance for a more detailed view.
       - Copy the Linode ID number to the clipboard. Minimize the Linode web portal.
         <img width="975" height="225" alt="image" src="https://github.com/user-attachments/assets/837a7cc5-ec0c-4c8f-9c8a-717b4b79bc6c" />

     
       - Restore the PyCharm editor. Under the client variable in the except block, call the load function on the client variable. Pass two parameters: the first one to tell the load function the type of resource to              connect to (an instance) and the second one for the instance ID. Paste the instance ID from the clipboard as the second parameter. Set the load function call as a variable named nginx_server as shown below:
         ```
                 nginx_server = client.load(linode_api4.Instance, 78380840)
        ```
      - Finally, pass the reboot function to the nginx_server variable to restart the server.

        ```
                nginx_server.reboot()
        ```           

      - Open a PowerShell window and SSH into the Linux host where the nginx container resides. Enter the docker ps command to reveal the container ID. Copy the container ID to the clipboard. Issue the docker stop               command to stop the container.
        ```
                docker ps
                docker stop <container-id>
        ```
        <img width="975" height="176" alt="image" src="https://github.com/user-attachments/assets/00a53a99-93c5-481c-a802-7462d3f87bdc" />

      - Rerun the program. Output will display on the screen that a connection error occurred.
      - Restore the Linode web portal and notice the server is in a rebooting state.
        
        <img width="975" height="436" alt="image" src="https://github.com/user-attachments/assets/2e879bb0-43bf-4fca-9e19-5821d95d5c32" />

        <img width="975" height="338" alt="image" src="https://github.com/user-attachments/assets/15efc626-9b7a-4a3a-a2f3-ed76af34c8f7" />


      - In the Linode web portal, confirm the Linux server returns to a running state.
        <img width="975" height="376" alt="image" src="https://github.com/user-attachments/assets/dccef9a6-88b4-4ec0-a302-1672891579db" />

        





























          





   
- 














          
















      







   










