# **python-monitor-website-restart-appserver**

## **Project Overview**
ThiThe purpose of this project is to write a scheduled Python program to automatically monitor the status of a nginx server. If the server receives a HTTP response code other than 200, the Python program will send an email notification to IT staff and restart the container. If the server is not accessible to users at all, an email notification to IT staff wil be sent and both the server and the container will be restarte

---
  
## **Feature**

### **EKS provisioning using Terraform**

- Install jenkins on digital ocean server
- Install ansible on digital ocean server
- Execute Ansible playbook from jenklins pipeline to configure 2 EC2 instances.

### **Diagrammatic Presentation**
- Install jenkins on digital ocean server
  ![image](https://github.com/user-attachments/assets/8cc2a474-d175-4907-97bb-5b6651e1d006)

  ![image](https://github.com/user-attachments/assets/4cf0542b-1117-444e-8342-0f00381a2efa)

  ![image](https://github.com/user-attachments/assets/ad6bb142-6759-4134-9f5c-065c121c9763)

  ![image](https://github.com/user-attachments/assets/269f656a-1ce2-402f-b5c4-18b907bf7f3a)

  ![image](https://github.com/user-attachments/assets/159cf267-4d2b-4fce-96ea-5ca052f09409)
