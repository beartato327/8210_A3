import React, { Component } from 'react'
import {Link} from 'react-router-dom'

export default class Navbar extends Component {
    render() {
        return (
            <nav>
                <div className ="nav-wrapper container">
                <a href="#" className ="brand-logo">Pet Report</a>
                <ul id="nav-mobile" className ="right">
                    <li><Link to="/register">Register</Link> </li>
                    <li><Link to="/login">Login</Link></li>
                </ul>
                </div>
            </nav>
        )
    }
}
