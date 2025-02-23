import datetime


# dummy head -> has two nodes: { doggo_LinkedList, caty_linkedlist }
# LinkedList -> headnode , stores time, also has tail, if someone wants to insert simply insert with time at the tail, while taking it out also take it out from the head

class Node():
    def __init__(self, name=None,  time = datetime.datetime.now(), next = None, prev=None, type=""):
        self.time = time
        self.next = next
        self.prev = prev
        self.name = name
        self.type = type


class AnimalShelter():
    def __init__(self):
        self.dog_head = Node(type="dog")
        self.cat_head = Node(type="cat")

    def deque_dog(self):
        dummy_head = self.dog_head

        if not dummy_head.next:
            return None

        dog = dummy_head.next

        if not dog.next.name:
            dummy_head.next = None
            dummy_head.prev = None
            return dog

        dummy_head.next = dog.next
        next = dog.next
        next.prev = dummy_head

        return dog

    def deque_cat(self):
        dummy_head = self.cat_head

        if not dummy_head.next:
            return None

        cat = dummy_head.next

        if not cat.next.name:
            dummy_head.next = None
            dummy_head.prev = None
            return cat

        dummy_head.next = cat.next
        next = cat.next
        next.prev = dummy_head

        return cat

    def dequeu(self, type=None):
        if type == None:
            return self.dequeu_from_the_older_from_both()
        elif type == "cat":
            return self.deque_cat()
        else:
            return self.deque_dog()

    def dequeu_from_the_older_from_both(self):
        node1 = self.dog_head.next
        node2 = self.cat_head.next

        if node1 and node2:
            main = node1 if node1.time < node2.time else node2
            head = self.dog_head if node1.time < node2.time else self.cat_head

        elif node1:
            main = node1
            head = self.dog_head

        elif node2:
            main = node2
            head = self.cat_head

        else:
            return None

        next = head.next.next

        if next.name:
            next.prev = head
            head.next = next
        else:
            head.next = None
            head.prev = None

        print(f'adopting animal {main.name}, type{main.type}, sheltered at{main.time}')

        return main

    def enqueue(self, type, name):
        if type == "dog":
            self.enqueue_helper(head=self.dog_head, name=name, type=type)
        else:
            self.enqueue_helper(head=self.cat_head, name=name, type= type)

    def enqueue_helper(self, head, name, type):
        new_animal = Node(name=name, type=type)
        if head.prev:
            tail = head.prev
            tail.next = new_animal
            new_animal.prev = tail
            new_animal.next = head
            head.prev = new_animal
        else:
            head.next = new_animal
            new_animal.next = head
            head.prev = new_animal
            new_animal.prev=head


def test_enqueue():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(name="Fluffy", type="cat")
    animal_shelter.enqueue(name="doggy1", type="dog")
    animal_shelter.enqueue(name="Fluffy2", type="cat")
    animal_shelter.enqueue(name="doggy2", type="dog")

    print(animal_shelter.dequeu().name)
    print(animal_shelter.dequeu().name)
    print(animal_shelter.dequeu().name)
    print(animal_shelter.dequeu().name)

