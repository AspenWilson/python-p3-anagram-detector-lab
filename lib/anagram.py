# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word= word

    def match(self, word_list):
        anagrams = []
        for i in word_list:
            if sorted(self.word.lower()) == sorted(i.lower()) and self.word.lower() != i.lower():
                anagrams.append(i)
        return anagrams