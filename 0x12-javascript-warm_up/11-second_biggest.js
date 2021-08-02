#!/usr/bin/node
function selectionSort (array, size) {
  let pos, min;

  if (!array) { return; }

  for (let i = 0; i < size - 1; i++) {
    min = array[i];
    for (let x = i + 1; x < size; x++) {
      if (array[x] < min) {
        min = array[x];
        pos = x;
      }
    }
    if (array[i] !== min) {
      array[pos] = array[i];
      array[i] = min;
    }
  }
  return array;
}
const array = [];
const len = process.argv.length;
if (len < 3 || len === 3) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    array.push(process.argv[i]);
  }
  const newArray = selectionSort(array, array.length);
  console.log(newArray[newArray.length - 2]);
}
