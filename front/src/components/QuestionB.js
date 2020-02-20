import React from 'react';
import {
    MenuItem,
    FormControl,
    InputLabel,
    Select,
    Button
} from '@material-ui/core'



class QuestionB extends React.Component {
    state = {
        env: "",
        bag: ""
    }
    handlePrevious = () => {
        this.props.goPreviousSurvey();
    }
    handleNext = () => {
        if (this.state.env !== '') {
            if (this.state.env === "outdoor" || this.state.env === "both") {
                this.props.setParentAnswer("outdoor", true);
                this.props.setParentAnswer("bag", this.state.bag);
            }
            else{
                this.props.setParentAnswer("outdoor", false);
            }
            this.props.goNextSurvey();
        }

        else {
            alert("잘못된 입력입니다.")

        }
    }


    handleChange = function (event) {
        if (event.target.name === "bagtype")
            this.setState({ bag: event.target.value })
        else
            this.setState({ env: event.target.value })
    }
    render() {
        let bag = <div></div>
        if (this.state.env === "outdoor" || this.state.env === "both") {
            bag =
                <div>
                    <FormControl>
                        <InputLabel id="bag" variant="outlined">Bag</InputLabel>
                        <Select
                            labelId="bag-select-label"
                            id="bag-select"
                            value={this.state.bag}
                            onChange={(event) => {
                                event.target.name = "bagtype"
                                this.handleChange(event)
                            }}
                            variant='filled'
                        // required={true}
                        >
                            <MenuItem value="eco-bag">에코백</MenuItem>
                            <MenuItem value="cross-bag">크로스백</MenuItem>
                            <MenuItem value="hand-bag">핸드백</MenuItem>
                            <MenuItem value="briefcase">서류가방</MenuItem>
                            <MenuItem value="backpack">백팩</MenuItem>

                        </Select>
                    </FormControl>
                </div>
        }
        return (
            <div id="QuestionB">
                <FormControl style={
                    {
                        minWidth: 120
                    }
                }>
                    <InputLabel id="env" variant='outlined'>휴대성</InputLabel>
                    <Select
                        labelId="env-select-label"
                        id="env-select"
                        value={this.state.env}
                        onChange={(event) => this.handleChange(event)}
                        variant='filled'
                    // required={true}
                    >
                        <MenuItem value="indoor">실내에서 사용</MenuItem>
                        <MenuItem value="outdoor">실외에서 사용</MenuItem>
                        <MenuItem value="both">실내외 겸용</MenuItem>
                    </Select>
                </FormControl>
                {bag}
                <div>
                    <Button onClick={() => { this.handlePrevious() }} variant='contained'>이전</Button>
                    <Button onClick={() => { this.handleNext() }} variant='contained'>다음</Button>
                </div>
            </div>
        );
    }
}
export default QuestionB