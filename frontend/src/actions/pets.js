import axios from 'axios'

import {GET_PETS} from './types'

// GET PETS
export const getPets = () => dispatch => {
    axios.get('/api/pets/')
    .then(res=>{
        dispatch({
            type: GET_PETS,
            payload: res.data
        })
    }).catch(err => console.log(err))
}