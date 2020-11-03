import React, { Component } from 'react'
import {connect} from 'react-redux'
import PropTypes from 'prop-types'
import {getPets} from '../../actions/pets'

export class Pets extends Component {
    static propTypes = {
        pets: PropTypes.array.isRequired
    }

    componentDidMount(){
        console.log(this.props.getPets())
        this.props.getPets()
    }

    render() {
        return (
            <>
                <h2>Pets</h2>
                <table>
                    <th>ID</th>
                    <th>Name</th>
                    <tbody>
                        {this.props.pets.map(pets => {
                            
                            <tr key={pets.id}>
                                console.log(pets.id)
                                <td>{pets.id}</td>
                                <td>{pets.name}</td>
                            </tr>
                        })}
                    </tbody>
                </table>
            </>
        )
    }
}

const mapStateToProps = state =>({
    pets: state.pets.pets
})

export default connect(mapStateToProps, {getPets})(Pets)
