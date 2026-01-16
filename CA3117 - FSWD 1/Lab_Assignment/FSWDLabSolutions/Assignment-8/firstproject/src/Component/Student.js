function Student(props) {
    return (
        <div style={{border: "1px solid black", margin: "10px", padding: "10px"}}>
            <p>Name: {props.data.name} </p>
            <p>Roll No: {props.data.roll} </p>
            <p>Department: {props.data.dept} </p>
        </div>
    );
}
export default Student;