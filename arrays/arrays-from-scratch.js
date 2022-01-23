// Build an array from scratch using classes in javascript
class MyArray {
  constructor() {
    this.length = 0;
    this.data = {};
  }

  get(index) {
    return this.data[index];
  }

  push(item) {
    this.data[this.length] = item;
    this.length++;
    return item;
  }

  pop() {
    const lastItem = this.data[this.length - 1];
    delete this.data[this.length - 1];
    this.length--;
    return lastItem;
  }

  delete(index) {
    const deletedItem = this.data[index];
    delete this.data[index];
    this.shiftItems(index);
    delete this.data[this.length - 1];
    this.length--;
    return deletedItem;
  }

  shiftItems(index) {
    for (let i = index; i < this.length - 1; i++) {
      this.data[i] = this.data[i + 1];
    }
  }
}

const newArray = new MyArray();
console.log(newArray.get(0));
console.log(newArray.push("Hi!"));
console.log(newArray.push("Cokesman"));
console.log(newArray.push("MB"));
console.log(newArray.push("BJ"));
console.log(newArray.push("You"));
console.log(newArray.push("are"));
console.log(newArray.push("awesome"));
// console.log(newArray.pop());
// console.log(newArray.pop());
console.log(newArray.delete(2));
console.log(newArray);
