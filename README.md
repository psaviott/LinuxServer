# Linux Server Configuration

Fron a baseline installation of a AWS Ubuntu Server we prepare it to host a
web application learning  how to access, secure, and perform the initial
configuration of a bare-bones Linux server. Also we install and configure a
database server, and deploy a
[Items Project](https://github.com/psaviott/Item-Catalog "Github project repository")
application onto it.

## Getting Started

This project use a Amazon Lightsail Ubuntu Server to host an application.
Here some information to access the host.
* IP Address: **18.204.17.121**
* SSH port: **2200**
* URL:

### Prerequisites

To deploy this application in your own AWS sistem you will need:
* [Amazon Web Services](https://aws.amazon.com/pt/?nc2=h_lg "Amazon Web Services homepage") account
* [Ubuntu Linux Server](https://www.ubuntu.com/) instance on [Amazon Lightsail](https://aws.amazon.com/pt/lightsail/ "Amazon Lightsail homepage")

### Installing and Running

1. Update all currently installed packages.
  ```
    $ sudo apt update && sudo apt upgrade
  ```

2. Change the SSH port from **22** to **2200** and forbid root access.
  ```
    $ sudo vi /etc/ssh/sshd_config
  ```
  ```
    $ sudo service ssh restart
  ```

3. Configure Lightsail firewall

  Inside the Item-Cataglog-Server instance on Amazon Lightsail go to network. Then add rules for HTTP, TCP and NTP connections.

4. Configure UFW firewall to only allow incoming connections for SSH(2200), HTTP(80) and NTP(123).

  Deny all incoming
  ```
    $ sudo ufw default deny incoming
  ```
  Allow all outgoing
  ```
    $ sudo ufw default allow outgoing
  ```
  Allow SSH on port 2200
  ```
    $ sudo ufw allow 2200/tcp
  ```
  Allow HTTP on port 80
  ```
    $ sudo ufw allow 80/tcp
  ```
  Allow NTP on port 123
  ```
    $ sudo ufw allow 123/udp
  ```
  Enable firewall
  ```
    $ sudo ufw enable
  ```
  >Warning: When changing the SSH port, make sure that the firewall is open for port 2200 first, so that you don't lock yourself out of the server.

  After that you can logon server with:
  ```
    $ ssh -i ~/.ssh/LightsailDefaultKey.rsa ubuntu@18.204.17.121 -p 2200
  ```

5. Give grader access.

  Create new user account on server
  ```
    $ sudo adduser grader
  ```
  Give user sudo permission adding grader ALL=(ALL:ALL) ALL to the file
  ```
    $ sudo visudo
  ```
  Create SSH key for user
  ```
    $ ssh-keygen -f ~/.ssh/udacity_key.rsa
  ```
  Add key for authorized_keys file
  ```
    $ sudo vi /home/grader/.ssh/authorized_keys
  ```
  Change the owner the permissions and restart the service
  ```
    $ sudo chown -R grader:grader /home/grader/.ssh
    $ sudo chmod 700 /home/grader/.ssh
    $ sudo chmod 644 /home/grader/.ssh/authorized_keys
    $ sudo service ssh restart
  ```
  Now you can logon system with the new user
  ```
    $ ssh -i ~/.ssh/udacity_key.rsa grader@18.204.17.121 -p 2200
  ```

6. Configure the local timezone to UTC

  By default Ubuntu systems has the timezone seted to UTC. To confirm you can run the comand:
  ```
    $  sudo dpkg-reconfigure tzdata
  ```

7. Install and configure Apache to serve a Python3

  Install Apache2
  ```
    $  sudo apt install apache2
  ```
  Install Python 3 mod_wsgi to allow apache2 to serve python3
  ```
    $  sudo apt-get install libapache2-mod-wsgi-py3
  ```
  Start Apache Server
  ```
    $  sudo service apache2 start
  ```

8. Install Github
  ```
    $  sudo apt install git
  ```

9.

## Deployment

* [How to create a Amazon Lightsail Instance](https://www.systemfixes.com/2018/12/31/how-to-create-an-aws-lightsail-linux-instance/ "Article about how to create an instance on Lightsail")
* [Connect to your instance with SHH private key](https://support.plesk.com/hc/en-us/articles/360000471513-How-to-connect-to-Amazon-Lightsail-server-via-SSH-with-a-private-key "How to connect to Amazon Lightsail server via SSH with a private key ")
* [How to configure UFW Firewall](https://www.digitalocean.com/community/tutorials/how-to-setup-a-firewall-with-ufw-on-an-ubuntu-and-debian-cloud-server "How To Setup a Firewall with UFW")

## Built With

* [Amazon Lightsail](https://aws.amazon.com/pt/lightsail/ "Amazon Lightsail homepage")
* [Ubuntu Server](https://www.ubuntu.com/ "Ubuntu homepage")
* [Apache](https://apache.org/ "Apache homepage")
* [UFW](https://help.ubuntu.com/community/UFW "UFW community")
* [PostgreSQL](https://www.postgresql.org/ "PostgreSQL homepage")

## Authors

* Philipe Saviott - [psaviott](https://github.com/psaviott)

## Acknowledgments

* [Python3](https://docs.python.org/3.6/index.html "Python3 documentation") documentation
* [SSH](https://en.wikipedia.org/wiki/Secure_Shell "Article about SSH") Wikipedia
* [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time " Article about UTC time") Wikipedia
* [Python mod wsgi](https://modwsgi.readthedocs.io/en/develop/ "mod wsgi documentation") documentation