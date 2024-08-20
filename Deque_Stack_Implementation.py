from collections import deque

# Main function equivalent
if __name__ == "__main__":
    dq = deque()
    
    dq.append(3)          # Similar to add() in Java
    dq.append(4)          # Similar to addLast() in Java
    dq.appendleft(2)      # Similar to addFirst() in Java
    dq.appendleft(1)      # Similar to addFirst() in Java
    dq.appendleft(10)     # Similar to addFirst() in Java
    
    print("Deque Content:", list(dq))
    print("Remove first Element:", dq.popleft())  # Similar to pollFirst() in Java
    print("Deque Content:", list(dq))
