import React from 'react'
import {
    Button,
    FormControl,
    InputLabel,
    Select
} from '@material-ui/core'
class QuestionE extends React.Component {

    state = {
        priority: ""
    }
    handleSubmit = () => {
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
                <FormControl variant="filled" style={
                    { 
                        minWidth: 150 
                    }
                }>
                    <InputLabel>정렬 우선순위</InputLabel>
                    <Select
                        native
                        value={this.state.priority}
                        onChange={(event) => {
                            this.handleChange(event)
                        }}
                    >
                        <option value="" />
                        <option value="performance-first">성능우선</option>
                        <option value="price-first">가격우선</option>
                        <option value="service-first">서비스우선</option>
                    </Select>
                </FormControl>
                <div>
                    <Button onClick={() => { this.handlePrevious() }} variant='contained'>이전</Button>
                    <Button href="#result" onClick={() => { this.handleSubmit() }} variant='contained'>제출</Button>
                </div>
            </div>
        )
    }
}


export default QuestionE