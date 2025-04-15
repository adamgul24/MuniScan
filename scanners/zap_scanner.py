import time
from zapv2 import ZAPv2
from utils.logger import setup_logger
from utils.results import save_result

logger = setup_logger()

API_KEY = 'changeme'  # Set this to your actual API key if needed
ZAP_ADDRESS = 'localhost'
ZAP_PORT = '8080'
ZAP_URL = f'http://{ZAP_ADDRESS}:{ZAP_PORT}'

zap = ZAPv2(apikey=API_KEY, proxies={'http': ZAP_URL, 'https': ZAP_URL})

def scan_with_zap(target):
    logger.info(f"ZAP: Starting passive scan on {target}")
    zap.urlopen(target)
    time.sleep(2)  # Give ZAP some time to register the site

    logger.info(f"ZAP: Starting active scan on {target}")
    scan_id = zap.ascan.scan(target)
    while int(zap.ascan.status(scan_id)) < 100:
        logger.info(f"ZAP: Scanning {target}... {zap.ascan.status(scan_id)}% complete")
        time.sleep(2)

    alerts = zap.core.alerts(baseurl=target)
    for alert in alerts:
        vuln_type = alert.get("alert")
        url = alert.get("url")
        risk = alert.get("risk")
        confidence = alert.get("confidence")
        desc = alert.get("description")
        cvss = 6.0  # Default score (could be improved later)
        severity = risk.capitalize()

        logger.info(f"ZAP Alert | {vuln_type} | URL: {url} | Risk: {risk} | Confidence: {confidence}")
        save_result(vuln_type, url, desc, severity, cvss)
