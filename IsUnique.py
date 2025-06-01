from typing import List
from collections import Counter
from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Occurrences = defaultdict(int)
        for i in arr:
            Occurrences[i] += 1
        valores = Occurrences.values()
        
        #Brute force
        '''             
        valores = list(Occurrences.values())
        print('valores', valores)
        for k in range(len(valores) - 1):
            for j in range(k+1, len(valores)):
                if valores[k] == valores[j]:
                    return False
        return True
        Time complexity O(n^2)
        Space complexity O(n)
        '''

        # Better solution
        return len(Occurrences) == len(set(valores))
        #Time complexity O(n^2)
        #Space complexity O(n)
    
        #Other solution
        '''
        c = Counter(arr)
        return len(c.values()) == len(set(c.values()))
        '''
    
sol = Solution()
rel = sol.uniqueOccurrences([1,2,2,1,1,3])
print(rel)
