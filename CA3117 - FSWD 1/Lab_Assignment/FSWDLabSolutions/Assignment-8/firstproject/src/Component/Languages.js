import React, { useState } from 'react';

export default function Languages() {
  const [langs, setLangs] = useState(["JavaScript", "Python", "Java"]);
  const [inputVal, setInputVal] = useState("");

  const addLang = () => {
    if(inputVal) {
        setLangs([...langs, inputVal]);
        setInputVal("");
    }
  };

  return (
    <div style={{border: '1px solid grey', padding: '10px', marginTop: '20px'}}>
      <h3>Q4: Languages</h3>
      <ul>
        {langs.map((lang, i) => <li key={i}>{lang}</li>)}
      </ul>
      <input 
        type="text" 
        value={inputVal} 
        onChange={(e) => setInputVal(e.target.value)} 
        placeholder="Add new language"
      />
      <button onClick={addLang}>Add</button>
    </div>
  );
}