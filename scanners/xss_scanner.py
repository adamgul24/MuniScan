import requests
from utils.logger import setup_logger

logger = setup_logger()

def scan_xss(target_url):
    payloads = [
        "<script>alert('XSS')</script>",
        "\"><script>alert(1)</script>",
        "'><img src=x onerror=alert('XSS')>"
    ]
    risk_score = 6.1
    severity = "Medium"
    vulnerable = False

    for payload in payloads:
        try:
            params = {'input': payload}
            response = requests.get(target_url, params=params, timeout=5)

            if payload in response.text:
                logger.info(f"XSS Detected | URL: {response.url} | Payload: {payload} | CVSS: {risk_score} | Severity: {severity}")
                vulnerable = True
        except requests.exceptions.RequestException as e:
            logger.warning(f"Request failed for {target_url} with payload {payload}: {e}")
    
    if not vulnerable:
        logger.info(f"No XSS vulnerabilities detected for {target_url}")
