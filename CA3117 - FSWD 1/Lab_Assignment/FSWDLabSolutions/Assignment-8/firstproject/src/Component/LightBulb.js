import React, { useState } from 'react';

export default function LightBulb() {
  const [isOn, setIsOn] = useState(false);

  const onImg = "https://www.w3schools.com/js/pic_bulbon.gif";
  const offImg = "https://www.w3schools.com/js/pic_bulboff.gif";

  return (
    <div style={{border: '1px solid grey', padding: '10px', marginTop: '20px', textAlign: 'center'}}>
      <h3>Q5: Double Click Bulb</h3>
      
  
      <div onDoubleClick={() => setIsOn(!isOn)}>
        <img 
            src={isOn ? onImg : offImg} 
            alt="bulb" 
            style={{width: "100px", cursor: "pointer"}} 
        />
      </div>
      
      <p>{isOn ? "On Me" : "Off Me"}</p>
      <small>(Double-click the bulb to toggle)</small>
    </div>
  );
}