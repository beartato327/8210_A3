import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import Navbar from './layout/Navbar'
import Dashboard from './pets/Dashboard'

class App extends Component{
    render(){
        return (
            <>
                <Navbar />
                <Dashboard />
            </>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));