class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: return "啊"
        return "一".join(i for i in strs)

    def decode(self, s: str) -> List[str]:
        if s == "啊": return []
        return s.split("一") 
