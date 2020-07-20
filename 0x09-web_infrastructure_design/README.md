# Project 0x09-Web infrastructure design

Web infrastructure concepts

Concepts:

    Network basics
    Server
    Web server
    DNS
    Load balancer
    Monitoring
    What is a database
    What’s the difference between a web server and an app server?
    DNS record types
    Single point of failure
    How to avoid downtime when deploying new code
    High availability cluster (active-active/active-passive)
    What is HTTPS
    What is a firewall
    You must be able to explain system redundancy
    Know all the mentioned acronyms: LAMP, SPOF, QPS

Tasks:

0-simple_web_stack - design a one server web infrastructure that hosts the website that is reachable via www.foobar.com. Start your explanation by having a user wanting to access your website.
Requirements:

        1 server
        1 web server (Nginx)
        1 application server
        1 application files (your code base)
        1 database (MySQL)
        1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8


1-distributed_web_infrastructure - design a three server web infrastructure that hosts the website www.foobar.com.
Requirements:

        2 servers
        1 web server (Nginx)
        1 application server
        1 load-balancer (HAproxy)
        1 set of application files (your code base)
        1 database (MySQL)


2-secured_and_monitored_web_infrastructure - design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.
Requirements:

        3 firewalls
        1 SSL certificate to serve www.foobar.com over HTTPS
        3 monitoring clients (data collector for Sumologic or other monitoring services)


3-scale_up
Requirements:

    You must add:
        1 server
        1 load-balancer (HAproxy) configured as cluster with the other one
        Split components (web server, application server, database) with their own server
