import sys

def main():
    passwords={}
    while True:
        ch1 = input("Enter your email id  ")
        ch2 = input("Enter your microsoft account  ")
        ch3 = input("Enter your facebook account  ")
        passwords[ch1] = input("Enter your password of your email account  ")
        passwords[ch3] = input("Enter your password for your facebook account  ")
        passwords[ch2] = input("Enter your microsoft password  ")
        
        choice = input("Do you wish to continue. If so Type Y/N  ")
        if(choice.upper() == 'N'):
            printing(passwords)
            sys.exit(0)


def printing(passwords):
    for i in passwords.items():
        print(i)     

if __name__ == "__main__":
    main()


