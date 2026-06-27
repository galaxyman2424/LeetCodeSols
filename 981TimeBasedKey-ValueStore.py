class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append((value, timestamp))
        else:
            self.dict[key] = [(value, timestamp)]


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        if timestamp < self.dict[key][0][1]:
            return ""
        
        values = self.dict[key]
        left = 0 
        right = len(values) - 1
        mid = 0
        res = ""


        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]  
                left = mid + 1
            else:
                right = mid - 1       
        
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)