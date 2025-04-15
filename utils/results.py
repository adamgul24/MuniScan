import json
import csv
from datetime import datetime

results = []

def save_result(vuln_type, url, payload, severity, score):
    results.append({
        "timestamp": datetime.now().isoformat(),
        "type": vuln_type,
        "url": url,
        "payload": payload,
        "severity": severity,
        "cvss": score
    })

def export_results():
    with open("results.json", "w") as f:
        json.dump(results, f, indent=4)
    
    with open("results.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "type", "url", "payload", "severity", "cvss"])
        writer.writeheader()
        writer.writerows(results)
