This project uses TWEEPY module a twitter API to scrape data from twitter.

This project gets the latest trending hash tags for APPLE Company, Latest I Phone X hash tags.

In src under tweety django app in tasks.py configure twitter API settings.

Create a virtual env with python 3 and install requirements.txt.

Configure database settings in settings.py.

run migrate command.

run celery to start twitter API as a cron command:- python manage.py celeryd -v 2 -B celery -E INFO

cron is a perodic task which will run every 5 mins.

In other terminal run manage.py runserver

![alt text](https://github.com/sskadit/iphonedjangotwitter/blob/master/1.png)

![alt text](https://github.com/sskadit/iphonedjangotwitter/blob/master/2.png)

![alt text](https://github.com/sskadit/iphonedjangotwitter/blob/master/3.png)

![alt text](https://github.com/sskadit/iphonedjangotwitter/blob/master/4.png)





