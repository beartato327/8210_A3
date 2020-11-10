import React, { Component } from 'react'
import { render } from 'react-dom'
import Navbar from './layout/Navbar'
import Dashboard from './pets/Dashboard'
import Login from './users/Login'
import Register from './users/Register'
import { HashRouter as Router, Route, Switch, Redirect } from "react-router-dom"

class App extends Component{

    render(){
    return(
        <Router>
        <>
            <Navbar />
            <div className="container">
                <Switch>
                    <Route exact path="/" component={Dashboard} />
                    <Route exact path="/register" component={Register} />
                    <Route exact path="/login" component={Login} />
                </Switch>
            </div>
        </>
        </Router>
    )
}      
}

export default App

const container = document.getElementById('app')
render(<App />, container)