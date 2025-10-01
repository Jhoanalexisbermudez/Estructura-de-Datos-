class Node {
    Integer value;
    Node next;

    Node(Integer value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedList {

    private Node head;

    // Insertar al inicio de la lista
    public void insertAtHead(Integer value) {
        Node newNode = new Node(value);
        newNode.next = head;
        head = newNode;
    }

    // Eliminar el último nodo (tail) de la lista
    public void deleteLast() {
        if (head == null) {
            // Lista vacía
            return;
        }

        if (head.next == null) {
            // Solo un elemento
            head = null;
            return;
        }

        Node current = head;
        while (current.next.next != null) {
            current = current.next;
        }

        // current está en el penúltimo nodo
        current.next = null;
    }

    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.value + "->");
            current = current.next;
        }
        System.out.print("/\n");
    }
}

public class LinkedListDemo {

    public static void main(String[] args) {
        LinkedList list = new LinkedList();

        // Insertar al inicio (se arma en orden inverso)
        list.insertAtHead(50);
        list.insertAtHead(40);
        list.insertAtHead(30);
        list.insertAtHead(20);
        list.insertAtHead(10);

        // Resultado inicial: 10->20->30->40->50->/
        list.printList();

        // Eliminar el último nodo (50)
        list.deleteLast();

        // Resultado esperado: 10->20->30->40->/
        list.printList();
    }
}
