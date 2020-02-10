import React from 'react'
import {
    FormControl,
    InputLabel,
    Select,
    MenuItem
} from '@material-ui/core'
class QuestionE extends React.Component {

    state = {
        priority: ""
    }
    handleChange = function (event) {
        this.setState({ priority: event.target.value })
    }
    render() {
        return (
            <div id="QuestionE">
                <FormControl>
                    <InputLabel id="priority" variant="filled" ></InputLabel>
                    <Select
                        labelId="priority-select-label"
                        id="priority-select"
                        value={ this.state.priority }
                        onChange={ (event) => {
                            this.handleChange(event)
                        } }
                    >
                        <MenuItem value="performance-first">성능우선</MenuItem>
                        <MenuItem value="price-first">가격우선</MenuItem>
                        <MenuItem value="service-first">서비스우선</MenuItem>
                    </Select>
                </FormControl>
            </div>
        )
    }
}


export default QuestionE