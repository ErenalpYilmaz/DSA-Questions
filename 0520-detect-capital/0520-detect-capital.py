class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        isTrue = True
        if word.islower() == True:
            return True
        if word.isupper() == True:
            return True
        for words in range(1, len(word)):
            if word[words].isupper() == True:
                isTrue = False
        return isTrue