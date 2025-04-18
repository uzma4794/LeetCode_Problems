class MyQueue:

    def __init__(self):
        self.stack1= []
        self.stack2= []


    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:      #if stack2 is empty
           while self.stack1:       # run until stack1 gets empty
                self.stack2.append(self.stack1.pop())            #append values in stack2 from stack1 after popping
        return self.stack2.pop()    # This step pops the element which is deque by the queue.


    def peek(self) -> int:
        if not self.stack2:      #if stack2 is empty - not makes this stateemnt true
           while self.stack1:       # run until stack1 gets empty
                self.stack2.append(self.stack1.pop())            #append values in stack2 from stack1 after popping
        return self.stack2[-1]    # This step pops the element which is deque by the queue.


    def empty(self) -> bool:
         return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
