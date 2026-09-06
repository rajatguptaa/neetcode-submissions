class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        print(strs)
    def decode(self, s: str) -> List[str]:
        print('s',s)
        res,i = [],0
        while i < len(s):
            
            j = i
            print('sssssss',s[j])
            while s[j] != "#":
                j += 1
                print('jjjj',j,'iii',i)

            length = int(s[i:j])
            print('length',length)
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            print('fdfdf',length)
        return res
