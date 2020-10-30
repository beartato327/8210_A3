import React, { Component } from 'react'

export class Navbar extends Component {
    render() {
        return (
            <nav className="blue-grey lighten-2">
                <div className="nav-wrapper container">
                <a href="#" className="brand-logo">Pet Report</a>
                <ul id="nav-mobile" className="right hide-on-med-and-down">
                    <li><a href="sass.html">Sass</a></li>
                    <li><a href="badges.html">Components</a></li>
                </ul>
                </div>
            </nav>
        )
    }
}

export default Navbar
