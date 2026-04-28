# Failed Login Detection

## Description
Detects multiple failed login attempts from a single IP.

## SPL Query
"failed password" | stats count by src_ip

## Why It Matters
Repeated failures may indicate brute-force attacks.
