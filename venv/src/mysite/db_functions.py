import sqlite3

db_location = "/db-mount/db.sqlite3"
table = "coords"


def _db_connect():
    # Connect to db
    conn = sqlite3.connect(db_location)
    cursor = conn.cursor()

    # Return connection and cursor objects
    return conn, cursor


def create_table():
    # Get db connection and cursor objects
    conn, cursor = _db_connect()

    cursor.execute("CREATE TABLE IF NOT EXISTS " + table + " (id INTEGER, latitude DECIMAL, longitude DECIMAL);")

    # Close db connection
    conn.commit()
    conn.close()
    return


def get_coords_from_db():
    
    # Get db connection and cursor objects
    conn, cursor = _db_connect()

    # Get latitude and longitude from coords table
    cursor.execute("SELECT COUNT(*) AS RowCnt FROM " + table + ";")
    if (cursor.fetchone()[0] > 0):
        cursor.execute("SELECT latitude FROM " + table + " WHERE id=1;")
        latitude = cursor.fetchone()[0]
        cursor.execute("SELECT longitude FROM " + table + " WHERE id=1;")
        longitude = cursor.fetchone()[0]
    else:
        return "N/A"
    
    # Close db connection
    conn.commit()
    conn.close()
    
    return "(" + str(latitude) + ", " + str(longitude) + ")"
    
    

def remove_and_replace_coords(latitude, longitude):
    
    # Get db connection and cursor objects
    conn, cursor = _db_connect()

    # Check if anything exists in db already, if so, remove
    cursor.execute("SELECT COUNT(*) AS RowCnt FROM " + table + ";")
    if (cursor.fetchone()[0] > 0):
        cursor.execute("DELETE FROM " + table + " WHERE id=1;")

    # Insert a row of data
    cursor.execute("INSERT INTO " + table + " VALUES ('1', " + str(latitude) + ", " + str(longitude) + ");")

    # Close db connection
    conn.commit()
    conn.close()
    
    return