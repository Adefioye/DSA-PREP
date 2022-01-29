// Google question
// Given an array = [2,5,1,2,3,5,1,2,4]
// It should return 2

// Given an array = [2,1,1,2,3,5,1,2,4]
// It should return 1

// Given an array = [2,3,4,5]
// It should return undefined

// find a way to set each element as key in a hash function
// And then set values to count
// if count is 2 return the index

// MY SOLUTION using the Map Object
array1 = [2, 5, 1, 2, 3, 5, 1, 2, 4];
array2 = [2, 1, 1, 2, 3, 5, 1, 2, 4];
array3 = [2, 3, 4, 5];

// function firstRecurringNumber(array) {
//   if (!Array.isArray(array)) {
//     return "Not an array";
//   }

//   const map = new Map();

//   for (let i = 0; i < array.length; i++) {
//     if (map.has(array[i])) {
//       return array[i];
//     } else {
//       map.set(array[i], 1);
//     }
//   }

//   return undefined;
// }

// Using javascript Object
function firstRecurringNumber1(array) {
  const map = {};
  for (let i = 0; i < array.length; i++) {
    if (map[array[i]] !== undefined) {
      return array[i];
    }
    map[array[i]] = i;
  }

  return undefined;
}

console.log(firstRecurringNumber1([2, 5, 5, 2, 3, 5, 1, 2, 4]));
// console.log(firstRecurringNumber1(array2));
// console.log(firstRecurringNumber1(array3));
