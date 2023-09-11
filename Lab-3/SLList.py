class SLList:
    class IntNode:
        def __init__(self, item, next_node):
            self.item = item # int
            self.next = next_node # IntNode
            
    def __init__(self):
        self.first = None # initialize an empty list
        self.size = 0 # init size var

    def addFirst(self, item):
        self.first = self.IntNode(item, self.first)
        self.size += 1 # increment size

    def reverse(self):
        # Grab head of list and assign to both an iterator value and a reverse value which we will use to update the list.
        jumper = self.first
        rev = self.first
        # for each item in the list, we are going to reassign the first value to the first value found.
        for _ in range(self.size-1):
            jumper = jumper.next
            # Since the list is added in reverse order already, when we do this it will reverse the order and assign index 0 to index n-1.
            rev.next = self.addFirst(jumper.item)
            # Using addFirst, we have to subtract the increment in that function or our size will be off by 2n-2.
            self.size -= 1

    def replicate(self):
        # Grab the head of the list to do manipulation. 
        List = self.first
        # Create a new list to fill
        rep = SLList()
        # Init the first value of the new list so its not just empty.
        rep.first = self.IntNode(List.item, self.first)
        
        # loop through the original list based on its size
        for _ in range(self.size):
            
            # create a loop which loops by the value of the item at any position in the original list.
            for _ in range(List.item):
                # add a new node with the original's value and assign it to the .next position in the new list.
                rep.first.next = self.IntNode(List.item, rep.first.next)
                # increment the size of the new list.
                rep.size += 1
            # After the loop is done to add N number of elements. We grab the next N in the original List.
            List = List.next
        # return the new list to store it as a separate object.
        return rep
        
        

    def insert(self, item, position):
        # check if position is within list.
        if position >= self.size:
            # if position is outside of or at the end of the list, iterate to the end of the list.
            end = self.first
            for _ in range(self.size-1):
                end = end.next
            # append new value at the end of list.
            end.next = self.IntNode(item, None)
            # increment size.
            self.size += 1
        else:
            # Set a temp variable to track the node before the node we want to insert to be able to reconnect the list.
            before = self.first
            # Create loop to iterate to the node at index-1.
            for _ in range(position-1):
                before = before.next
            # Make jumper variable to be the index that we want to insert.
            jumper = before.next
            # Insert node and reconnect the list by setting the next next node to jumper. Increment size.
            before.next = self.IntNode(item, jumper)
            self.size += 1

    def equals(self, anotherList):
        # check if lists are the same size. If they aren't the same size the lists won't be the same.
        if self.size == anotherList.size:
            # grab the heads of both lists to start the comparison with the first node.
            List = self.first
            anotherList = anotherList.first
            # loop through every node and compare their values.
            for _ in range(self.size):
                # I added a print just for verbosity. Comment out line if you aren't interested.
                print(List.item,anotherList.item)
                # compare items and if they are the same do nothing, if they aren't then return false and stop processing
                if List.item == anotherList.item:
                    pass
                else:
                    return False
                # update to the next node and repeat
                List = List.next
                anotherList = anotherList.next
            # If nothing is found, then return true.
            return True
        # If they aren't the same size then return false.
        else:
            return False
    
    # I added a basic print list function for debugging and testing.
    def print_list(self):
        # grab head and print in a loop through each item in the list.
        jumper = self.first
        for _ in range(self.size):
            print(jumper.item)
            jumper = jumper.next


    def reverse_recursion(self):
        # pass the head of the list into the start of the recursion function to start. 
        self.reverse_helper(self.first)

    def reverse_helper(self, List):
        # check if the current node is None. If it is, stop recursion.
        if List != None:
            # Otherwise, print item for verbosity
            print(List.item)
            # and update list using addFirst.
            rev = self.addFirst(List.item)
            # recurse deeper into list until recursion breaks.
            return self.reverse_helper(List.next)