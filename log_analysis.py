from collections import Counter

# Sample log data
logs = [
    "Failed password from 192.168.1.10",
    "Failed password from 192.168.1.10",
    "Accepted password from 192.168.1.5",
    "Failed password from 192.168.1.20",
    "Failed password from 192.168.1.10",
    "Failed password from 192.168.1.20",
]

failed_ips = []

# Extract failed login IPs
for log in logs:
    if "Failed password" in log:
        ip = log.split("from ")[1]
        failed_ips.append(ip)

# Count occurrences
ip_counts = Counter(failed_ips)

# Detect suspicious IPs
print("Suspicious IPs (more than 2 failed attempts):")
for ip, count in ip_counts.items():
    if count > 2:
        print(f"{ip} → {count} failed attempts")
