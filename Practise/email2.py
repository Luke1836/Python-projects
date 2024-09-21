import re as r 

def main():

    email = input("What's your email address ").strip()

    if r.search(r"^[\w|\.]+@[\w|\.]*\w+\.edu$", email, r.IGNORECASE):
        print("VALID")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
