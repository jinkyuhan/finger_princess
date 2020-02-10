import React from 'react';
import {
    FormGroup,
    FormControl,
    FormControlLabel,
    FormLabel,
    Checkbox
} from '@material-ui/core'
class QuestionC extends React.Component {
    state = {
        photoshop: false,
        premiere_pro: false,
        auto_cad: false,
        vmware: false
    }
    
    handleChange = function (name) {
        this.setState({[name]: !this.state[name]})
    }
    
    render() {
        return (
            <div id="QuestionC">
                <FormControl>
                    <FormLabel component="legend">Check all the programs you use</FormLabel>
                    {/* demo */ }
                    <FormGroup>
                        <FormControlLabel
                            control={ <Checkbox checked={ this.state.photoshop } onChange={ () =>this.handleChange('photoshop') }  ></Checkbox> }
                            value="photoshop"
                            label="Adobe Photoshop"
                        />
                        <FormControlLabel
                            control={ <Checkbox checked={ this.state.premiere_pro } onChange={ ()=>this.handleChange('premiere_pro') }  ></Checkbox> }
                            value="premiere_pro"
                            label="Adobe Premiere Pro" />
                        <FormControlLabel
                            control={ <Checkbox checked={ this.state.auto_cad } onChange={ ()=>this.handleChange('auto_cad') }  ></Checkbox> }
                            value="auto_cad"
                            label="IBM Auto_cad" />
                        <FormControlLabel
                            control={ <Checkbox checked={ this.state.vmware } onChange={ ()=>this.handleChange('vmware') }  ></Checkbox> }
                            value="vmware"
                            label="Vmware playerstation" />
                    </FormGroup>
                    {/* demo end */ }
                </FormControl>
            </div>
        );
    }
}

export default QuestionC