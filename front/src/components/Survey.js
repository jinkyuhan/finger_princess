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
    }

    // setParentAnswer = (key, value) => {
    //     this.setState(current => {
    //         let newState = current;
    //         newState.answer[key] = value;
    //         return newState;
    //     })
    //     this.props.setParentAnswer(this.state.answer)
    //     console.log(this.state.answer)
    // }
    hanldeSubmit = () => {
        console.log("request to api")   //request filtered id list
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
                                <QuestionA setParentAnswer={this.props.setParentAnswer} goNextSurvey={this.handleNext} goPreviousSurvey={this.handlePrevious}/>
                            </StepContent>
                        </Step>
                        < Step key={ 2 } >
                            <StepLabel>{ '실내/실외' }</StepLabel>
                            <StepContent>
                                <QuestionB setParentAnswer={this.props.setParentAnswer} goNextSurvey={this.handleNext} goPreviousSurvey={this.handlePrevious}/>
                            </StepContent>
                        </Step>
                        < Step key={ 3 } >
                            <StepLabel>{ '자주 사용하는 프로그램을 모두 선택하세요' }</StepLabel>
                            <StepContent>
                                <QuestionC setParentAnswer={this.props.setParentAnswer} goNextSurvey={this.handleNext} goPreviousSurvey={this.handlePrevious}/>
                            </StepContent>

                        </Step>
                        < Step key={ 4 } >
                            <StepLabel>{ '가격 상한선을 입력하세요' }</StepLabel>
                            <StepContent>
                                <QuestionD setParentAnswer={this.props.setParentAnswer} goNextSurvey={this.handleNext} goPreviousSurvey={this.handlePrevious}/>
                            </StepContent>

                        </Step>
                        < Step key={ 5 } >
                            <StepLabel>{ '정렬 기준을 선택하세요' }</StepLabel>
                            <StepContent>
                                <QuestionE setParentAnswer={this.props.setParentAnswer} goPreviousSurvey={this.handlePrevious} submitSurvey={this.hanldeSubmit}/>
                            </StepContent>
                        </Step>
                    </Stepper>
                </Container>
            </div >
        )
    }
}

export default Survey;