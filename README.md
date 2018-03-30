Music Picker
===============

This is a Flask webapp built on top of a sqlite3 database. Allows playing of songs from YouTube, as well as querying.

Run with `python3 app.py`

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
