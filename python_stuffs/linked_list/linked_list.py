class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None # next node

class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def append(self, data):
        """Append data to linked list

        Args:
            data : data of the new Node to be appended 
        """
        new_node = Node(data)
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        
        curr_node.next = new_node

    def length(self):
        """get length of linked list
        """
        curr_node = self.head
        total = 0
        while curr_node.next != None:
            total +=1
            curr_node = curr_node.next
        return total

    def display(self):
        """Helper function to display data in the linked list
        """
        curr_node = self.head
        res_string = "HEAD->"

        while curr_node.next != None:
            curr_node = curr_node.next
            res_string += str(curr_node.data) + "->"
        res_string += 'END'
        return res_string


    def get(self, index):
        """get node's data at index of linked list

        Args:
            index (int): index position of linked list 
        """

        assert index < self.length(), "Invalid index. Index out of range"

        curr_node = self.head
        curr_index = 0
        while curr_index <= index:
            curr_node = curr_node.next
            curr_index +=1

        return curr_node.data

    def delete(self, index):
        assert index < self.length(), "Invalid index. Index out of range"

        curr_node = self.head
        curr_index = 0
        while curr_index <= index:
            latest_node = curr_node # to keep reference node after the deleted note
            curr_node = curr_node.next
            curr_index += 1
        
        print("deleted: ", curr_node.data)
        latest_node.next = curr_node.next
        
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(0)
    linked_list.append(10)
    linked_list.append(100)

    print(linked_list.length())

    print(linked_list.display())

    # print(linked_list.get(10))
    # print(linked_list.get(0))
    # print(linked_list.get(1))
    # print(linked_list.get(2))
    linked_list.delete(3)
    print(linked_list.display())