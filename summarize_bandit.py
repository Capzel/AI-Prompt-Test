import os
import csv
import subprocess
from collections import defaultdict

# Paths
input_folder = "."  # current folder
folder_name = os.path.basename(os.path.abspath(input_folder))
output_csv = f"{folder_name}_summary_2.csv"

# Prepare output structure
summary = defaultdict(lambda: {"HIGH": 0, "MEDIUM": 0, "LOW": 0})

# Loop through all .py files
for filename in os.listdir(input_folder):
    if filename.endswith(".py") and filename != "summarize_bandit.py":
        print(f"Scanning: {filename}")
        filepath = os.path.join(input_folder, filename)
        sample_id = filename.replace(".py", "")

        # Run Bandit on each file, outputting CSV format
        bandit_cmd = ["bandit", "-f", "csv", "-o", "temp_result.csv", filepath]
        subprocess.run(bandit_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Ensure the file is in summary even if no issues found
        summary[sample_id]  # Initializes to zeroes

        # Parse Bandit CSV result
        with open("temp_result.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["issue_confidence"] in ["MEDIUM", "HIGH"]:
                    severity = row["issue_severity"]
                    summary[sample_id][severity] += 1

# Write summary CSV
with open(output_csv, "w", newline='') as csvfile:
    fieldnames = ["Sample ID", "High Severity", "Medium Severity", "Low Severity", "Total"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for sample_id, counts in summary.items():
        row = {
            "Sample ID": sample_id,
            "High Severity":  counts["HIGH"],
            "Medium Severity":  counts["MEDIUM"],
            "Low Severity":  counts["LOW"],
            "Total": counts["HIGH"] + counts["MEDIUM"] + counts["LOW"]
        }
        writer.writerow(row)

# Cleanup
if os.path.exists("temp_result.csv"):
    os.remove("temp_result.csv")

print(f"\nSummary written to: {output_csv}")