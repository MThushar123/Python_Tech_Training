#Linked List Operations – Implement insertion, deletion, and searching in a linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print(f"Inserted {data} at the end.")

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for i in range(position - 1):
            if temp is None:
                print("Position out of range.")
                return
            temp = temp.next
        if temp is None:
            print("Position out of range.")
            return
        new_node.next = temp.next
        temp.next = new_node
        print(f"Inserted {data} at position {position}.")

    def delete_by_value(self, data):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.data == data:
            self.head = self.head.next
            print(f"Deleted {data}.")
            return
        temp = self.head
        while temp.next and temp.next.data != data:
            temp = temp.next
        if temp.next is None:
            print(f"{data} not found.")
        else:
            temp.next = temp.next.next
            print(f"Deleted {data}.")

    def delete_by_position(self, position):
        if self.head is None:
            print("List is empty.")
            return
        if position == 0:
            self.head = self.head.next
            print(f"Deleted node at position {position}.")
            return
        temp = self.head
        for i in range(position - 1):
            if temp.next is None:
                print("Position out of range.")
                return
            temp = temp.next
        if temp.next is None:
            print("Position out of range.")
        else:
            temp.next = temp.next.next
            print(f"Deleted node at position {position}.")

    def search(self, data):
        temp = self.head
        position = 0
        while temp:
            if temp.data == data:
                print(f"{data} found at position {position}.")
                return
            temp = temp.next
            position += 1
        print(f"{data} not found.")

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Interactive menu
ll = LinkedList()
while True:
    print("\nLinked List Operations:")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at position")
    print("4. Delete by value")
    print("5. Delete by position")
    print("6. Search")
    print("7. Display list")
    print("8. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        data = int(input("Enter data to insert: "))
        ll.insert_at_beginning(data)
    elif choice == '2':
        data = int(input("Enter data to insert: "))
        ll.insert_at_end(data)
    elif choice == '3':
        data = int(input("Enter data to insert: "))
        pos = int(input("Enter position: "))
        ll.insert_at_position(data, pos)
    elif choice == '4':
        data = int(input("Enter data to delete: "))
        ll.delete_by_value(data)
    elif choice == '5':
        pos = int(input("Enter position to delete: "))
        ll.delete_by_position(pos)
    elif choice == '6':
        data = int(input("Enter data to search: "))
        ll.search(data)
    elif choice == '7':
        ll.display()
    elif choice == '8':
        break
    else:
        print("Invalid choice. Try again.")