class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxValue = 0
        temp_string = '' 
        for elm in s:
            if elm in temp_string:
                uniqueIndex = temp_string.index(elm)
                temp_string = temp_string[uniqueIndex+1:len(temp_string)]
                temp_string += elm
            else:
                temp_string += elm
            
            if len(temp_string) > maxValue:
                maxValue = len(temp_string)

        return maxValue
