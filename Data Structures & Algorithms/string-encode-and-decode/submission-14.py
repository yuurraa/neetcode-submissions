class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: return "啊"
        return "अ".join(i for i in strs)

    def decode(self, s: str) -> List[str]:
        if s == "啊": return []
        return s.split("अ") 
