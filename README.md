# Flask Timetable Project

This project is a Flask web application that connects to a PostgreSQL database (in my case with the help of docker) to display the table of courses based on the student’s level (courses grabbed from my course schedule).

## Project Overview

This is an application that uses flask to build a web app that connects to a postgres database database contains a table named `courses` with course details like course_name, course_code, etc.
Also for easy deployment used dockerization.

## Before setup you should start your database and configure the files in a project for your usage:
you should change parameters username, password, port, and database
after that for best experience add data to your database that can be graded by levels (if more that two, add some in the index.html)

The next step is to create a docker file by using this command:
docker built -t image_name

And now you can follow further instructions for setup

## Setup instructions using docker
pull the image by using
docker pull image_name

Then run it in attached mode by using:
docker run --name any_name p5000:5000 image_name

After that you can go to your localhost:5000 and see that app already works there.

### Prerequisites
- Python
- PostgreSQL
- Docker

## Screenshots:
![image](https://github.com/user-attachments/assets/d3d28287-1f59-4ae5-96f8-218087ddddec)
![image](https://github.com/user-attachments/assets/836164ac-89d2-4b6b-8149-53e4c6a98690)

