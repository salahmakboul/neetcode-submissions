
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}


class Solution {
    public Node copyRandomList(Node head) {
        if (head == null){
            return null;
        }
        HashMap<Node, Node> map = new HashMap<>();
        Node current = head ;
        while (current != null) {
            //copie of the node
            Node new_node = new Node(current.val);
            map.put(current, new_node);
            current = current.next;
        }
        current = head;
        while (current != null){
            Node clone = map.get(current);
            clone.next = map.get(current.next);
            clone.random = map.get(current.random);
            current = current.next;
        };
        return map.get(head);
        
    }
}
