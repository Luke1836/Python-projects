import random as r 

def main():
    names = []
    
    for i in range(0, 5, 1):
        names.append(input("Enter the names of your friends ")) 

    names.sort(key = str.upper , reverse=True)

    for i in range(0, 5, 1):
        print(names[i])

    print("hello"*3)

    print(names[r.randint(0, len(names)-1)])
if __name__ == "__main__":
    main()