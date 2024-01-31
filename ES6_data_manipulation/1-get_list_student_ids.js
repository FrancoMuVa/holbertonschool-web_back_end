export default function getListStudentIds(arrayOfStudents) {
  if (!Array.isArray(arrayOfStudents)) {
    return [];
  }
  const newArray = arrayOfStudents.map((obj) => obj.id);
  return newArray;
}
