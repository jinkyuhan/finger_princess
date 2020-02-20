import React from 'react'
import QuestionA from './QuestionA'
import QuestionB from './QuestionB'
import QuestionC from './QuestionC'
import QuestionD from './QuestionD'
import QuestionE from './QuestionE'
import { Stepper, Step, StepLabel, StepContent, Container } from '@material-ui/core';


class Survey extends React.Component {
    state = {
        activeStep: 0,
        steps: ['게임을 하는가', '실내/실외', '자주 쓰는 프로그램', '가격 상한선', '성능우선/가격우선/서비스우선'],
        answers: {
            games: {},
            outdoor: false,
            bag: "",
            programs: {},
            budget: 0,
            priority: ""
        }
    }

    setAnswer = (key, value) => {
        this.setState(current => {
            let newState = current;
            newState.answers[key] = value;
            return newState;
        })
        console.log(this.state.answers)
    }
    hanldeSubmit = () => {
        console.log("request to api")   //request filtered id list
        document.location.href = "localhost:3000/#/result"
    }
    handleNext = () => {
        this.setState(current => ({ activeStep: current.activeStep + 1 }))
    };
    handlePrevious = () => {
        this.setState(current => ({ activeStep: current.activeStep - 1 }))
    };
    render() {
        const { activeStep } = this.state;
        return (
            <div className='Survey'>
                <Container maxWidth='lg'>
                    <Stepper activeStep={ activeStep } orientation="vertical">
                        {/* {steps.map((step, index) => (
                            console.log(step)
                            < Step key = { index } >
                            <StepLabel>{step.label}</StepLabel>
                            <StepContent>{step.question}</StepContent>
                            </Step>
                    ))} */}
                        < Step key={ 1 } >
                            <StepLabel>{ '플레이 하는 모든 게임을 선택하세요' }</StepLabel>
                            <StepContent>
                                <QuestionA setParentAnswer={this.setAnswer} goNextSurvey={this.handleNext} goPreviousSurvey={this.handlePrevious}/>
                            </StepContent>
                        </Step>
                        < Step key={ 2 } >
                            <StepLabel>{ '실내/실외' }</StepLabel>
                            <StepContent>
                                <QuestionB setParentAnswer={this.setAnswer} goNextSurvey={this.handleNext} goPreviousSurvey={this.handlePrevious}/>
                            </StepContent>
                        </Step>
                        < Step key={ 3 } >
                            <StepLabel>{ '자주 사용하는 프로그램' }</StepLabel>
                            <StepContent>
                                <QuestionC setParentAnswer={this.setAnswer} goNextSurvey={this.handleNext} goPreviousSurvey={this.handlePrevious}/>
                            </StepContent>

                        </Step>
                        < Step key={ 4 } >
                            <StepLabel>{ '가격 상한선' }</StepLabel>
                            <StepContent>
                                <QuestionD setParentAnswer={this.setAnswer} goNextSurvey={this.handleNext} goPreviousSurvey={this.handlePrevious}/>
                            </StepContent>

                        </Step>
                        < Step key={ 5 } >
                            <StepLabel>{ '성능우선/기능우선/서비스우선' }</StepLabel>
                            <StepContent>
                                <QuestionE setParentAnswer={this.setAnswer} goPreviousSurvey={this.handlePrevious} submitSurvey={this.hanldeSubmit}/>
                            </StepContent>
                        </Step>
                    </Stepper>
                </Container>
            </div >
        )
    }
}

export default Survey;