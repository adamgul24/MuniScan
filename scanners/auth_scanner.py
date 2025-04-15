import requests
from utils.logger import setup_logger

logger = setup_logger()

def scan_auth_weakness(target_url):
    login_endpoint = f"{target_url}/login"  # Adjust if different path
    credentials = [
        ("admin", "admin"),
        ("admin", "password"),
        ("user", "user"),
        ("test", "test"),
        ("admin", "123456")
    ]
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    risk_score = 7.5
    severity = "High"
    vulnerable = False

    for username, password in credentials:
        data = {"username": username, "password": password}
        try:
            response = requests.post(login_endpoint, data=data, headers=headers, timeout=5)
            if "welcome" in response.text.lower() or "dashboard" in response.url.lower():
                logger.info(f"Weak Auth Detected | URL: {login_endpoint} | Credentials: {username}/{password} | CVSS: {risk_score} | Severity: {severity}")
                vulnerable = True
                break
        except requests.exceptions.RequestException as e:
            logger.warning(f"Auth check failed for {login_endpoint} with {username}:{password} | Error: {e}")
    
    if not vulnerable:
        logger.info(f"No weak authentication detected for {login_endpoint}")
