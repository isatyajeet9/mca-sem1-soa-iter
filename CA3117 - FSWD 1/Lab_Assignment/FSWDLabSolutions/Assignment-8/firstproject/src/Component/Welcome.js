import React, { useState } from 'react';

export default function Welcome() {
  const [show, setShow] = useState(false);

  return (
    <div style={{border: '1px solid grey', padding: '10px', marginTop: '20px'}}>
      <h3>Q3: Welcome Toggle</h3>
      <button onClick={() => setShow(!show)}>Toggle Message</button>
      {show && <h4 style={{color: 'blue'}}>Welcome to React!</h4>}
    </div>
  );
}