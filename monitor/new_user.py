import os
import sys
from datetime import datetime

# Correctly import email_alert.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'alerts')))
from email_alert import send_email_alert

LOG_PATH = "/var/log/auth.log"
OUTPUT_LOG = os.path.join(os.path.dirname(__file__), "../logs/suspicious_activity.log")

def detect_new_users():
    if not os.path.exists(LOG_PATH):
        print(f"[!] Log file {LOG_PATH} not found.")
        return

    with open(LOG_PATH, "r") as log:
        lines = log.readlines()

    new_user_lines = [line for line in lines if "useradd" in line or "new user" in line]

    if new_user_lines:
        os.makedirs(os.path.dirname(OUTPUT_LOG), exist_ok=True)
        with open(OUTPUT_LOG, "a") as out:
            out.write(f"\n--- New user creation detected on {datetime.now()} ---\n")
            for line in new_user_lines[-5:]:
                out.write(line)

        print("[+] New user creation logged.")

        subject = "Alert: New User Account Created"
        body = f"The following new user activity was detected:\n\n{''.join(new_user_lines[-5:])}"
        send_email_alert(subject, body, "roshan.log.monitor.project@gmail.com")
    else:
        print("[i] No new user creation found.")

if __name__ == "__main__":
    detect_new_users()

