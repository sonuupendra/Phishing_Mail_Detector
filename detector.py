print("_____PHISHING MAIL DETECTOR_____")

#INPUT STAGE
text_in_email = input("\nPlease enter the email content below.\n")

print("Analyzing...")
print("Email length:", len(text_in_email))

text = text_in_email.lower()

#ANALYSIS STAGE
suspicious_words = ["urgent", "click", "login", "verify"]

found_suspicious_words = 0

for word in suspicious_words:
    if word in text:
        found_suspicious_words += 1

print("Suspicious Langauge Indicators found: ", found_suspicious_words)

#DECISION MAKING STAGE
if found_suspicious_words >= 2:
    print("LIKELY A PHISHING MAIL")
else:
    print("MAIL IS FINE, PLEASE GO AHEAD")