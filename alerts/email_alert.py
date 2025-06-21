import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, body, to_email):
    from_email = "roshan.log.monitor.project@gmail.com"  # Replace with your Gmail
    from_password = "npzlfenwqeoomyvw"  # Use an App Password if 2FA is enabled

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, from_password)
        server.send_message(msg)
        server.quit()
        print("[+] Email alert sent.")
    except Exception as e:
        print(f"[!] Failed to send email: {e}")
