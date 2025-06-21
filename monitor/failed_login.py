import sys
import os
from datetime import datetime

# Import email alert module
import importlib.util

alerts_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../alerts/email_alert.py"))
spec = importlib.util.spec_from_file_location("email_alert", alerts_path)
email_alert = importlib.util.module_from_spec(spec)
spec.loader.exec_module(email_alert)
send_email_alert = email_alert.send_email_alert


LOG_PATH = "/var/log/auth.log"
OUTPUT_LOG = os.path.join(os.path.dirname(__file__), "../logs/suspicious_activity.log")

def detect_failed_logins():
    if not os.path.exists(LOG_PATH):
        print(f"[!] Log file {LOG_PATH} not found.")
        return

    with open(LOG_PATH, "r") as log_file:
        lines = log_file.readlines()

    failed_logins = [line for line in lines if "Failed password" in line or "authentication failure" in line]

    if failed_logins:
        # Write to log file
        os.makedirs(os.path.dirname(OUTPUT_LOG), exist_ok=True)
        with open(OUTPUT_LOG, "a") as out:
            out.write(f"\n--- Failed login attempts on {datetime.now()} ---\n")
            for line in failed_logins[-5:]:
                out.write(line)

        print("[+] Failed login attempts logged.")

        # Send email alert
        subject = "Alert: Failed Login Attempts Detected"
        body = f"The following failed logins were found:\n\n{''.join(failed_logins[-5:])}"
        send_email_alert(subject, body, "roshan.log.monitor.project@gmail.com")

    else:
        print("[i] No failed logins found.")

if __name__ == "__main__":
    detect_failed_logins()

