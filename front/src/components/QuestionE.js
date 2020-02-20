import React from 'react'
import {
    Button,
    FormControl,
    InputLabel,
    Select,
    MenuItem
} from '@material-ui/core'
class QuestionE extends React.Component {

    state = {
        priority: ""
    }
    handleSubmit = () =>{
        this.props.setParentAnswer("priority", this.state.priority);
        this.props.submitSurvey();
    }
    handlePrevious = () => {
        this.props.goPreviousSurvey();
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
                <div>
                    <Button onClick={ () => { this.handlePrevious() } } variant='contained'>이전</Button>
                    <Button href="#result" onClick={ () => { this.handleSubmit() } } variant='contained'>제출</Button>
                </div>
            </div>
        )
    }
}


export default QuestionE