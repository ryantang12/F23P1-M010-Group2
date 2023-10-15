def compare_files(file1_name: str, file2_name: str = "TextOutput.txt") -> bool:
    try:
        # Open the first file and read its contents
        with open(file1_name, 'r') as file1:
            content1 = file1.read()

        # Open the second file and read its contents
        with open(file2_name, 'r') as file2:
            content2 = file2.read()

        # Check if the contents of the two files are identical
        if content1 == content2:
            return True
        else:
            return False

    except FileNotFoundError:
        print("One or both files not found.")
        return False


def are_strings_identical(string1: str, string2: str) -> bool:
    # Check if the lengths of the two strings are the same
    if len(string1) != len(string2):
        return False

    # Go through the characters of both strings and compare them
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False

    # If the loop completes without finding any differences, the strings are identical
    return True
