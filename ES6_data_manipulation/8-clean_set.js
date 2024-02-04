export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') return '';
  let StrConCat = '';
  for (const item of set) {
    if (item && item.startsWith(startString)) {
      if (StrConCat.length === 0) {
        StrConCat += item.replace(startString, '');
      } else {
        StrConCat += item.replace(startString, '-');
      }
    }
  }
  return StrConCat;
}
