import './App.css';

import StudentList from './Component/StudentList';
import Counter from './Component/Counter';
import Welcome from './Component/Welcome';
import Languages from './Component/Languages';
import LightBulb from './Component/LightBulb';
import Registration from './Component/Registration';

function App() {
  return (
    <div className="App" style={{ padding: '20px' }}>
      <h1>React Assignment 8</h1>
      <StudentList />
      <Counter />
      <Welcome />
      <Languages />
      <LightBulb />
      <Registration />
    </div>
  );
}

export default App;