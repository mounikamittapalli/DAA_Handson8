class SinglyLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.nodes = [None] * capacity  # Array to store the nodes
        self.head = -1  # -1 indicates empty list
        self._size = 0



    def insert(self, value):
        if self._size == self.capacity:
            print("List Overflow")
            return

        new_index = self._size  # New node will be inserted at the current size index
        self.nodes[new_index] = {"data": value, "next": -1}

        if self.head == -1:  # List is empty, new node will be the head
            self.head = new_index
        else:
            current = self.head
            while self.nodes[current]["next"] != -1:
                current = self.nodes[current]["next"]
            self.nodes[current]["next"] = new_index  # Link the new node

        self._size += 1  # Increment the size

    def delete(self, value):
        if self.head == -1:
            print("List Underflow")
            return

        current = self.head
        previous = -1

        while current != -1:
            if self.nodes[current]["data"] == value:
                if previous == -1:  # Deleting the head node
                    self.head = self.nodes[current]["next"]
                else:
                    self.nodes[previous]["next"] = self.nodes[current]["next"]
                self._size -= 1  # Decrement the size
                return
            previous = current
            current = self.nodes[current]["next"]

        print(f"Value {value} not found in the list.")

    def search(self, value):
        current = self.head
        while current != -1:
            if self.nodes[current]["data"] == value:
                return True
            current = self.nodes[current]["next"]
        return False

    def is_empty(self):
        return self.head == -1

    def get_size(self):  # Renamed method to avoid conflict with attribute
        return self._size
    def __str__(self):
            # Create a string representation of the linked list
            current = self.head
            values = []
            while current != -1:
                values.append(str(self.nodes[current]["data"]))
                current = self.nodes[current]["next"]
            return " -> ".join(values) if values else "Empty List"

# Example usage
linked_list = SinglyLinkedList(5)
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
print(linked_list)
print("Search for 20:",linked_list.search(20))  # True
linked_list.delete(20)
print("After removing value:",linked_list)
print("Search for 20:",linked_list.search(20))  # False
print("checking list is empty:",linked_list.is_empty())  # checking list sizw
print("size of singleLinkedList:",linked_list.get_size())  # getting size
