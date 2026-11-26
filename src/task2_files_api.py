
# Task 2: File Handling, APIs and Environment Variables

import csv
import json
import os
import requests
from dotenv import load_dotenv

# 1. Read employees.csv and create employees.json
employees = []

with open("task2/employees.csv", "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["salary"] = int(row["salary"])
        employees.append(row)

print("Rows read:", len(employees))

with open("task2/employees.json", "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)

# 2. Create high_earners.csv
high_earners = [
    emp for emp in employees
    if emp["salary"] > 50000
]

with open("task2/high_earners.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=employees[0].keys())
    writer.writeheader()
    writer.writerows(high_earners)

print("High earners:", len(high_earners))

# 3. Load environment variables from .env
load_dotenv("task2/.env")

api_key = os.getenv("API_KEY")
print("API key loaded:", "Yes" if api_key else "No")

# 4. Fetch users from API
url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    users = response.json()

    print("\nFirst 3 users:")
    for user in users[:3]:
        print(user["id"], user["name"], user["email"])

    # Save users.json
    with open("task2/users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

    # 5. Parse nested JSON using get()
    first_user = users[0]
    company_name = first_user.get("company", {}).get("name", "Unknown")
    city = first_user.get("address", {}).get("city", "Unknown")

    print("\nCompany:", company_name)
    print("City:", city)

except requests.exceptions.Timeout:
    print("Error: API request timed out")

except requests.exceptions.ConnectionError:
    print("Error: Connection failed")

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)

except requests.exceptions.RequestException as error:
    print("Request Error:", error)

# 6. Test 404 error handling
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999",
        timeout=5
    )

    if response.status_code == 404:
        print("\n/users/9999 -> 404 Not found")
    else:
        response.raise_for_status()

except requests.exceptions.RequestException as error:
    print("404 test request error:", error)
