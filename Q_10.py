def longest_c_word(filename):
    """
    Find and return the longest word in a text file that starts with a "c"
    :param filename: name of the text file
    :return: the longest word starting with a "c"
    """
    longest = ""  # stores the longest word found so far
    special_chars = ",?.!;:" #things to be removed/omitted

    # open the file and read it
    with open(filename) as f:
        for line in f:
            # remove punctuation
            for c in special_chars:
                line = line.replace(c, "")
            # lowercase
            line = line.lower()
            # split the line into individual words
            words = line.split()
            # check each word
            for word in words:
                # check if the word starts with a "c"
                if word.startswith("c"):

                    # if the word is longer than the current longest one
                    if len(word) > len(longest):
                        longest = word

    return longest
print(longest_c_word("Q_10_txt_file.txt"))