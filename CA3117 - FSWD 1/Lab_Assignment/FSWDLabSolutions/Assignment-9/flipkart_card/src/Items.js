import React from 'react'

export default function Items(props) {
    let sty1 = {
        width: "18rem",
        marginLeft:"6em",
        marginRight:"8em",
        marginTop: "2em",
        height: "30rem",
        marginBottom: "4em"
    }
    let sty2={
        border: "2px solid black"
    }
    return (
        <>
            <div class="col-sm-3">
                <div class="card" style={sty1}>
                    <img style={sty2} src={props.listItem.imag} class="card-img-top" alt="" height="320rem" width="35rem"/>
                    <div class="card-body">
                        <h5 class="card-title">{props.listItem.title}</h5>
                        <p class="card-text">Price: <b>{props.listItem.price}</b></p>
                        <button type="button" className="btn btn-sm btn btn-warning mx-3" onClick={() => props.updateEvnt(props.listItem)}>Update</button>
                        <button type="button" className="btn btn-sm btn-danger mx-3" onClick={() => props.deleteItem(props.listItem.sno)}>Delete</button>
                    </div>
                </div>
            </div>


            {/* <div>
        <h4>{props.listItem.title}</h4>
        <p>{props.listItem.price}</p>
        <button type="button" className="btn btn-sm btn-danger" onClick={()=>props.deleteItem(props.listItem.sno)}>Delete</button>
    </div> */}
        </>
    )
}
