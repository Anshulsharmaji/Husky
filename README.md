# Husky
Django Based Social Network


Husky is a social network similar to instagram but aims to provide a professional means of communication.
It is suitable for mobile view and offers Real-time Chat using Ajax, Jquery, Web-sockets and Channels using Python/Django.
Other features are Jquery based Like, Follow, Unfollow buttons, Comments and Notifications.

# Installation

Install dependencies

pip3 install -r requirements.txt
Ensure that Redis is installed and running on port 6379 (default).

Run these two commands in two separate terminals

python3 manage.py runserver --noworker

python3 manage.py runworker

Live Preview: https://www.sucide.me
