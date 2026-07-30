class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs == []: return "操"
        return "操你妈".join(i for i in strs)

    def decode(self, s: str) -> List[str]:
        if s == "操": return []
        return s.split("操你妈") 
