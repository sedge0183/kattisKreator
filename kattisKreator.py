# --------------------------------------------------

# Program to create files for Kattis questions
# Creates a file with the questions URL commented on the top line 
# Requires ID of Kattis question by command line in standard input
# You can also give which programming language you would like to use

# --- How to call ---
# python3 kattisKreator.py {ID*} {Language*}

# * is optional
# You will be asked to enter ID through standard input if not given
# If language not given, default language is used (see deafault variable)

# --------------------------------------------------

import sys

# dictionary to store data on all compatible langauges
# langauge -> (extension, single-line comment notation)
languages = {
        "python" : ("py", "#"),
        "go" : ("go", "//")
    }

# default langauge varialbe
default = "python"

def main():

    # Case where language is not given, use default langauge
    if len(sys.argv) < 3:

        # Case where ID is given
        if len(sys.argv) == 2:
            probID = sys.argv[1]
        # No ID given, ask user for ID
        else:
            probID = input("ID not given. Please enter the Problem's ID: ")
    
        ex, comment = languages[default]

    # Case where both ID and langauge is given
    else:
        probID = sys.argv[1]

        lang = sys.argv[2].lower()
        # Check if language is in dictionary
        try:
            ex, comment = languages[lang] 
        except:
            print("Specified language not found: \"{}\" is not compatible".format(lang))
            print("Check your spelling or add the langauge to the dictionaty")
            quit()

    name = "{}.{}".format(probID, ex)
    with open(name, "w") as file:
        file.write("{} Program descirption at https://open.kattis.com/{}\n\n".format(comment, probID))


if __name__ == "__main__":
    main()