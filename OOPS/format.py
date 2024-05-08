import re as r

def main():
    name = input("What's your name? ").strip()
    matches = r.search(r"^(\w+), *(\w+)$", name) #We can use ? or * to clean up the space accordingly
    if matches:
        name = matches.group(2) + " " +  matches.group(1)
 
    print(f"Hello, {name}")
    

if __name__ == "__main__":
    main()