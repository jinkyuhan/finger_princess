import React from 'react';
import { Container} from '@material-ui/core'
import QuestionA from './QuestionA'


class Survey extends React.Component {
    render() {
        return (
            <div className="Survey">
                <Container maxWidth="lg">
                    <QuestionA />
                </Container>
            </div>
        )
    }
}

export default Survey