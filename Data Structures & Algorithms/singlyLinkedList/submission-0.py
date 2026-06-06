class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head

        while curr and index:
            curr = curr[1]
            index -= 1

        return curr[0] if curr else -1
        

    def insertHead(self, val: int) -> None:
        self.head = [val, self.head]
        

    def insertTail(self, val: int) -> None:
        node = [val, None]

        if not self.head:
            self.head = node
            return

        curr = self.head
        while curr[1]:
            curr = curr[1]

        curr[1] = node

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        if index == 0:
            self.head = self.head[1]
            return True

        curr = self.head

        while curr and index > 1:
            curr = curr[1]
            index -= 1

        if not curr or not curr[1]:
            return False

        curr[1] = curr[1][1]
        return True

    def getValues(self) -> List[int]:
        ans = []
        curr = self.head

        while curr:
            ans.append(curr[0])
            curr = curr[1]

        return ans
