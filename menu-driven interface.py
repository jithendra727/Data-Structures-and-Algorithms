# Python code for the queue implementation 
#using an array, including a menu-driven interface

class queue:
    def __init__(self, maxsize):
         # Initialize the queue with a given maximum size
        self.queue = [None] * maxsize
        self.front = -1
        self.rear = -1
        self.maxsize = maxsize

    def is_empty(self):
        # Check if the queue is empty
        return self.front == -1
    
    def is_full(self):
        # Check if the queue is full
        return self.rear == self.maxsize - 1
    
    def insert(self, item):
        #insert an item into the queue
        if self.is_full():
            print("\nOVERFLOW\n")
            return
        if self.is_empty():
            #if the que is empty, initialize fornt and rear to 0
            self.front = 0
            self.rear = 0

        else:
            #otherwise, increment the rear pointer
            self.rear += 1
        self.queue[self.rear] = item
        print("\nValue inserted\n")
    
    def delete(self):
        #delete an item from the queue
        if self.is_empty() or self.front > self.rear:
            print("\nUNDERFLOW\n")
            return
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            #otherwise, increment the front pointer
            self.front += 1
        print("\nValue deleted : ",item)

    def display(self):
        #display the elements of the queue
        if self.is_empty():
            print("\nEmpty queue\n")
        else:
            print("\nPrinting values ....\n")
            for i in range(self.front, self.rear +1):
                print(self.queue[i])

def main():
        maxsize = 5
        q = queue(maxsize)

        while True:
            # Display the menu to the user
            print("\n*************************Main Menu*****************************\n")
            print("\n=================================================================\n")
            print("\n1. Insert an element\n2. Delete an element\n3. Display the queue\n4. Exit\n")
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                #Inset an element 
                item = int(input("\nEnter the element: "))
                q.insert(item)
            elif choice == 2:
                #Delete an element
                q.delete()
            elif choice == 3:
            # Display the queue
                q.display()
            elif choice == 4:
                # Exit the program
                print("\nExiting...")
                break

            else:
                # Invalid choice
                print("\nEnter a valid choice\n")

if __name__ == "__main__":
    main()