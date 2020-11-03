import {GET_PETS} from '../actions/types.js'

const initialState = {
    pets:[]
}

export default function(state = initialState, action){
    switch(action.type){
        case GET_PETS:
            return{
                ...state,
                pets: action.payload
            }
        default:
            return state
    }
}