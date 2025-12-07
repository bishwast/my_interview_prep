# 🛡️ Automated Threat Intelligence Tool

## Project Overview
This tool automates the process of **Target Verification** for SOC Analysts. It accepts an IP address, validates the format, and queries the **AbuseIPDB** database to determine if the IP has a history of malicious activity.

It is designed to reduce the "Mean Time to Detect" (MTTD) by allowing analysts to quickly check IPs directly from the CLI without navigating web interfaces.

## ⚡ Features
* **API Integration:** Connects securely to the AbuseIPDB v2 API.
* **Input Validation:** Uses the `ipaddress` library to prevent invalid input and injection errors.
* **JSON Parsing:** Automatically extracts and formats key threat metrics (Abuse Score, ISP, Country).
* **Secure Configuration:** Uses a separated `config.py` file to protect API credentials.

## 🛠️ Skills Used
* **Language:** Python 3.12
* **Libraries:** `requests`, `json`, `ipaddress`
* **Concept:** RESTful API Consumption & Error Handling

## 🚀 How to Run
1.  **Install Dependencies:**
    ```bash
    pip install requests
    ```
2.  **Setup Configuration:**
    Create a file named `config.py` in the same directory and add your key:
    ```python
    ABUSE_IPDB_KEY = "YOUR_API_KEY_HERE"
    ```
3.  **Run the Tool:**
    ```bash
    python threat_check.py
    ```

## 📊 Sample Output
```text
Enter an IP address to scan: 118.25.6.39
✅ Valid IP detected: 118.25.6.39
Connecting to AbuseIPDB...

--- SUCCESS! THREAT REPORT BELOW ---
Abuse Confidence Score: 100%
ISP: Tencent Cloud Computing
Last Reported: 2024-01-05
