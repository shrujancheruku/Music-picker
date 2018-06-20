Music Picker
===============

12 hour take-home project. The only requirement was to use the given sqlite3 database. This required learning SQL, as well as understanding the YouTube API to obtain video info.

This is a Flask webapp built on top of a sqlite3 database. Allows playing of songs from YouTube, as well as querying.
It's responsive thanks to Bootstrap4, that I used on top of the Jinja2 templating engine. Try resizing the window to see!<br/>

Run with <br/>
```
export FLASK_APP=app.py
flask run
```
<br/>
The app should run on http://127.0.0.1:5000/

Completed Functionality
-------------

* Obtaining Video ID from YouTube API
* Displaying random videos on the homepage
* Allowing the user to select a genre of music
* Allowing searches by Artist, Track or Album
* *Adding new songs to the DB* (see below)

Things to Work On
-------------

* Querying YouTube for more metadata when adding new songs
* Allow user to select correct video from options when adding song
* Better playlist organization under the playing video
* Better animation (shading active video, hover effects, transitions)
* Account for input errors in search terms

Packages Required
----------------

* Python3
* Flask
* sqlite3
* flask-wtf
