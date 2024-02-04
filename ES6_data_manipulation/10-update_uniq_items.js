export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) throw new Error('Cannot process');
  for (const item of map) {
    if (item[1] === 1) {
      item[1] = 100;
    }
    map.set(item[0], item[1]);
  }
  return map;
}
