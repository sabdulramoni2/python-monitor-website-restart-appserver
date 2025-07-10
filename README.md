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
- Run nginx container
