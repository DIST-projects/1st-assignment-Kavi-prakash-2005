# ==========================================
# RPC CLIENT PROGRAM
# Runs on: Local Windows Machine
# Connects to: Azure VM RPC Server
# ==========================================

# requests module is used to send HTTP requests
import requests

# Public IP address of Azure VM
# Example: "http://20.xx.xx.xx:8000"
SERVER_IP = "http://52.237.81.179:8000"    # replace with your VM IP


# Input text for RPC operations
text = "Never odd or even"


# -------- RPC CALL 1 --------
# Calls remote word_count procedure
r1 = requests.post(
    SERVER_IP + "/word_count",
    json={"text": text}
)
print("Word Count:", r1.json()["result"])


# -------- RPC CALL 2 --------
# Calls remote reverse_text procedure
r2 = requests.post(
    SERVER_IP + "/reverse_text",
    json={"text": text}
)
print("Reversed Text:", r2.json()["result"])


# -------- RPC CALL 3 --------
# Calls remote is_palindrome procedure
r3 = requests.post(
    SERVER_IP + "/is_palindrome",
    json={"text": text}
)
print("Is Palindrome:", r3.json()["result"])
