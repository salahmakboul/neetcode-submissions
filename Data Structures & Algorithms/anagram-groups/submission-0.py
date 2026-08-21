class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        array=[]
        strp={}
        for i in range(len(strs)):
            stored_strs="".join(sorted(strs[i]))
            if stored_strs not in strp :
                strp[stored_strs]=[]
            strp[stored_strs].append(strs[i])
            array=list(strp.values())
        return array

        