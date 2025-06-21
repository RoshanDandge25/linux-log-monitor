import os
import sys
from datetime import datetime

# Fix path to alerts/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'alerts')))
from email_alert import send_email_alert

LOG_PATH = "/var/log/auth.log"
OUTPUT_LOG = os.path.join(os.path.dirname(__file__), "../logs/suspicious_activity.log")

def detect_sudo_usage():
    if not os.path.exists(LOG_PATH):
        print(f"[!] Log file {LOG_PATH} not found.")
        return

    with open(LOG_PATH, "r") as f:
        lines = f.readlines()

    sudo_lines = [line for line in lines if "sudo:" in line and "COMMAND=" in line]
    
    if sudo_lines:
        os.makedirs(os.path.dirname(OUTPUT_LOG), exist_ok=True)
        with open(OUTPUT_LOG, "a") as out:
            out.write(f"\n--- Sudo command usage on {datetime.now()} ---\n")
            for line in sudo_lines[-5:]:
                out.write(line)
        
        print("[+] Sudo usage logged.")

        subject = "Alert: Sudo Commands Executed"
        body = f"The following sudo commands were recently run:\n\n{''.join(sudo_lines[-5:])}"
        send_email_alert(subject, body, "roshan.log.monitor.project@gmail.com")
    else:
        print("[i] No sudo usage found.")

if __name__ == "__main__":
    detect_sudo_usage()

