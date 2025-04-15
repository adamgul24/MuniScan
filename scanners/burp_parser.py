import xml.etree.ElementTree as ET
import json
import csv
from datetime import datetime

def parse_burp_xml(xml_file, output_json='burp_results.json', output_csv='burp_results.csv'):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    issues = []

    for issue in root.findall(".//issue"):
        item = {
            "timestamp": datetime.now().isoformat(),
            "type": issue.findtext("name"),
            "url": issue.findtext("host"),
            "payload": issue.findtext("path") or "",
            "severity": issue.findtext("severity") or "Unknown",
            "cvss": 6.0  # Default score; adjust manually if needed
        }
        issues.append(item)

    # Export to JSON
    with open(output_json, 'w') as f:
        json.dump(issues, f, indent=4)

    # Export to CSV
    with open(output_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "type", "url", "payload", "severity", "cvss"])
        writer.writeheader()
        writer.writerows(issues)

    print(f"Exported {len(issues)} Burp issues to {output_json} and {output_csv}")

# Example usage:
# parse_burp_xml('burp_output.xml')
