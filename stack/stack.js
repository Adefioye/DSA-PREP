class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.top = null;
    this.bottom = null;
    this.length = 0;
  }

  peek() {
    return this.top;
  }

  push(value) {
    const newNode = new Node(value);

    if (this.length == 0) {
      this.top = newNode;
      this.bottom = this.top;
      this.length++;
    } else {
      const formerTopNode = this.top;
      this.top = newNode;
      this.top.next = formerTopNode;
      this.length++;
    }

    return this;
  }

  pop() {
    if (this.top == this.bottom) {
      this.bottom = null;
    }

    this.top = this.top.next;
    this.length--;

    return this;
  }
}

const myStack = new Stack();

// discord
// udemy
// google

console.log(myStack.push(9));
console.log(myStack.push(8));
console.log(myStack.push(3));

console.log(myStack.pop());
console.log(myStack.pop());
console.log(myStack.pop());
