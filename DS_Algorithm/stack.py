import sys

class STACK:
    def __init__(self):
        self.list = []
        self.size = 0


    def is_empty(self) -> bool:
        if(self.size == 0):
            return True
        else:
            return False
        
    def push(self, k: int):
        self.list.append(k)
        self.size += 1
    
    def pop(self) -> int:
        if(self.size == 0):
            print("Error: STACK empty")
        else:
            self.size -= 1
            return self.list.pop()

    def size(self) -> int:
        return self.size


