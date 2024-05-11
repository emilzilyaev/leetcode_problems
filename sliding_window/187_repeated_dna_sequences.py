class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        occureed_substrings = set()
        occured_twice = set()

        for i in range(len(s)-9):
            if s[i:i+10] in occureed_substrings:
                occured_twice.add(s[i:i+10])
            else:
                occureed_substrings.add(s[i:i+10])


        return list(occured_twice)
