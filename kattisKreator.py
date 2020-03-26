import sys

def main():

    # Case where the problem ID is not given by command line. 
    if len(sys.argv) == 1:
        probID = input("ID not given. Please enter the Problem's ID: ")

    else:
        probID = sys.argv[1]

    # Programming extension, will be changeable
    ex = "py"
    comment = "#"
    
    name = "{}.{}".format(probID, ex)
    with open(name, "w") as file:
        file.write("{} Program descirption at https://open.kattis.com/{}\n\n".format(comment, probID))


if __name__ == "__main__":
    main()