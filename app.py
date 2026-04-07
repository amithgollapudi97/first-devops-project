import requests

print("Starting app...")

response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)
print("Automation Level 2 working 🚀")
