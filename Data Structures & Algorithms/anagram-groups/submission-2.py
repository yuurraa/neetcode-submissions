class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in strs:
            anagrams[str(sorted(dict(Counter(i)).items()))].append(i)
        return list(anagrams.values())
