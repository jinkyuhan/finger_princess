import React from 'react'
import { TextField } from '@material-ui/core'

class QuestionD extends React.Component {
    state = {
        error: false,
        helptxt: ""
    }
    validate = (event) => {
        if (!event.target.value.match(/^[0-9]*$/)) {
            this.setState({ error: true, helptxt: "숫자만 입력하세요" })
        }
        else {
            this.setState({ error: false, helptxt: "" })
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
                            onChange={ this.validate } />
                    </div>
                </form>
            </div>
        )
    }
}


export default QuestionD