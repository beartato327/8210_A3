import React, { Component } from 'react'

export default class Navbar extends Component {
    render() {
        return (
            <nav>
                <div class="nav-wrapper container">
                <a href="#" class="brand-logo">Pet Report</a>
                <ul id="nav-mobile" class="right">
                    <li><a href="sass.html">Login</a></li>
                </ul>
                </div>
            </nav>
        )
    }
}
