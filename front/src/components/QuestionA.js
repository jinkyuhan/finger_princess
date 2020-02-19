import React from 'react';
import {
    FormGroup,
    FormControl,
    FormControlLabel,
    FormLabel,
    Checkbox,
    Button
} from '@material-ui/core'
class QuestionA extends React.Component {
    state = {
        lol: false,
        pubg: false,
        fifa: false,
        overwatch: false
    }
    handlePrevious = () => {
        this.props.goPreviousSurvey();
    }
    handleNext = function () {
        this.props.setParentAnswer("games", this.state)
        this.props.goNextSurvey()
    }

    handleChange = function (name) {
        this.setState({ [name]: !this.state[name] })
    }

    render() {
        const variable = [<div>hello1</div>, <div>hello2</div>]
        
        return (
            <div id="QuestionA">
                <FormControl>
                    <FormLabel component="legend">Check all the games you play</FormLabel>
                    {/* demo */ }
                    <FormGroup>
                        {/* <FormControlLabel
                            control={ <Checkbox checked={ this.state.lol } onChange={ () => this.handleChange('lol') }  ></Checkbox> }
                            value="lol"
                            label="League of Legend"
                        />
                        <FormControlLabel
                            control={ <Checkbox checked={ this.state.pubg } onChange={ () => this.handleChange('pubg') }  ></Checkbox> }
                            value="pubg"
                            label="Battle Ground" />
                        <FormControlLabel
                            control={ <Checkbox checked={ this.state.fifa } onChange={ () => this.handleChange('fifa') }  ></Checkbox> }
                            value="fifa"
                            label="FIFA Online 4" />
                        <FormControlLabel
                            control={ <Checkbox checked={ this.state.overwatch } onChange={ () => this.handleChange('overwatch') }  ></Checkbox> }
                            value="overwatch"
                            label="OverWatch" /> */}
                    </FormGroup>
                    {/* demo end */ }
                </FormControl>
                <div>
                    <Button onClick={ () => { this.handlePrevious() } } variant='contained'>이전</Button>
                    <Button onClick={ () => { this.handleNext() } } variant='contained'>다음</Button>
                </div>
                {variable}
            </div>
        );
    }
}

export default QuestionA