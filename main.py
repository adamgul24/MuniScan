from utils.logger import setup_logger
from scanners.sqli_scanner import scan_sql_injection
from scanners.xss_scanner import scan_xss
from scanners.auth_scanner import scan_auth_weakness
from scanners.zap_scanner import scan_with_zap
from utils.results import export_results

def load_targets(file_path='config/targets.txt'):
    with open(file_path) as f:
        return [line.strip() for line in f if line.strip()]

def main():
    logger = setup_logger()
    targets = load_targets()
    
    for url in targets:
        logger.info(f"Starting scans for: {url}")
        scan_sql_injection(url)
        scan_xss(url)
        scan_auth_weakness(url)
        scan_with_zap(url)

    export_results()

if __name__ == "__main__":
    main()
