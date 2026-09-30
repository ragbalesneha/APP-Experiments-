import re
text = """
Hello students!
for any queries , contact abc@gmail.com or teacher123@college.edu.
You can also contact support@yahoo.com.
"""
email_pattren = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattren, text)
print("Email addresses found:")
for email in emails:
    print(email)