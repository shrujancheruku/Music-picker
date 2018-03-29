import app

table_name = 'Track'  # name of the table
new_column = 'url'  # name of the new column
column_type = 'TEXT'
default_val = ''

# Connecting to the database file
conn = app.create_connection()
cursor = conn.cursor()

# Adding a new column with a default row value
cursor.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'"\
        .format(tn=table_name, cn=new_column, ct=column_type, df=default_val))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()