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
  
# Create a Repository on github and push your code using the following commands
  ```python
   
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/yourGithubName/yourRepoName.git
git push -u origin main
  ```
  
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
  
###  Step 4 Configure EC2 instance
  ###### Connect to Ec2 bash in order to do the configuration,we will connect to the browser.Click Connect
  ![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/click.png "install inside dir virtualenv") 
  ###### At the bottom Click connect button
  ![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/click_connect.png "install inside dir virtualenv")
  ###### After connecting to bash lets update the server
 ### 1. Update Your Server
  ###### Its very much important to update the server
  ```python
  sudo apt-get update
sudo apt-get upgrade
  
  ```
 ### 2.  Use a Virtual Environment for Python
  ```python
  apt-get install python3-venv
mkdir /home/udoms/env/
python3 -m venv /home/udoms/env/md
  ```
 ### 3. Now activate your virtual environment.
  ```python
  source /home/ubuntu/env/md/bin/activate
  ```
  ###### After activating you will see something like this
  ![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/bash.png "install inside dir virtualenv")
  
  ###### You can also verify that you are working from within your virtual environment by taking a look at where the Python binary is located.`which python`
 ### 4. clone the repo 
  ```python
  git clon <url to to you repo>
  ```
  ### 5. Navigate to the cloned repo folder `cd microdomains`
  ### 6.  Get Started With uWSGI
  ###### First we need to install the web server gateway interface (WSGI). In this case, we will be using uWSGI. You will also need the development packages for your version of Python to be installed.
  ```python 
  sudo apt-get install python3.8-dev
sudo apt-get install gcc
pip install uwsgi
  ```
  
 ### 7. Add you domain which will be your public ip  address or domain name to allowed in settings.py on django project
  ![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/allowed.png "install inside dir virtualenv")
 ### 8. Get Started With uWSGI
  ###### First we need to install the web server gateway interface (WSGI). In this case, we will be using uWSGI. You will also need the development packages for your version of Python to be installed.
 ```python
  sudo apt-get install python3.8-dev
sudo apt-get install gcc
pip install uwsgi
  ```
### 8. Configure the Nginx Web Server
  ###### Install Nginx `sudo apt-get install nginx`
### 9. Let’s tell Nginx about our Django project by creating a configuration file at sudo nano /etc/nginx/sites-available/microdomains.conf
  ![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/config.png "install inside dir virtualenv")
  ```python
  # the upstream component nginx needs to connect to
upstream django {
    server unix:///home/udoms/yourreponame/mysite.sock;
}
# configuration of the server
server {
    listen      80;
    server_name micro.domains www.micro.domains;
    charset     utf-8;
    # max upload size
    client_max_body_size 75M;
    # Django media and static files
    location /media  {
        alias /home/ubuntu/rouyReponame/media;
    }
    location /static {
        alias /home/ubuntu/yourRoponame/static;
    }
    # Send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include     /home/ubuntu/yourReponame/uwsgi_params;
    }
}
  ```
 ### 9. We need to create the `sudo nano /home/udoms/microdomains/uwsgi_params
  ```python
  uwsgi_param  QUERY_STRING       $query_string;
uwsgi_param  REQUEST_METHOD     $request_method;
uwsgi_param  CONTENT_TYPE       $content_type;
uwsgi_param  CONTENT_LENGTH     $content_length;
uwsgi_param  REQUEST_URI        $request_uri;
uwsgi_param  PATH_INFO          $document_uri;
uwsgi_param  DOCUMENT_ROOT      $document_root;
uwsgi_param  SERVER_PROTOCOL    $server_protocol;
uwsgi_param  REQUEST_SCHEME     $scheme;
uwsgi_param  HTTPS              $https if_not_empty;
uwsgi_param  REMOTE_ADDR        $remote_addr;
uwsgi_param  REMOTE_PORT        $remote_port;
uwsgi_param  SERVER_PORT        $server_port;
uwsgi_param  SERVER_NAME        $server_name;
  ```
  ![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/micro.png "install inside dir virtualenv")
  
### 10. Next we can publish our changes by creating a symbolic link from sites-available to sites-enabled like so:
  `sudo ln -s /etc/nginx/sites-available/microdomains.conf /etc/nginx/sites-enabled/`
### 11. At settings.py on your django project ,add the following 
  ```python
  STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
  ```
  ![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/macro.png "install inside dir virtualenv")

###### With these changes in place, we can now tell Django to put all static files in the static folder.Run `python manage.py collectstatic`
 ### 12. Restart the Nginx server to apply changes by running the following command
  `sudo /etc/init.d/nginx restart`
  ### 13. Get Nginx, uWSGI, and Django to Work Together `uwsgi --socket mysite.sock --module yourRepoName.wsgi --chmod-socket=666`
  ### 14. Lets now configure our Production server
  ###### Rather than passing arguments to uWSGI like we did above, we can put these options in a configuration file at the root of you Django project called `mysite_uwsgi.ini`
  ```python
  [uwsgi]
# full path to Django project's root directory
chdir            = /home/ubuntu/yourReponame/
# Django's wsgi file
module           = yourReponame.wsgi
# full path to python virtual env
home             = /home/ubuntu/env/md
# enable uwsgi master process
master          = true
# maximum number of worker processes
processes       = 10
# the socket (use the full path to be safe
socket          = /home/ubuntu/yourReponame/mysite.sock
# socket permissions
chmod-socket    = 666
# clear environment on exit
vacuum          = true
# daemonize uwsgi and write messages into given log
daemonize       = /home/ubuntu/uwsgi-emperor.log
  ```
  ![alt text](https://github.com/Danchiwaz/technical-interview-interintel/blob/main/screenshots/wsgi.png "install inside dir virtualenv")
 ######  Proceed to start up uwsgi and specify the ini file by running the command: `uwsgi --ini microdomains_uwsgi.ini`
  
###### Visit http:public ip address/domain name a browser and you will see the default Django landing page if everything works correctly.
  
