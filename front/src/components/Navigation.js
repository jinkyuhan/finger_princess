import React from 'react'
import { Stepper, Step, StepLabel, Container, Button } from '@material-ui/core';


class Navigation extends React.Component {
    state = {
        activeStep: 0,
        steps: ['게임을 하는가?', '실내/실외', '자주 쓰는 프로그램', '가격상한선', '성능우선/가격우선/서비스우선']
    }

    handleNext = () => {
        this.setState(current => ({ activeStep: current.activeStep + 1 }))
    };
    handlePrevious = () => {
        this.setState(current => ({ activeStep: current.activeStep - 1 }))
    };

    render() {
        const { activeStep, steps } = this.state;
        return (
            <div className='Navigation'>
                <Container maxWidth='lg'>
                    <Stepper activeStep={activeStep} orientation="vertical">
                        {steps.map((label, index) => (
                            <Step key={label}>
                                <StepLabel>{label}</StepLabel>
                            </Step>
                        ))}
                    </Stepper>
                    <Button variant="outlined" onClick={this.handlePrevious}>이전</Button>
                    <Button variant="outlined" onClick={this.handleNext}>다음</Button>
                </Container>
            </div>
        )
    }
}

export default Navigation;