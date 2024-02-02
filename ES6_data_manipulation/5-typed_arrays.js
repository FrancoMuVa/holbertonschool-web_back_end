export default function createInt8TypedArray(length, position, value) {
  if (position > length) {
    throw new Error('Position outside range');
  }
  const arrBuffer = new ArrayBuffer(length);
  const viewer = new DataView(arrBuffer);
  viewer.setInt8(position, value);
  return viewer;
}
