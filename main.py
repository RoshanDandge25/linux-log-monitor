from monitor import failed_login, sudo_usage, new_user

def main():
    print("[*] Starting Linux Log Monitor...")
    
    # Run all three detectors
    failed_login.detect_failed_logins()
    sudo_usage.detect_sudo_usage()
    new_user.detect_new_users()
    
    print("[*] Monitoring completed.")

if __name__ == "__main__":
    main()

