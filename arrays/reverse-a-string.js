const myString = "Hi! my name is Koko";

function reverseAString(str) {
  // create an array from character string
  // find a way to loop over the array and make the first last and added into an array
  // the new array is then converted back to a string

  // Check INPUT
  if (typeof str !== "string") {
    return "Hmm! Not the correct input";
  }

  if (str.length === 1) {
    return str;
  }

  const reverseStringArrays = [];
  for (let i = str.length - 1; i >= 0; i--) {
    reverseStringArrays.push(str[i]);
  }
  return reverseStringArrays.join("");
}

// Using builtin methods
function reverseAString2(str) {
  return str.split("").reverse().join("");
}

// using ES6 method and a spread operator
const reverseAString3 = (str) => [...str].reverse().join("");

// console.log(reverseAString(myString));
// console.log(reverseAString("You are a bastard"));
// console.log(reverseAString2(myString));
// console.log(reverseAString("You are a bastard"));
// console.log(reverseAString3(myString));
// console.log(reverseAString3("You are a bastard"));
console.log(reverseAString("bastard"));
