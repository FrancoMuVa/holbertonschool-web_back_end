export default function updateUniqueItems(map) {
  for (const item of map) {
    if (item[1] === 1) {
      item[1] = 100;
    }
    map.set(item[0], item[1]);
  }
  return map;
}
