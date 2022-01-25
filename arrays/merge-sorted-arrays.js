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

// console.log(mergeSortedArrays(array1, array2));

function mergeSortedArrays2(array1, array2) {
  // Typical assumption is that array is sorted
  // check inputs to confirm they have elements, if one of then don't, return the other
  const mergeArrays = [];
  let array1Item = array1[0];
  let array2Item = array2[0];
  let i = 0;
  let j = 0;

  if (array1.length === 0) {
    return arr2.sort();
  }

  if (array2.length === 0) {
    return arr1.sort();
  }

  if (Array.isArray(array1) !== true || Array.isArray(array2) !== true) {
    return "Incorrect input, Please use an array object";
  }

  while (array1Item || array2Item) {
    if (!array2Item || array1Item < array2Item) {
      console.log(array1Item, array2Item);
      mergeArrays.push(array1Item);
      i++;
      array1Item = array1[i];
    } else {
      mergeArrays.push(array2Item);
      j++;
      array2Item = array2[j];
    }
  }
  return mergeArrays;
}
console.log(mergeSortedArrays2([0, 3, 4, 31], [4, 6, 30]));
