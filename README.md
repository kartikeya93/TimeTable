# Time-table Management System

This is a project done for Ela Women as a task for the employment process.

## Technologies used

1. Python
2. Django
3. HTML
4. Bootstrap
5. Django-Utilities like django-widgets, django-notifications-hq
6. Celery for CRON Jobs
7. SQLite3 for database

## Objective

To create a Django-based website, where 7 teachers will be given a schedule for the day, with emails and notifications at the beginning of each class.

## What was achieved

Django based site beautified using bootstrap which consists of the following:

1. Registration page for the teachers
2. Login page
3. User specific home page
4. User specific timetable application, which shows the timetables for the next 4 days (should the time tables exist)
5. CRON-like jobs for mainly TWO tasks:
    - Creating new timetables for every user at 00:00 hrs every weekday.
    - Sending emails and notifications 10 mins before each class. (No notification/email if the teacher has a free period)
6. Time table created will never have any collisions: No two teachers will have same class at the same time, and every class will have all 7 periods.

## Installation

1. Install Python/Django
2. Install dependencies like:
   - django-widgets
   - django-celery
   - django-notifications-hq
3. Clone this repository

