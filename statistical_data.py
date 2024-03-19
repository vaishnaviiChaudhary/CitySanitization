from curses import window
from sys import winver
from tkinter import Button
import mysql.connector
import matplotlib.pyplot as plt

# Connect to the database
cnx = mysql.connector.connect(user='root', password='root@1234',
                              host='localhost', database='citysanitizationdb')
cursor = cnx.cursor()

# Query the data
query = ("SELECT city, COUNT(*) FROM sanitizationapply GROUP BY city")
cursor.execute(query)
data = cursor.fetchall()
labels = [row[0] for row in data]
values = [row[1] for row in data]

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct='%1.1f%%')
ax.axis('equal')
plt.title('Cities with Sanitizations')

# Show the chart
plt.show()

# Close the database connection
cursor.close()
cnx.close()