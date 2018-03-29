import sqlite3

sqlite_file = 'media.sqlite'  # name of the sqlite database file
table_name = 'Track'  # name of the table
new_column = 'url'  # name of the new column
column_type = 'TEXT'
default_val = ''

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Adding a new column with a default row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'"\
        .format(tn=table_name, cn=new_column, ct=column_type, df=default_val))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()