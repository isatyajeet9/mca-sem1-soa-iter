import React, { useState } from 'react';

export default function Registration() {
  const [formData, setFormData] = useState({ name: "", email: "", password: "" });
  const [submitted, setSubmitted] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (formData.name && formData.email && formData.password) {
      setSubmitted(formData);
    } else {
      alert("All fields are required!");
    }
  };

  return (
    <div style={{border: '1px solid grey', padding: '10px', marginTop: '20px'}}>
      <h3>Q6: Registration Form</h3>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Name" onChange={(e) => setFormData({...formData, name: e.target.value})} /><br/>
        <input type="email" placeholder="Email" onChange={(e) => setFormData({...formData, email: e.target.value})} /><br/>
        <input type="password" placeholder="Password" onChange={(e) => setFormData({...formData, password: e.target.value})} /><br/>
        <button type="submit">Register</button>
      </form>
      
      {submitted && (
        <div style={{marginTop: '10px', color: 'green'}}>
            <p>Name: {submitted.name}</p>
            <p>Email: {submitted.email}</p>
        </div>
      )}
    </div>
  );
}