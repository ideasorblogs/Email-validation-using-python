import re

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(email_pattern, email):
        return True
    else:
        return False

def check_emails(emails):
    valid_emails = []
    invalid_emails = []

    for email in emails:
        if is_valid_email(email):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)

    return valid_emails, invalid_emails

if __name__ == '__main__':

    email_input = input("Enter an email address or tyoe 'fie' to choose a list of email: ")

    if email_input.lower() == 'file':
        file_path = input("Enter the path to the email list: ")

        try:
            with open(file_path, 'r') as file:
                email_list = file.read().splitlines()

        except FileNotFoundError:
            print("File not found. Please check the file path and try again")
            exit(1)

    else:
        email_list = [email_input]

    valid_emails,invalid_emails = check_emails(email_list)

    print("\nValid email addressess: ")

    for email in valid_emails:
        print(email)


print("\nInvalid email addresses")
for email in invalid_emails:
    print(email)

        