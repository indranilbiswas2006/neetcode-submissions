class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        highest_element = 0
        for i in range(n): 
            max_element = True
            for j in range(i,n): 
                if arr[j] > arr[i]: 
                    arr[i] = arr[j]
                    max_element = False 
            if max_element: 
                highest_element = max(arr[i],highest_element)

        arr.remove(highest_element)
        arr.append(-1)
        return arr

        