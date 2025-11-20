# Simple Spam / Fraud Call Detection Program

spam_keywords = [
    "lottery", "prize", "winner", "free", "loan", "credit card",
    "insurance", "offer", "otp", "bank", "atm", "fraud", "money",
    "gift", "cashback", "claim", "verification"
]

message = input("Enter the caller message: ").lower()

is_spam = False

for word in spam_keywords:
    if word in message:
        is_spam = True
        break

if is_spam:
    print("⚠️ This call might be SPAM or FRAUD!")
else:
    print("✔ This call looks safe.")
