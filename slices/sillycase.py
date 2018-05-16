def sillycase(word):
    word1 = []
    for letter in word:
        word1.append(letter)

    word2 = len(word1) / 2
    lower_letter = word1[0:round(word2)]
    lower_letter = "".join(lower_letter)

    upper_letter = word1[round(word2):]
    upper_letter = "".join(upper_letter)


    return lower_letter.lower() + upper_letter.upper()


word = sillycase("steakhouse")
print(word)