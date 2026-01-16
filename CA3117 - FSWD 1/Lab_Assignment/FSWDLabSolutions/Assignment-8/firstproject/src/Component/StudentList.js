import Student from "./Student";

function StudentList() {
  const students = [
    { name: "Satyajeet", roll: 101, dept: "CA" },
    { name: "Ankush", roll: 102, dept: "IT" },
    { name: "Rohit", roll: 103, dept: "CSE" },
    { name: "Sanket", roll: 104, dept: "ECE" },
  ];

  return (
    <div style={{border: '1px solid grey', padding: '10px', marginTop: '20px'}}>
      <h3>Q1: Student List</h3>
      
      <div style={{display: 'flex', flexWrap: 'wrap'}}>
        {students.map((stu, index) => (
          <Student key={index} data={stu} />
        ))}
      </div>
    </div>
  );
}

export default StudentList;