import React from 'react'

export default function Footer() {
  let ftStyl={
    position: "fixed",
    bottom: "0",
    backgroundColor: "black",
    color: "white",
    textAlign: "center",
    width: "100%"
  }
  return (
    <div style={ftStyl}>
      Copyright &copy; FSWD1 Lab by Debabrata Roy
    </div>
  )
}
