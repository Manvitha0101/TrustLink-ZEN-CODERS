# TrustLink - Simple Demo Script
# Team ZEN CODERS

def check_url(url):
    suspicious_keywords = ["free", "offer", "crypto", "login", "verify", "update", "lottery"]
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            return "Suspicious Link Detected"
    return "Safe Link"

if __name__ == "__main__":
    print("TrustLink - AI-Powered Fraud Detection (Demo)")
    print("------------------------------------------------")
    url = input("Enter a website URL: ")
    result = check_url(url)
    print("Result:", result)
