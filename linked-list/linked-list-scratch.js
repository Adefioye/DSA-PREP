// Create first linked list from scratch
// 10-->5-->16

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor(value) {
    this.head = {
      value: value,
      next: null,
    };
    this.tail = this.head;
    this.length = 1;
  }
  printList() {
    const array = [];
    let currentNode = this.head;
    while (currentNode !== null) {
      array.push(currentNode.value);
      currentNode = currentNode.next;
    }
    return array;
  }
  append(value) {
    const newNode = new Node(value);
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
    return this;
  }
  prepend(value) {
    const newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
    return this;
  }

  insert(index, value) {
    if (index >= this.length) {
      this.append(value);
      return this.printList();
    }

    if (index === 0) {
      this.prepend(value);
      return this.printList();
    }

    const newNode = new Node(value)
    let counter = 0 
    let leader = this.head
    while ((counter + 1) < index) {
      leader = leader.next 
      counter++
    }
    newNode.next = leader.next 
    leader.next = newNode 

    return this.printList()
  }
}
const myLinkedList = new LinkedList(10);
console.log(myLinkedList);
myLinkedList.append(5);
console.log(myLinkedList.printList());
myLinkedList.append(16);
console.log(myLinkedList.printList());
myLinkedList.prepend(7);
console.log(myLinkedList.printList());
console.log(myLinkedList.insert(10, 99))
console.log(myLinkedList.insert(0, 25))
console.log(myLinkedList.insert(1, 55))
console.log(myLinkedList.insert(3, 56))
console.log(myLinkedList.insert(5, 57))

// Experiment with the Node class
// const myNode = new Node(10);
// console.log(myNode);
