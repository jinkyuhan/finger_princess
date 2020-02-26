import React from 'react';
import {
    FormControl,
    InputLabel,
    Select,
    Button
} from '@material-ui/core'



class QuestionB extends React.Component {
    state = {
        env: "",
        bag: "",
        selectbox1: "휴대성",
        selectbox2: "가방 종류"
    }
    handlePrevious = () => {
        this.props.goPreviousSurvey();
    }
    handleNext = () => {
        if (this.state.env !== '') {
            if (this.state.env === "outdoor" || this.state.env === "both") {
                this.props.setParentAnswer("outdoor", true);
                if (this.state.bag !== "") {
                    this.props.setParentAnswer("bag", this.state.bag);
                    this.props.goNextSurvey();
                }
                else {
                    alert("필수 입력사항이 누락되었습니다.")
                }
            }
            else {
                this.props.setParentAnswer("outdoor", false);
                this.props.goNextSurvey();
            }
        }

        else {
            alert("필수 입력사항이 누락되었습니다.")
        }
    }


    handleChange = function (event) {
        if (event.target.name === "bagtype")
            this.setState({ bag: event.target.value, selectbox2: '' })
        else
            this.setState({ env: event.target.value, selectbox1: '' })
    }
    render() {
        let bag = <FormControl></FormControl>
        if (this.state.env === "outdoor" || this.state.env === "both") {
            bag =<FormControl variant="filled">
                        <InputLabel>가방 종류</InputLabel>
                        <Select
                            native
                            value={this.state.bag}
                            onChange={(event) => {
                                event.target.name = "bagtype"
                                this.handleChange(event)
                            }}
                        >
                            <option value="" />
                            <option value="eco-bag">에코백</option>
                            <option value="cross-bag">크로스백</option>
                            <option value="hand-bag">핸드백</option>
                            <option value="briefcase">서류가방</option>
                            <option value="backpack">백팩</option>
                        </Select>
                    </FormControl>
        }
        return (
            <div id="QuestionB">
                <div>
                    <FormControl variant="filled">
                        <InputLabel>휴대성</InputLabel>
                        <Select
                            native
                            value={this.state.env}
                            onChange={(event) => this.handleChange(event)}
                        >
                            <option value="" />
                            <option value="indoor">실내에서 사용</option>
                            <option value="outdoor">실외에서 사용</option>
                            <option value="both">실내외 겸용</option>
                        </Select>
                    </FormControl>
                    {bag}
                </div>
                <div>
                    <Button onClick={() => { this.handlePrevious() }} variant='contained'>이전</Button>
                    <Button onClick={() => { this.handleNext() }} variant='contained'>다음</Button>
                </div>
            </div>
        );
    }
}
export default QuestionB