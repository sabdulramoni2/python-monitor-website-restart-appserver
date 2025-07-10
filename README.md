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
- Run nginx container
