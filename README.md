# linux-log-monitor


TITLE : => Linux Log Monitor with Email Alerts

A lightweight and effective Linux log monitoring tool that scans for:

- ❌ Failed login attempts  
- ⚠️ Unauthorized sudo usage  
- 🆕 Suspicious new user creation  
- sends real-time email alerts while also logging all activities locally.

---

 ✅ Features
- 🔍 Detect failed login attempts from `/var/log/auth.log`
- 🔐 Monitor usage of `sudo` commands
- 👤 Track the creation of new user accounts
- 📧 Instantly send email alerts to your configured address
- 📝 Log all alerts to a file: `logs/suspicious_activity.log`
- 🔁 Fully automatable using `cron` (set to run every 15 minutes)

---

## 💻 System Requirements

| Component         | Requirement                          |
|------------------|--------------------------------------|
| Virtual Machine   | 1 Linux VM (Ubuntu/Debian preferred) |
| RAM               | Minimum 2 GB                         |
| OS                | Ubuntu 20.04+ / Debian 11+           |
| Python Version    | Python 3.6 or higher                 |
| Required Tools    | `cron`, `mailutils` (optional)       |
| Log Source        | `/var/log/auth.log`                  |
| Internet          | Required for sending email alerts    |

---
## 📁 Project Structure

linux-log-monitor/
├── alerts/
│ └── email_alert.py
├── logs/
│ └── suspicious_activity.log
├── monitor/
│ ├── failed_login.py
│ ├── sudo_usage.py
│ └── new_user.py
├── main.py
├── requirements.txt
└── README.md



🙏 Usage & Permission Note
If you wish to use, modify, or distribute this project:

📧 Please contact me if any qwery (roshandandge25@gmail.com).
✉️ Make sure to update the email address in alerts/email_alert.py with your own before using the script.
✉️ Feel free to reach out via GitHub or the email listed in the repo.
💡 Suggestions for Improvement

👨‍💻 Roshan Dandge
