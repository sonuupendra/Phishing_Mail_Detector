print("_____PHISHING MAIL DETECTOR_____")

#INPUT STAGE
def get_email_text():
    text_in_email = input("\nPlease enter the email content below.\n")
    print("Analyzing...")
    print("Email length:", len(text_in_email))
    return text_in_email

#ANALYSIS STAGE
def mail_analysis(text):
    suspicious_words = ["urgent", "click", "login", "verify"]
    found_suspicious_words = 0

    for word in suspicious_words:
        if word in text:
            found_suspicious_words += 1
    return found_suspicious_words



#DECISION MAKING STAGE
def risk_analysis(found_suspicious_words):
    if found_suspicious_words >= 2:
        return "LIKELY A PHISHING MAIL" 
       
    else:
        return "MAIL IS FINE, PLEASE GO AHEAD"


text_in_mail = get_email_text()
text = text_in_mail.lower()

found_suspicious_words = mail_analysis(text)
print("Suspicious Langauge Indicators found: ", found_suspicious_words)

risk_decision = risk_analysis(found_suspicious_words)
print(risk_decision)

def extract_links(text):
    words = text.split()
    links = []
    for word in words:
        clear_word = word.strip("().,")
        if clear_word.startswith("http"):
            links.append(clear_word)
    
    return links

links = extract_links(text)
if links:
    print("LINKS HAVE BEEN DETECTED IN THE MAIL")
    for link in links:
        print(" -",link)
else:
    print("NO LINKS DETECTED IN THE MAIL")
