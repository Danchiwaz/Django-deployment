# Section B 
# QUESTION 1
## [Click me to view the Live App](http://54.84.183.133/)
# Understanging what is django
###### Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
# How I Developed the site
###### This project is concerning a login and success page.I have developed it with django, and for the designing I used figma.
###### Figma is one of the trusted designing tool though there are other tools like adobeXD.
###### The way I have designed this project,I have enabled users to sign Up in order to login and be redirected to a Success Page.

1. Django is dependent on python  for it to run ,Python is needed to be install in your local machine.[Download Python](https://www.python.org/downloads/)
2. After installing python, now we are ready to work with django but there are  things we need to take care of such as install django.

# Walkthrough
### 1. Navigate to your CMD or bash on Ubuntu.We need to install virtual environment.Type on your cmd `pip install virtualenv`


![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/install_virtu.png "install virtualenv")
### 2. Create a directory/folder for you project `md yourDirecoryName` and click enter
### 3. Nagigate to the directory created `cd yourDirectoryName`
### 4. Inside the Directory lets create a virtual environment.Write the following `virtualenv myEnv`


![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/virtual.png "install inside dir virtualenv")
### 5. Activate the virtual environment `.\myEn\Scripts\activate`

![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/activate.png "install inside dir virtualenv")

### 6. Now We can install Django inside our Virtualenv, `pip install django`

![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/django.png "install inside dir virtualenv")
### 7. Lets now create django project by running `django-admin startproject <yourProjectName>
![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/django_run.png "install inside dir virtualenv")
### 8. Navigate to the project by `cd <yourProjectName>`
![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/django_root.png "install inside dir virtualenv")
### 9. Run Django by writting `python manage.py runserver`
![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/django_running.png "install inside dir virtualenv")
  
## Your are now running Django
  
  # Deploy Django  
  
  ###### For production we shall use nginx, uwsgi and aws EC2 
  
  ### Create a free acccount on aws [Click me to view the Live App](https://aws.amazon.com/free/)
  ### Step 1: Have an EC2 instance 
  ![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/aws.png "install inside dir virtualenv")
  #### On Step1: Choose an Amazon Machine Image (AMI) page,
  -Search by “ubuntu”.
  -choose 64-bit (x86) and select Ubuntu Server 20.04 LTS (HVM), SSD Volume Type.
  ![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/search.png "install inside dir virtualenv")
### step 2: Ensure Choose instance type that is marked as *** Free tier eligible ***
  - Click *** Review and Launch. ***
  ![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/launch.png "install inside dir virtualenv")
### step 3:  Review Instance Launch page, our instance will be running Ubuntu Server 20.04.Click Launch.
  ![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/launch2.png "install inside dir virtualenv")
### On Select an existing key pair or create a new key pair modal:
  -Choose Create a new key pair
-Choose RSA key pair type
-Type in key pair name. For example, my_demo_key.
-Click Download Key Pair. A my_demo_key.pem file should be downloaded on your local machine. Make sure you safely store this key file.
-Click Launch Instances.
  
 ### Wait a few seconds. We should see the page below once the instance is ready. Click View Instances.
  ![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/view.png "install inside dir virtualenv")
 ### On Instances page, the instance that we just launched should be displayed.
- Type a name that is easy to remember. For example, my_demo_server.
- Take a note of its public IPv4 address. For example, 54.193.19.108.
- Take a note of its security group name. For example by default, launch-wizard-1.

###### At this point, a new instance is launched.
### To connect instance and make instance public, we need to alter security group.
- Open Security Groups page that is under Network & Security section.
- Click Security group ID of launch-wizard-1 group.
- On launch-wizard-1 page, click Edit inbound rules.
- On Edit inbound rules page, add *SSH* type rule whose source is *My IP*; add *HTTP* type rule whose source is *Anywhere-IPv4*; add *HTTP* type rule whose source is *Anywhere-IPv6*; add *HTTPS* type rule whose source is *Anywhere-IPv4*; add *HTTPS* type rule whose source is *Anywhere-IPv6*.
  ![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/security.png "install inside dir virtualenv")


