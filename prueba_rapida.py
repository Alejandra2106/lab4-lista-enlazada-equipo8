from src.linked_list import LinkedList, Node

ll = LinkedList()

ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)

print("Lista inicial:", ll)

resultado = ll.search(2)

print("¿Se encontró?:", resultado)

resultado2 = ll.search(5)

print("¿Se encontró el 5?:", resultado2)

print("Lista final:", ll)
print("Tamaño:", len(ll))