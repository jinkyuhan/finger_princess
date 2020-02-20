import React from 'react'
import { Grid } from '@material-ui/core'
import ResultCard from '../components/ResultCard'

class Result extends React.Component {
    
    render() {
        console.log(this.props.data)
        return (
            <div className="result">
                <Grid container spacing={ 0 }>
                    <Grid item xs={ 12 }>
                        <ResultCard />
                    </Grid>
                </Grid>
            </div>
        )
    }
}



export default Result