def Stack():
    n =[]
    return n

def checkempty(n):
    return len(n)==0

def push(n,item):
    n.append(item)
    print("pushed item : "+ item)

def pop(n):
    if(checkempty(n)):
        return "stack is empty"
    
    return n.pop()

n = Stack()
push(n, str(1))
push(n, str(2))
push(n, str(3))
push(n, str(4))

print("popped item: "+ pop(n))
print("stack after popping an element: " + str(n))