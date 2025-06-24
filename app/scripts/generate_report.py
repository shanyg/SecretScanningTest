import csv

# Dummy API Key for a hypothetical reporting service
REPORTING_API_KEY = "rep_DUMMY_REPORTING_API_KEY_ABCDEF123456"

def generate_csv_report(data, filename="report.csv"):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = data[0].keys() if data else []
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Report '{filename}' generated successfully.")

# Dummy PGP Private Key Block (simulating embedded key)
# In reality, these are usually files, but can be embedded.
DUMMY_PGP_PRIVATE_KEY_BLOCK = """-----BEGIN PGP PRIVATE KEY BLOCK-----
xcVBNYtGg0IBMwoBApYRYzYOUR_DUMMY_PGP_PRIVATE_KEY_CONTENT_FOR_TESTING
-----END PGP PRIVATE KEY BLOCK-----"""

if __name__ == "__main__":
    sample_data = [
        {"id": 1, "name": "Item A", "value": 100},
        {"id": 2, "name": "Item B", "value": 200},
    ]
    generate_csv_report(sample_data)
    print(f"Reporting API Key (dummy): {REPORTING_API_KEY}")
    print("PGP Key (dummy, first 20 chars):", DUMMY_PGP_PRIVATE_KEY_BLOCK[:20])
