
def main():
    username , domain = input("Enter your email address  ").strip().split('@')

    if domain.endswith(".com"):
        print("VALID")
    else:
        print("Not valid") 



if __name__ == "__main__":
    main()