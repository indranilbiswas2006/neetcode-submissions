class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n = len(operations)
        rec = []

        for i,op in enumerate(operations): 
            len_rec = len(rec)
            if op == "+": 
                value = rec[len_rec-1] + rec[len_rec-2]
                rec.append(value)
            elif op == "D": 
                value = rec[len_rec-1] * 2 
                rec.append(value)
            elif op == "C": 
                rec.pop()
            else: 
                rec.append(int(op))   
        return sum(rec)
        