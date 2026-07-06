import re

def detect_phishing(url):
    phishing_score = 0

    # Check for IP address in URL
    if re.search(r'https?://\d+\.\d+\.\d+\.\d+', url):
        phishing_score += 1

    # Check for @ symbol
    if '@' in url:
        phishing_score += 1

    # Check for multiple hyphens
    if '-' in url:
        phishing_score += 1

    # Check URL length
    if len(url) > 50:
        phishing_score += 1

    if phishing_score >= 2:
        return "Suspicious Website (Possible Phishing)"
    else:
        return "Safe Website"

url = input("Enter Website URL: ")
result = detect_phishing(url)

print("\nAnalysis Result:")
print(result)
