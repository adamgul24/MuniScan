
# MuniScan 🛡️ - Automated Web Vulnerability Scanner for Municipal Web Applications

## Overview
MuniScan is an automated vulnerability scanning tool specifically designed for assessing the security posture of municipal web applications. It integrates multiple scanners, including custom SQLi, XSS, authentication weakness checkers, OWASP ZAP active/passive scans, and Burp Suite result parsing.

## Folder Structure
```
MuniScan/
├── config/
│   └── targets.txt                 # 🔗 List of municipal app targets
│
├── scanners/
│   ├── sqli_scanner.py            # 🔐 SQL Injection scanner
│   ├── xss_scanner.py             # 🧪 XSS vulnerability scanner
│   ├── auth_scanner.py            # 🔑 Weak credential/authentication scanner
│   ├── zap_scanner.py             # ⚡ ZAP API active/passive scanner
│   └── burp_parser.py             # 🧠 Parses Burp Suite XML exports into results
│
├── utils/
│   ├── logger.py                  # 📋 Logger setup for scanning operations
│   └── results.py                 # 📊 Handles CVSS scoring + exporting results
│
├── muniscan.py                    # 🚀 Entry point — runs all scans and exports
├── requirements.txt               # 📦 Required Python libraries
├── README.md                      # 📝 Project overview and instructions
│
├── output/                        # 🗂️ Output folder for scan results and logs
│   ├── muniscan.log               # 📜 Full scan log with timestamps, actions, payloads
│   ├── results.json               # 📁 Structured output for report generation
│   ├── results.csv                # 📑 Table format for screenshots/charts
│   ├── burp_results.json          # 📄 Parsed Burp Suite findings (JSON)
│   └── burp_results.csv           # 📄 Parsed Burp Suite findings (CSV)
```

## Usage Instructions

1. **Install Required Libraries:**
```bash
pip install -r requirements.txt
```

2. **Add Your Target Applications:**
Edit `config/targets.txt` and list your target URLs (one per line). 
Example:
```
http://water.cyberapolis.gov/
http://www.capower.com/
```

3. **Run the Scanner:**
```bash
python muniscan.py
```

4. **View Results:**
- Results are saved to the `output/` folder as JSON and CSV.
- Logs are available in `muniscan.log`.

## Notes
- Ensure ZAP and Burp Suite are properly configured.
- Replace the ZAP API key in `zap_scanner.py` with your actual key.

## Disclaimer
This tool is intended for authorized testing only. Use responsibly and ethically within the scope of your engagement.
