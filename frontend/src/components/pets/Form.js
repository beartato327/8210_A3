import React, { Component } from 'react'

export class Form extends Component {
    constructor(props){
        super(props)
        this.state = {
            report_type: "GENERAL",
        }
    }

    onChange = e => this.setState({ [e.target.name]: e.target.value })
    onSubmit = e => { e.preventDefault(); console.log("submit"); }

    render() {
        const {report_type} = this.state
        return (
            <div>
                <h2>Add Report</h2>
                <form onSubmit={this.onSubmit}>
                    <div>
                        <label>Report Type</label>
                        <select name="report_type" onChange={this.onChange} value={report_type}>
                            <option value="VACCINES">Vaccines</option>
                            <option value="SURGERY">Surgery</option>
                            <option value="GENERAL">General</option>
                        </select> 
                    </div>
                </form>
            </div>
        )
    }
}

export default Form
