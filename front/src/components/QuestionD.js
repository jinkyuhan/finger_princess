import React from 'react'
import {
    TextField,
    Button
} from '@material-ui/core'

class QuestionD extends React.Component {
    state = {
        error: false,
        helptxt: "",
        budget: 0
    }

    validate = (event) => {
        if (!event.target.value.match(/^[0-9]*$/)) {
            this.setState({ error: true, helptxt: "숫자만 입력하세요" })
            return false
        }
        else {
            this.setState({ error: false, helptxt: "", budget: Number(event.target.value) })
            return true
        }
    }
    handlePrevious = () => {
        this.props.goPreviousSurvey();
    }
    handleNext = (event) => {
        if (this.state.error === false) {
            this.props.setParentAnswer("budget", this.state.budget);
            this.props.goNextSurvey();
        }
        else{
            alert("잘못된 입력입니다.")
        }
    }

    render() {
        return (
            <div id="QuestionD">
                <form autoComplete="off">
                    <div>
                        <TextField
                            fullWidth
                            variant="filled"
                            margin="normal"
                            error={ this.state.error }
                            id="budget_limit"
                            label="상한 금액을 입력하세요"
                            helperText={ this.state.helptxt }
                            onChange={ this.validate }
                        />
                    </div>
                </form>
                <div>
                    <Button onClick={ () => { this.handlePrevious() } } variant='contained'>이전</Button>
                    <Button onClick={ () => { this.handleNext() } } variant='contained'>다음</Button>
                </div>

            </div>
        )
    }
}


export default QuestionD