def FrequencyMap(Text,k):
    FrequencyMap = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        FrequencyMap[Pattern]= 0
        for i in range(len(Text)-k+1):
            if Text[i:i+len(Pattern)]==Pattern:
                FrequencyMap[Pattern] += 1
    return FrequencyMap

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text,k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words
