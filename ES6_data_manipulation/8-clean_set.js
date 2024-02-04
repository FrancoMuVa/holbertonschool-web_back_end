export default function cleanSet(set, startString) {
  if (startString === '') return '';
  let StrConCat = '';
  for (const item of set) {
    const splitSttr = item.split(startString);
    if (splitSttr.length > 1) {
      if (StrConCat !== '') {
        StrConCat += '-';
      }
      StrConCat += splitSttr[1];
    }
  }
  return StrConCat;
}
