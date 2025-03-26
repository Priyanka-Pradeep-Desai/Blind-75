from collections import defaultdict
def find_anagrams(s):

    a_char = ord('a')

    result = []

    # for each length, we do a sliding window
    for i in range(2, len(s)):

        d = defaultdict(list)  # key: the hashmap, if found then it will be a list the value

        c = [0] * 26 # this keeps track of the character frequency

        # initalize the sliding window
        for j in range(i):
            # initial version
            c[ord(s[j])-a_char]+=1

        # first time value add to dict
        d[tuple(c)].append([0,i-1])

        # now proceed to sliding window
        for j in range(i, len(s)):
            # remove
            c[ord(s[j-i])-a_char]-=1
            # add
            c[ord(s[j])-a_char]+=1
            # add to dictionary
            d[tuple(c)].append([j-i+1, j])

        # loop through dictionary, find any tuple that has more than 1 frequency
        for k, v in d.items():

            if len(v) > 1:
                for start, end in v:
                    result.append(s[start: end+1])
    return result

s = "abccba" #List : ab ba bc cb abc cba bcc ccb abcc ccba abccb bccba
find_anagrams(s)
