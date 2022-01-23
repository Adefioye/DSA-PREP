// Reference types
const object1 = { value: 10 };
const object2 = object1; //object2 references the address assigned to object1
const object3 = { value: 10 };

// Context vs Scope
// Scope is initiated when we are in code block or a function. In javascript, this is
// initiated within a curly brace. However, a context can be known by using the "this" keyword
// and it shows the object environment within which the "this" keyword is used.

// const object4 = {
//   a: function () {
//     console.log(this);
//   },
// };
// console.log(object4.a());

// Instantiation
class Player {
  constructor(name, player) {
    console.log("player", this);
    this.name = name;
    this.player = player;
  }
  introduce() {
    console.log(`Hi! I am ${this.name}, I'm a ${this.type}`);
  }
}

class Wizard extends Player {
  constructor(name, player) {
    super(name, player);
    console.log("wizard", this);
  }
  play() {
    console.log(`Hey! I'm the amazing magical ${this.name}`);
  }
}

const wizard1 = new Wizard("Koko", "Sorcerer");

// This is gonna log to the console the Wizard class for the 2 "this" keywords in both
// the Player and Wizard class.Perhaps, becasue it is the entry point for the
// instantiation of the Class.
