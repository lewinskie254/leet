
#create permutations of all words 
def permutation(lst):
	if len(lst) == 0:
		return []
	if len(lst) == 1:
		return [lst]

	l = [] 
	for i in range(len(lst)):
		m = lst[i]
		remLst = lst[:i] + lst[i+1:] 
		for p in permutation(remLst):
			l.append([m] + p)
	return l


#create words from the permutations 
def word_checker(words): 
	word_permutations = permutation(words) 
	words_to_check = []
	
	for word in word_permutations:
		word_to_append = ""
		for i in range(len(word)): 
			word_to_append += word[i]
		
		words_to_check.append(word_to_append)
	
	return words_to_check

#return indexes of each word 
def findSubstring(s, words): 
	list_of_indexes = []
	list_of_words = word_checker(words) 
	for i in range(len(s)): 
		for word in list_of_words: 
			l = len(word)
			if s[i:i+l] == word: 
				list_of_indexes.append(i)
	
	return list_of_indexes


print(findSubstring("barfoothefoobarman", ["foo","bar"]))
#124 out of 182 tests passed. 


from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        substring_len = word_len * num_words
        word_count = Counter(words)
        result = []

        for i in range(word_len):  # Iterate over possible starting points
            left = i
            right = i
            current_count = Counter()
            while right + word_len <= len(s):
                # Extract a word from the right end
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] += 1
                    
                    # If a word's count exceeds its expected frequency, shrink the window
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                    
                    # If the window size matches the required substring length, it's a valid match
                    if right - left == substring_len:
                        result.append(left)
                else:
                    # Reset counters and move left pointer
                    current_count.clear()
                    left = right
        
        return result
