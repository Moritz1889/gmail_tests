import time
from gmail_login import run as run_gmail_login
from gmail_login_failure import run as run_gmail_login_failure

while True:
    run_gmail_login()
    time.sleep(10)

    run_gmail_login_failure()
    time.sleep(10)