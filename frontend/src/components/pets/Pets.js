import React, { Component } from 'react'

class Pets extends Component {
    constructor(props){
        super(props)
        this.state = {
            data:[],
            loaded: false,
            placeholder: "Loading"
        }
    }

    componentDidMount(){
        fetch("api/pet")
        .then(response =>{
            if(response.status > 400){
                return this.setState(() =>{
                    return {placeholder: "Something went wrong!"}
                })                
            }
            return response.json()
        })
        .then(data => {
            this.setState(() => {
                return{
                    data,
                    loaded: true
                }
            })
        })
    }

    render() {
        return (
            <div>
                <table className="striped">
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Age</th>
                            <th>Type</th>
                            <th>Breed</th>
                            <th />
                        </tr>
                    </thead>
                    <tbody>
                        
                            {this.state.data.map(pet => {
                                return(
                                    <tr key={pet.id}>
                                        <td >
                                            {pet.pet_name}
                                        </td>
                                        <td>
                                            {pet.pet_age}
                                        </td>
                                        <td>
                                            {pet.pet_type}
                                        </td>
                                        <td>
                                            {pet.pet_breed}
                                        </td>
                                        <td>
                                            <button className="btn">Add Report</button>
                                        </td>
                                    </tr>
                                )
                            })}
                    </tbody>
                </table>
            
            </div>
        )
    }
}

export default Pets
