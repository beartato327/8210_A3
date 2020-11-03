import React, { Component } from 'react'
import { render } from 'react-dom'
import Navbar from './layout/Navbar'
import Dashboard from './pets/Dashboard'

class App extends Component{

    render(){
    return(
        <>
            <Navbar />
            <div className="container">
                <Dashboard />
            </div>
        </>
    )
}      
}

export default App

const container = document.getElementById('app')
render(<App />, container)