import React from 'react';
import {
    FormGroup,
    FormControl,
    FormControlLabel,
    FormLabel,
    Checkbox
} from '@material-ui/core'
class QuestionA extends React.Component {
    state = {
        lol: false,
        pubg: false,
        fifa: false,
        overwatch: false
    }
    
    handleChange = function (name) {
        this.setState({[name]: !this.state[name]})
    }
    
    render() {
        return (
            <div id="QuestionA">
                <FormControl>
                    <FormLabel component="legend">Check all the games you play</FormLabel>
                    {/* demo */ }
                    <FormGroup>
                        <FormControlLabel
                            control={ <Checkbox checked={ this.state.lol } onChange={ () =>this.handleChange('lol') }  ></Checkbox> }
                            value="lol"
                            label="League of Legend"
                        />
                        <FormControlLabel
                            control={ <Checkbox checked={ this.state.pubg } onChange={ ()=>this.handleChange('pubg') }  ></Checkbox> }
                            value="pubg"
                            label="Battle Ground" />
                        <FormControlLabel
                            control={ <Checkbox checked={ this.state.fifa } onChange={ ()=>this.handleChange('fifa') }  ></Checkbox> }
                            value="fifa"
                            label="FIFA Online 4" />
                        <FormControlLabel
                            control={ <Checkbox checked={ this.state.overwatch } onChange={ ()=>this.handleChange('overwatch') }  ></Checkbox> }
                            value="overwatch"
                            label="OverWatch" />
                    </FormGroup>
                    {/* demo end */ }
                </FormControl>
            </div>
        );
    }
}

export default QuestionA