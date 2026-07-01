class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        s1count = {}
        s2count = {}

        for char in s1:
            if char in s1count:
                s1count[char] += 1
            else:
                s1count[char] = 1


        left = 0
        s1len = len(s1)

        #print("String one frequency map: ")
        #for k in s1count:
            #print("key: ", k, " value: ", s1count[k])


        all_match = False

        for right in range(len(s2)):
            if s2[right] not in s2count:
                s2count[s2[right]] = 1
            else:
                s2count[s2[right]] += 1
            
            if right - left + 1 > s1len:
                s2count[s2[left]] -= 1
                left += 1

            all_match = all(s1count[ch] == s2count.get(ch, 0) for ch in s1count)
            

            #print("String two frequency map: ")
            #for k in s2count:
                #print("key: ", k, " value: ", s2count[k])

            if all_match:

                return True


        return False