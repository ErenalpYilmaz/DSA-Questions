class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""

        maxLenght = max(len(word1), len(word2))

        for item in range(maxLenght):
            if item < len(word1):
                result += word1[item]
            if item < len(word2):
                result += word2[item]

        return result