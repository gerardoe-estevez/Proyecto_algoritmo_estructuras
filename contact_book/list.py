
class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        string=str(self.data)
        
        return string
    

class LinkedList: 
    def __init__(self):
        self.head = None
        self.size = 0

    
    def append(self,data):
        this_node = node(data)
        if self.size == 0:
            self.head = this_node
        else:
            current = self.head
            if current.data.email==this_node.data.email:
                raise ValueError('Ya existe un email')
            while current.next != None:
                current = current.next
                if current.data.email==this_node.data.email:
                    raise ValueError('Ya existe un email')
            current.next = this_node
        self.size +=1 
        return 
            
    

    def add_to_front(self, data:node):
        self.head = node(data=data, next=self.head)  

    def is_empty(self):
        return self.head == None


    def add_to_end(self, data:node):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)
    

    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data



    def __str__(self) -> str:
        string = str("[")
        current = self.head
        while current != None:
            string += str(current)
            if current.next!=None:
                string += str(",")
            current = current.next
        string += "]"
        return string
        
    def __len__(self):
        return self.size

