const strings = ["a", "b", "c", "d"];

// To get access to values (This occur in constant time)
const getSecondElement = strings[2]; // O(1)
console.log(getSecondElement);

// push: To push an element into an array
// push could be O(n) for dynamic arrays
strings.push("e"); // O(1)
console.log(strings);

// pop: To remove the last item in the array
strings.pop(); //O(1)
console.log(strings);

// unshift: To add an element to the beginning of the array
strings.unshift("x");
console.log(strings);

// splice:  To add element within an array
strings.splice(2, 0, "alien");
console.log(strings);
