# Enter your code here. Read input from STDIN. Print output to STDOUT
class Stacks:
    def __init__(self):
        self.items = []
        self.max_item = []
    
    def push(self, item):
        self.items.append(item)   
        if len(self.max_item) != 0:
            if item >= self.max_item[-1]:
                self.max_item.append(item)
        else:
            self.max_item.append(item)
        # else:
        #     self.max_item.append(self.max_item[-1])

    def pop(self):
        if len(self.items) == 0:
            print('Error')
            return
        a = self.items.pop()
        if len(self.max_item) != 0:
            if a == self.max_item[-1]:
                self.max_item.pop()

    def find_max(self):
        if len(self.max_item) != 0:
            print(self.max_item[-1]) 

s = Stacks()
for i in range(int(input())):
    nums = list(map(int, input().split()))
    if nums[0] == 1:
        s.push(nums[1])
    elif nums[0] == 2:
        s.pop()
    else:
        s.find_max()

