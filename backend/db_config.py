import mysql.connector

# Connect to the MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="ipl_cricket"
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Example: Execute a query
cursor.execute("SELECT * FROM teams")

# Fetch the results
results = cursor.fetchall()
print(results)

# Do something with the results (e.g., print them)
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
