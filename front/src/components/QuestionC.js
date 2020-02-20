import React from 'react';
import server from '../config'
import axios from 'axios'
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
        programs: {}
    }

    FormControls = []

    handlePrevious = () => {
        this.props.goPreviousSurvey();
    }
    handleNext = function () {
        this.props.setParentAnswer("programs", this.state.programs)
        this.props.goNextSurvey()
    }

    handleChange = function (name) {
        this.setState(current => {
            let newPrograms = current.programs;
            newPrograms = { ...newPrograms, [name]: !(current.programs[name]) }
            return {
                programs: newPrograms
            }
        })
    }

    getPrograms = async () => {
        const BASEURL = server.getBASEURL();
        let data;
        try {
            const res = await axios.get(`${BASEURL}/fp_api/programs/`)
            data = res.data
        }
        catch (Error) {
            console.log(Error)
        }
        return data
    }

    //setState는 절대로 반복문 안에서 호출하지 않는다.
    loadPrograms = (data) => {
        let newPrograms = {}
        for (let idx in data) {
            newPrograms[data[idx].name] = false;
        }
        this.setState({
            programs: newPrograms
        })
    }

    renderForms = (programs) => {
        let FormControls = []
        for (let programName in programs) {
            FormControls.push(
                <FormControlLabel
                        key = {programName}
                        control={<Checkbox
                        checked={programs.programName}
                        onChange={() => this.handleChange(programName)}
                    ></Checkbox>}
                    label={programName}
                />
            )
        }
        return FormControls
    }

    // Data 구독은 did mount에서
    async componentDidMount() {
        const data = await this.getPrograms()
        this.loadPrograms(data)
    }

    render() {
        return (
            <div id="QuestionC">
                <FormControl>
                    <FormLabel component="legend">Check all the games you play</FormLabel>
                    <FormGroup>
                        {this.renderForms(this.state.programs)}
                    </FormGroup>
                </FormControl>
                <div>
                    <Button onClick={() => { this.handlePrevious() }} variant='contained'>이전</Button>
                    <Button onClick={() => { this.handleNext() }} variant='contained'>다음</Button>
                </div>
            </div>
        );
    }
}

export default QuestionA