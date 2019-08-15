"""
    Given a word in sentence, reverse each word of the sentence individually in the
    sentence itself
"""

def reverse_word_in_sentence(input):

    wordlist = input.split()

    # newWords = [word[::-1] for word in wordlist]
    # newSentence = ''.join(newWords)
    # return newSentence
    rwordlist = []
    #rsentence = ''

    for word in wordlist:
        rwordlist.append(word[::-1])

    rsentence = ' '.join(rwordlist)
    return rsentence

    #return rwordlist


reverse_sentenced = reverse_word_in_sentence('Hello World')

print(reverse_sentenced.capitalize())
