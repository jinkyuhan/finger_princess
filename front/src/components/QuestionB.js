import React from 'react';
import {
    MenuItem,
    FormControl,
    FormControlLabel,
    InputLabel,
    FormHelperText,
    FormLabel,
    Select
} from '@material-ui/core'



class QuestionB extends React.Component {
    state = {
        env: "",
        // inputLabel: "indoor",
        // labelWidth: 100
    }

    handleChange = function (event) {
        this.setState({ env: event.target.value })
    }
    render() {
        let bag = <div></div>
        if (this.state.env == "outdoor" || this.state.env == "both"){
            bag = <div>hihi</div>  
        }
        return (
            <div id="QuestionB">
                <FormControl>
                    <InputLabel id="env" variant="filled" ></InputLabel>
                    <Select
                        labelId="env-select-label"
                        id="env-select"
                        value={this.state.env}
                        onChange={(event) => this.handleChange(event)}
                        // required={true}
                    >
                        <MenuItem value="indoor">실내에서 사용</MenuItem>
                        <MenuItem value="outdoor">실외에서 사용</MenuItem>
                        <MenuItem value="both">실내외 겸용</MenuItem>
                    </Select>
                </FormControl>
                {bag}
            </div>
        );
    }
}
export default QuestionB