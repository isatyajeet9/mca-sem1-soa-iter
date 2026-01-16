import React, { useState } from 'react'

export default function AddItems(props) {
    let addSty1={
        textAlign:"left"
    }
    const [title, setTitle]=useState("");
    const [price, setPrice]=useState("");
    const [imagg, setImag]=useState("");
    const addSubmitItem = ((e)=>{
        e.preventDefault();
        if(!title || !price || !imagg){
            alert("Submission Fields can not be blank!!");
        }
        else
            props.addItemForm(title,price,imagg);
    })
    return (
        <div className='container my-3' style={addSty1}>
            <h1>Add New Product</h1>
            <form onSubmit={addSubmitItem}>
                <div class="mb-3" style={addSty1}>
                    <label for="exampleInputEmail1" class="form-label">Product Name</label>
                    <input type="text" value={title} onChange={(e1)=>setTitle(e1.target.value)} class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"/>
                </div>
                <div class="mb-3" style={addSty1}>
                    <label for="exampleInputPassword1" class="form-label">Product Price</label>
                    <input type="number" value={price} onChange={(e1)=>setPrice(e1.target.value)} class="form-control" id="exampleInputPassword1"/>
                </div>
                <div class="mb-3" style={addSty1}>
                    <label for="exampleInputPassword1" class="form-label">Product Image</label>
                    <input type="file" onChange={(e1)=>setImag(URL.createObjectURL(e1.target.files[0]))} class="form-control" id="exampleInputPassword1"/>
                </div>
                <button type="submit" class="btn btn-primary">Add Product</button>
            </form>
        </div>
    )
}
