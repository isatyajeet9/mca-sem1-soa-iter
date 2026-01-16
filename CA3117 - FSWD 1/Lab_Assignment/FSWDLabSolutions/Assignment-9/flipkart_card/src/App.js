import on from './on.png';
import off from './off.png';
import './App.css';
import { useState } from 'react';
import Items from './Items';
import Header from './Header';
import Footer from './Footer';
import AddItems from './AddItems'

import im1 from './images/im1.jpg'
import im2 from './images/im2.jpg'
import im3 from './images/im3.jpg'
import im4 from './images/img4.jpg'
import noImg from './images/noImg.jpg'

function App() {
  // 1st Implement
  // var arr1=[23, "ABC", true, 52.36]

  // 2nd Implement
  // const [isOn, setIsOn] = useState(false);
  // // let isOn=false
  // function onOff() {
  //   setIsOn (!isOn);
  // }
  let sty1 = {
    marginBottom:"2em"
  }
  let addSty1 = {
    textAlign: "left"
  }

  const [flipItem, updateitem] = useState(
    [
      {
        sno: 1,
        title: "Blanket",
        price: 500,
        imag: im1
      },
      {
        sno: 2,
        title: "T-Shirt",
        price: 1500,
        imag: im2
      },
      {
        sno: 3,
        title: "Rolex Watch",
        price: 20000,
        imag: im3
      },
      {
        sno: 4,
        title: "Samsung Galaxy A14",
        price: 50000,
        imag: im4
      }
    ]
  );

  function deleteItem(dltItm) {
    updateitem(
      flipItem.filter(e11 => {
        return (e11.sno !== dltItm)
      })
    )
  }

  // For Update Element
  const [uptitle, setTitle] = useState("");
  const [upprice, setPrice] = useState("");
  const [upimagg, setImag] = useState("");
  const [editItem, setEditItem] = useState(null);
  function updateEvnt(updItem) {
    setEditItem(updItem);  // show form
    setTitle(updItem.title);
    setPrice(updItem.price);
    setImag(updItem.imag);
  }
  const UpdateItemForm = (sno, title, price, imagg) => {
    updateitem(prev =>
      prev.map(item =>
        item.sno === sno
          ? { ...item, title, price, imag: imagg }
          : item
      )
    );
  };


  const addItemForm = (title, price, imagg) => {
    console.log("Added Item: ", title, " Price is: ", price)
    const myItem = {
      sno: flipItem[flipItem.length - 1].sno + 1,
      title: title,
      price: price,
      imag: imagg
    }
    updateitem([...flipItem, myItem]);
  }

  return (
    <div>
      {/* 1st Implement */}
      {/* <h1>FSWD Class</h1>
      <p>The Class is super Good</p>
      <b>{arr1.map((e1, index)=>{
        return (<span key={index}>{e1},</span>)
      })}</b> */}

      {/* 2nd Implement */}
      {/* <img src={isOn? on:off} alt="" height="500px" width="350px"/>
      <br />
      <button onClick={onOff}>
        {isOn?"Off Me":"On Me"}
      </button> */}
      <Header siteName="FSWD1 Products" />
      <AddItems addItemForm={addItemForm} />
      <h2>Product Details</h2>
      {flipItem.length == 0 ? "No To Do List" :
        <div class="row">
          {flipItem.map(e1 => {
            return (<Items listItem={e1} key={e1.sno} deleteItem={deleteItem} updateEvnt={updateEvnt} />);
          })}
        </div>
      }
      {/* Update Element */}
      {editItem && (
        <form className='container my-3' style={addSty1} onSubmit={(e) => {
          e.preventDefault();
          UpdateItemForm(editItem.sno, uptitle, upprice, upimagg);
          setEditItem(null);  // close form
        }}>
          <h3>Modify Details for Product No. {editItem.sno}</h3>

          <div className="mb-3" style={addSty1}>
            <label>Product Name</label>
            <input
              type="text"
              value={uptitle}
              onChange={(e1) => setTitle(e1.target.value)}
              className="form-control"
            />
          </div>

          <div className="mb-3" style={addSty1}>
            <label>Product Price</label>
            <input
              type="number"
              value={upprice}
              onChange={(e1) => setPrice(e1.target.value)}
              className="form-control"
            />
          </div>

          <div className="mb-3" style={addSty1}>
            <label>Product Image</label>
            <input
              type="file"
              onChange={(e1) => setImag(URL.createObjectURL(e1.target.files[0]))}
              className="form-control"
            />
          </div>

          <button className="btn btn-primary" style={sty1}>Modify</button>
        </form>
      )}
      <Footer siteName="FSWD1" />
    </div>
  );
}

export default App;
