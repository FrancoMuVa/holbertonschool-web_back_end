export default function getStudentIdsSum(arrayOfStudents) {
  return arrayOfStudents.reduce((counter, current) => counter + current.id, 0);
}
