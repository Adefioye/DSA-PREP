const array1 = [0, 3, 4, 31];
const array2 = [4, 6, 30];

function mergeSortedArrays(arr1, arr2) {
  // check if the inputs are arrays
  // loop over each array and add the items to a  new array
  // the array with the items is then sorted
  if (Array.isArray(arr1) !== true || Array.isArray(arr2) !== true) {
    return "Incorrect input, Please use an array object";
  }

  const mergedArray = [];
  for (let i = 0; i < arr1.length; i++) {
    mergedArray.push(arr1[i]);
  }

  for (let i = 0; i < arr2.length; i++) {
    mergedArray.push(arr2[i]);
  }

  return mergedArray.sort((a, b) => a - b);
}

console.log(mergeSortedArrays(array1, array2));
