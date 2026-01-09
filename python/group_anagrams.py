# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #first pass turn every string into an array where index contains count of each letter
        all_strings = []
        for s in strs:
            char_count = [0] * 27
            for c in s:
                char_count[ord(c) - ord('a')] += 1
            all_strings.append(tuple((s, tuple(char_count))))

        #second pass create hashmap where array is converted to tuple and used as key then values are an array containing words in the set
        count_to_words = {}
        for word, counter in all_strings:
            if counter in count_to_words:
                count_to_words[counter].append(word)
            else:
                count_to_words[counter] = [word]
        
        result = []
        for count, words in count_to_words.items():
            group = words
            result.append(group)
        return result
