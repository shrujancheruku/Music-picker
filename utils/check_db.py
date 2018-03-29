import app
import sqlite3
import get_url

# Connecting to the database file
conn = app.create_connection()
cursor = conn.cursor()

tracks = app.select_all_tracks(conn)
for track in tracks:
    if track[9] is "":
        _id = get_url.youtube_search(track[1])
        if _id is None:
            continue
        url = '"' + _id + '"'
        cursor.execute("UPDATE {tn} SET {cn}={url} WHERE {idf}={track_id}".
                       format(tn="Track", cn="url", idf="TrackId", url=url, track_id=track[0]))
        conn.commit()

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()
