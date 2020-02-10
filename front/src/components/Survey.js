import React from 'react'
import QuestionA from './QuestionA'
import QuestionB from './QuestionB' 
import { Stepper, Step, StepLabel, StepContent, Container } from '@material-ui/core';


class Survey extends React.Component {
    state = {
        activeStep: 0,
        steps:['게임을 하는 가','실내/실외', '자주 쓰는 프로그램', '가격 상한선', '성능우선/가격우선/서비스우선']
    }
    handleNext = () => {
        this.setState(current => ({ activeStep: current.activeStep + 1 }))
    };
    handlePrevious = () => {
        this.setState(current => ({ activeStep: current.activeStep - 1 }))
    };

    render() {
        const { activeStep,steps } = this.state;
        return (
            <div className='Survey'>
                <Container maxWidth='lg'>
                    <Stepper activeStep={activeStep} orientation="vertical">
                        {steps.map((label,index)=>( 
                                <Step key={index}>
                                    <StepLabel>{label}</StepLabel>
                                    <StepContent><QuestionB /></StepContent>
                                </Step> 
                            ))}
                    </Stepper>
                    
                </Container>
            </div>
        )
    }
}

export default Survey;