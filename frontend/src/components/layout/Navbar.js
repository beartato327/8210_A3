import React, { Component } from 'react'

export default class Navbar extends Component {
    render() {
        return (
            <nav>
                <div className ="nav-wrapper container">
                <a href="#" className ="brand-logo">Pet Report</a>
                <ul id="nav-mobile" className ="right">
                    <li><a href="sass.html">Login</a></li>
                </ul>
                </div>
            </nav>
        )
    }
}
