import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"  # Change this to your SMTP server
    port = 587  # Change this to your SMTP port
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Create message container
        msg = MIMEMultipart('alternative')
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add body to email
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"Email sent to {recipient_email}")

        # Clean up the server connection
        server.quit()
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

def main():
    # Email credentials
    sender_email =# Change this to your email
    sender_password =# Change this to your password

    # Email parameters
    subject = "Personalized Email"
    body_template = "Hello {name},\n\nThis is a personalized email just for you!\n\nBest regards,\nYour Name"

    # Load recipient list from CSV file
    with open(r'C:\CodersCave\Phase2 Golden Task\Book1.csv', mode='r') as file:

        reader = csv.DictReader(file)
        for row in reader:
            recipient_email = row['email']
            recipient_name = row['name']
            personalized_body = body_template.format(name=recipient_name)
            send_email(sender_email, sender_password, recipient_email, subject, personalized_body)

if __name__ == "__main__":
    main()