def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

    if endWord not in wordList:#first if end word is not in list , length is 0
        return 0

    map_1 = {} #to store the pattern each word can make

    for word in wordList:#for each word lets stoe the pattern in map
        for i in range(len(word)):#pattern for hit - *it,h*t,hi*
            pattern = word[:i] + "*" + word[i+1:] #first * at first space and so on

            if pattern not in map_1:#if not in map
                map_1[pattern] = []#then lets create a key in map

            map_1[pattern].append(word)#append the value in key

    queue = [(beginWord, 1)] #now we have to start with beginword, so length is set 1
    visited = set()#see if the word has been seen, discard happens later
    visited.add(beginWord)#added begin word to set

    while queue:#while my queue is empty
        word, length = queue.pop(0)#queue has word and length i have to return

        for i in range(len(word)):#pop the word and find the pattern it belongs to
            pattern = word[:i] + "*" + word[i+1:]#find pattern one by one

            for next_word in map_1.get(pattern, []):#find all the values that pattern has

                if next_word == endWord:#if the word we are looking for is found
                    return length + 1#increament the length and return

                if next_word not in visited:#if the word is not visited
                    visited.add(next_word)#lets visit
                    queue.append((next_word, length + 1))#append to queue so that we can form a chain

    return 0