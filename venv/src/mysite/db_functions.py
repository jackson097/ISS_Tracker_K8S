import sqlite3

db_location = "/db-mount/db.sqlite3"

def get_coords_from_db():
    # Connect to db
    conn = sqlite3.connect(db_location)
    cursor = conn.cursor()

    # Get latitude and longitude from coords table
    cursor.execute("SELECT COUNT(*) AS RowCnt FROM coords;")
    if (cursor.fetchone()[0] > 0):
        cursor.execute("SELECT latitude FROM coords WHERE id=1;")
        latitude = cursor.fetchone()[0]
        cursor.execute("SELECT longitude FROM coords WHERE id=1;")
        longitude = cursor.fetchone()[0]
    else:
        return "N/A"
    
    # Close db connection
    conn.commit()
    conn.close()
    
    return "(" + str(latitude) + ", " + str(longitude) + ")"
    
    

def remove_and_replace_coords(latitude, longitude):
    # Connect to db
    conn = sqlite3.connect(db_location)
    cursor = conn.cursor()

    # Check if anything exists in db already, if so, remove
    cursor.execute("SELECT COUNT(*) AS RowCnt FROM coords;")
    if (cursor.fetchone()[0] > 0):
        cursor.execute("DELETE FROM coords WHERE id=1;")

    # Insert a row of data
    cursor.execute("INSERT INTO coords VALUES ('1', " + str(latitude) + ", " + str(longitude) + ");")

    # Close db connection
    conn.commit()
    conn.close()
    
    return