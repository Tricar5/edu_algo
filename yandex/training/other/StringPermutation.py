
# check if two string is permutation of each_other


def testStringPermutation(s1, s2):

    d_1 = {}
    d_2 = {}

    for i in range(len(s1)):

        if s1[i] not in d_1.keys():
            d_1[s1[i]] = 0

        d_1[s1[i]] += 1

        if s2[i] not in d_2.keys():
            d_2[s2[i]] = 0

        d_2[s1[i]] += 1

    for letter in d_1.keys():
        if letter not in d_2.keys():
            return False

        if d_1[letter] != d_2[letter]:
            return False

    return True


# Python program to check if two strings are
# Permutations of each other
NO_OF_CHARS = 256


# Function to check whether two strings are
# Permutation of each other
def arePermutation(str1, str2):
    # Create two count arrays and initialize
    # all values as 0
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS

    # For each character in input strings,
    # increment count in the corresponding
    # count array
    for i in str1:
        count1[ord(i)] += 1

    for i in str2:
        count2[ord(i)] += 1

    # If both strings are of different length.
    # Removing this condition will make the
    # program fail for strings like
    # "aaca" and "aca"
    if len(str1) != len(str2):
        return 0

    # Compare count arrays
    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return 0

    return 1
