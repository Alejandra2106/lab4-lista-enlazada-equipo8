# src/linked_list.py
# Estructura base — cada equipo implementa su operación asignada.


class Node:
    """Nodo de la lista enlazada."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """Lista enlazada simple."""

    def __init__(self):
        self.head = None

    # ------------------------------------------------------------------ #
    # Implementado por el docente — NO modificar                          #
    # ------------------------------------------------------------------ #
    def __str__(self):
        """Retorna una representación legible de la lista."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Lista vacía"

    def __len__(self):
        """Retorna el número de nodos."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # ------------------------------------------------------------------ #
    # TODO — Equipo A: rama feature/append                                #
    # ------------------------------------------------------------------ #
    
    def append(self, data):
        if data is None:
            raise ValueError("No se permite insertar None")
        
        # Caso de la lista vacía.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        # Caso de la lista no vacía.
        else:
            # Recorremos la lista hasta el último nodo.
            current = self.head
            while current.next:
                current = current.next
            # Enlazamos el nuevo nodo al final de la lista.
            current.next = new_node


    # ------------------------------------------------------------------ #
    # TODO — Equipo B: rama feature/delete                                #
    # ------------------------------------------------------------------ #
    def delete(self, data):
        # Caso 1: Lista Vacía
        if self.head is None:
            return False
         
        # Caso 2: Eliminar head
        if self.head.data == data:
            self.head = self.head.next
            return True
         
        # Caso 3: Buscar en el resto de la lista
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return True
        current = current.next

        return False

    # ------------------------------------------------------------------ #
    # TODO — Equipo C: rama feature/search                                #
    # ------------------------------------------------------------------ #
    # Esqueleto de referencia
    def search(self, data):
        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                return current_node

            current_node = current_node.next

        return None


