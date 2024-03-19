import mysql.connector
import smtplib

# Connect to MySQL database
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@1234',
    database='citysanitizationdb'
)

# Fetch the latest application of sanitization pincode
cursor = db.cursor()
cursor.execute('SELECT city FROM sanitizationapply ORDER BY id DESC LIMIT 1')
latest_city = cursor.fetchone()[0]

# Compare the latest application of sanitization pincode with the whole pincode column of volunteer
cursor.execute("SELECT email FROM volunteers WHERE city=%s", (latest_city,))
selected_volunteers = cursor.fetchall()

# Send an email to the selected volunteer(s)
for volunteer in selected_volunteers:
    to_addr = volunteer[0]
    subject = 'You have been selected for the sanitization job'
    body = 'Congratulations! You have been selected for the sanitization job. Please contact us for further details.'

    # Connect to SMTP server and send email
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'CleanHire04@gmail.com'
    smtp_password = 'fsewlzhnbjyhbixz'

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    msg = f'To: {to_addr}\nSubject: {subject}\n\n{body}'
    server.sendmail(smtp_username, to_addr, msg)

    server.quit()

# Close MySQL database connection
db.close()
