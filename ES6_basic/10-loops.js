export default function appendToEachArrayValue(array, appendString) {
  const newArray = array;
  for (const item of array) {
    const idx = array.indexOf(item);
    newArray[idx] = appendString + item;
  }

  return newArray;
}
