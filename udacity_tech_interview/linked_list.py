# https://classroom.udacity.com/courses/ud513/lessons/7117335401/concepts/78875247320923


class Element:

    def __init__(self, value):
        self.value = value
        #print('self.value: ', self.value)
        self.next = None
        #print('self.next: ', self.next)


class LinkedList:
    def __init__(self, head_element=None):
        self.head = head_element

    def append(self, new_element):
        current = self.head
        if self.head:
            #print('self.head is true')
            while current.next:
                current = current.next
            current.next = new_element
            #print('current.next: ', current.next)
        else:
            self.head = new_element
            #print(self.head)
            #print(new_element.value)



element1 = Element(1)
element2 = Element(2)
element3 = Element(3)

linlist1 = LinkedList()
linlist1.append(element1)
linlist1.append(element2)
linlist1.append(element3)

print(element2.next.value)