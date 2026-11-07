# SOC-Tools - 3 Tools by Ayesha
Day 30 Demo - SOC Level 1 Analyst Project

Aspiring SOC Analyst | Python | Cybersecurity

## Tool 1: Log Analyzer
Checks system logs and finds failed login attempts. If failed logins are too many, it gives a BruteForce Attack Alert.

Run: `python log_analyzer.py`

## Tool 2: IP Checker
Checks if an IP is malicious using VirusTotal API. It shows Owner, Malicious count and Result - Safe / Suspicious / Malicious. And saves report in CSV file.

Run: `python ip_checker.py`
Note: Add your own VirusTotal API Key in the code.

## Tool 3: File Integrity Checker
My best tool. It creates a Golden Hash of files. If any new file is added or any file is changed, it gives [ALERT] / [NEW] / [Safe].

Run: `python checkk_folder.py`

## Skills
Python, SOC Monitoring, Log Analysis, Threat Detection, VirusTotal API, File Integrity Monitoring

Created by: Ayesha - SOC Analyst Trainee
Day: 30 / 40
