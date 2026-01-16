import React, { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div style={{border: '1px solid grey', padding: '10px', marginTop: '20px'}}>
      <h3>Q2: Counter</h3>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount((count > 0) ? count - 1 : 0)}>Decrement</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}