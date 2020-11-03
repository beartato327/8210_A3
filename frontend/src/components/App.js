import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import {Provider} from 'react-redux'
import store from '../store'

import Navbar from './layout/Navbar'
import Dashboard from './pets/Dashboard'

class App extends Component{
    render(){
        return (
            <Provider store={store}>
                <>
                    <Navbar />
                    <Dashboard />
                </>
            </Provider>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));