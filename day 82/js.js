/*
  Write a function `findLargestElement` that takes an array of numbers and returns the largest element.
  Example:
  - Input: [3, 7, 2, 9, 1]
  - Output: 9
*/

function findLargestElement(numbers) {
    //
    let b=number[0];
    for (let i=0; i<number.length;i++){
        if(number[i]>b){
            b=number[i];
        }
    }
    return b;
}

module.exports = findLargestElement;
