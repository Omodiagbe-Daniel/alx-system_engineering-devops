0x09. Web infrastructure design
DevOps
SysAdmin
web infrastructure
 By: Sylvain Kalache, co-founder at Holberton School
 Weight: 1
 Project to be done in teams of 3 people (your team: Daniel Onosetale Omodiagbe)
 Project over - took place from Aug 18, 2022 6:00 AM to Aug 22, 2022 6:00 AM
 Manual QA review was done by on Sep 3, 2022 9:20 AM
In a nutshell…
Manual QA review: 0.0/42 mandatory & 0.0/5 optional
Altogether:  0.0%
Mandatory: 0.0%
Optional: 0.0%
Calculation:  0.0% + (0.0% * 0.0%)  == 0.0%
Concepts
For this project, we expect you to look at these concepts:

DNS
Monitoring
Web Server
Network basics
Load balancer
Server

Resources
Read or watch:

Network basics concept page
Server concept page
Web server concept page
DNS concept page
Load balancer concept page
Monitoring concept page
What is a database
What’s the difference between a web server and an app server?
DNS record types
Single point of failure
How to avoid downtime when deploying new code
High availability cluster (active-active/active-passive)
What is HTTPS
What is a firewall
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
You must be able to explain what each component is doing
You must be able to explain system redundancy
Know all the mentioned acronyms: LAMP, SPOF, QPS
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
General
A README.md file, at the root of the folder of the project, is mandatory
For each task, once you are done whiteboarding (on a whiteboard, piece of paper or software or your choice), take a picture/screenshot of your diagram
This project will be manually reviewed:
As each task is completed, the name of that task will turn green
Upload a screenshot, showing that you completed the required levels, to any image hosting service (I personally use imgur but feel free to use anything you want).
For the following tasks, insert the link from of your screenshot into the answer file
After pushing your answer file to GitHub, insert the GitHub file link into the URL box
You will also have to whiteboard each task in front of a mentor, staff or student - no computer or notes will be allowed during the whiteboarding session
Focus on what you are being asked:
Cover what the requirements mention, we will explore details in a later project
Keep in mind that you will have 30 minutes to perform the exercise, you will get points for what is asked in requirements
Similarly in a job interview, you should answer what the interviewer asked for, be careful about being too verbose - always ask the interviewer if going into details is necessary - speaking too much can play against you
In this project, again, avoid going in details if not asked
Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. Simple web stack
mandatory
Score: 0.0% (Checks completed: 0.0%)
A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a LAMP stack.

On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via www.foobar.com. Start your explanation by having a user wanting to access your website.

Requirements:

You must use:
1 server
1 web server (Nginx)
1 application server
1 application files (your code base)
1 database (MySQL)
1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8
You must be able to explain some specifics about this infrastructure:
What is a server
What is the role of the domain name
What type of DNS record www is in www.foobar.com
What is the role of the web server
What is the role of the application server
What is the role of the database
What is the server using to communicate with the computer of the user requesting the website
You must be able to explain what the issues are with this infrastructure:
SPOF
Downtime when maintenance needed (like deploying new code web server needs to be restarted)
Cannot scale if too much incoming traffic
Please, remember that everything must be written in English to further your technical ability in a variety of settings.