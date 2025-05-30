import os
import csv
import subprocess
from collections import defaultdict

# Paths
input_folder = "."
folder_name = os.path.basename(os.path.abspath(input_folder))
output_csv = f"{folder_name}_detailed_summary.csv"

# Severity × Confidence combinations
severity_levels = ["LOW", "MEDIUM", "HIGH"]
confidence_levels = ["LOW", "MEDIUM", "HIGH"]

# Create summary structure
summary = defaultdict(lambda: {
    f"{sev}_{conf}": 0 for sev in severity_levels for conf in confidence_levels
})

# Scan files
for filename in os.listdir(input_folder):
    if filename.endswith(".py") and filename != "summarize_bandit.py":
        print(f"Scanning: {filename}")
        filepath = os.path.join(input_folder, filename)
        sample_id = filename.replace(".py", "")

        # Run Bandit
        bandit_cmd = ["bandit", "-f", "csv", "-o", "temp_result.csv", filepath]
        subprocess.run(bandit_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        summary[sample_id]  # Initialize entry

        # Parse result
        with open("temp_result.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sev = row["issue_severity"]
                conf = row["issue_confidence"]
                key = f"{sev}_{conf}"
                if key in summary[sample_id]:
                    summary[sample_id][key] += 1

# Write CSV with descriptive headers
with open(output_csv, "w", newline='') as csvfile:
    # Create clear column names
    matrix_headers = [
        f"Severity: {sev} / Confidence: {conf}"
        for sev in severity_levels for conf in confidence_levels
    ]
    fieldnames = ["Sample ID"] + matrix_headers + ["Total /w LOW CONF"]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for sample_id, counts in summary.items():
        row = {"Sample ID": sample_id}
        total = 0
        for sev in severity_levels:
            for conf in confidence_levels:
                key = f"{sev}_{conf}"
                header = f"Severity: {sev} / Confidence: {conf}"
                row[header] = counts[key]
                total += counts[key]
        row["Total /w LOW CONF"] = total
        writer.writerow(row)

# Cleanup
if os.path.exists("temp_result.csv"):
    os.remove("temp_result.csv")

print(f"\nDetailed summary written to: {output_csv}")
