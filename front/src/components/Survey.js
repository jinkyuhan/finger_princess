import React from 'react'
import QuestionA from './QuestionA'
import QuestionB from './QuestionB'
import QuestionC from './QuestionC'
import QuestionD from './QuestionD'
import { Stepper, Step, StepLabel, StepContent, Button, Container } from '@material-ui/core';


class Survey extends React.Component {
    state = {
        activeStep: 0,
        // steps: [
        //     {
        //         label: '게임을 하는 가',
        //         question: QuestionA
        //     },
        //     {
        //         label: '실내/실외',
        //         question: QuestionB
        //     },
        //     {
        //         label: '자주 쓰는 프로그램',
        //         question: QuestionA
        //     },
        //     {
        //         label: '가격 상한선',
        //         question: QuestionA
        //     },
        //     {
        //         label: '성능우선/가격우선/서비스우선',
        //         question: QuestionA
        //     }
        // ]
        steps: ['게임을 하는가', '실내/실외', '자주 쓰는 프로그램', '가격 상한선', '성능우선/가격우선/서비스우선'],
        messageFromQuestionA: ""
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
                    <Stepper activeStep={activeStep} orientation="vertical">
                        {/* {steps.map((step, index) => (
                            console.log(step)
                            < Step key = { index } >
                            <StepLabel>{step.label}</StepLabel>
                            <StepContent>{step.question}</StepContent>
                            </Step>
                    ))} */}
                        < Step key={1} >
                            <StepLabel>{'게임을 하는 가?'}</StepLabel>
                            <StepContent><QuestionA />
                                <Button onClick={this.handlePrevious} variant='contained'>이전</Button>
                                <Button onClick={this.handleNext} variant='contained'>다음</Button>
                            </StepContent>
                        </Step>
                        < Step key={2} >
                            <StepLabel>{'실내/실외'}</StepLabel>
                            <StepContent><QuestionB />
                                <Button onClick={this.handlePrevious} variant='contained'>이전</Button>
                                <Button onClick={this.handleNext} variant='contained'>다음</Button></StepContent>
                        </Step>
                        < Step key={3} >
                            <StepLabel>{'자주 사용하는 프로그램'}</StepLabel>
                            <StepContent><QuestionC />
                                <Button onClick={this.handlePrevious} variant='contained'>이전</Button>
                                <Button onClick={this.handleNext} variant='contained'>다음</Button></StepContent>

                        </Step>
                        < Step key={4} >
                            <StepLabel>{'가격 상한선'}</StepLabel>
                            <StepContent><QuestionD />
                                <Button onClick={this.handlePrevious} variant='contained'>이전</Button>
                                <Button onClick={this.handleNext} variant='contained'>다음</Button></StepContent>

                        </Step>
                        < Step key={5} >
                            <StepLabel>{'성능우선/기능우선/서비스우선'}</StepLabel>
                            <StepContent><QuestionA />
                                <Button onClick={this.handlePrevious} variant='contained'>이전</Button>
                                <Button onClick={this.handleNext} variant='contained'>제출</Button></StepContent>

                        </Step>
                    </Stepper>
                </Container>
            </div >
        )
    }
}

export default Survey;