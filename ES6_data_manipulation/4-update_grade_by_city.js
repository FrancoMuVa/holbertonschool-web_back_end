export default function updateStudentGradeByCity(arrayOfStudents, city, newGrades) {
  const matching = arrayOfStudents.map((students) => {
    let stuGrade;
    if (students.location === city) {
      const matchId = newGrades.filter((obj) => obj.studentId === students.id);
      if (matchId.length > 0 && matchId[0].grade > 0) {
        stuGrade = matchId[0].grade;
      } else {
        stuGrade = 'N/A';
      }
      return {
        ...students,
        grade: stuGrade,
      };
    }
    return undefined;
  });
  return matching.filter((obj) => obj !== undefined);
}
