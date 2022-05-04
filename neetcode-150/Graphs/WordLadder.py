'''
https://leetcode.com/problems/word-ladder/
'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # if there is no end word in the list of words
        if endWord not in wordList:
            return 0

        # we create structures to make adj list
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        
        # iterate over every word and every word's symbol and create patterns with one missed letter
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)

            res += 1
            
        return 0
