# slice the email in to username and domain and super domain

def main():
    print('Welcome to the email slicer.')
    user_email = input("Enter your email: ")
    (username,domain) = user_email.split('@')
    (domain,extension) = domain.split('.')

    print('Username: ', username)
    print('Domain: ', domain)
    print('Extension: ', extension)

while True:
    main()