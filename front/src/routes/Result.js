import React from 'react'
import { Grid } from '@material-ui/core'
import ResultCard from '../components/ResultCard'
import axios from 'axios'
import server from '../config'

class Result extends React.Component {

    state = {
        recommends:[]
    }

    getRecommends = async () => {
        const BASEURL = server.getBASEURL();
        const dataFromApp = this.props.data;
        // const recommends = await axios.post(`${BASEURL}/fp_api/recommned/`, dataFromApp) // example try catch 해줘야함
        const res = await axios.get(`${BASEURL}/fp_api/games/`) // test request
        const recommends = res.data
        return recommends
    }

    renderResultCards = (recommends) => {
        let resultCards = []
        recommends.map((recommendedItem) => {
            resultCards.push(
                <Grid  key={recommendedItem.id} item xs={12}>
                    <ResultCard laptop={recommendedItem} />
                </Grid >
            )
            return null
        })
        return resultCards;
    }

    async componentDidMount(){
        this.setState({
            recommends: await this.getRecommends()
        })
    }

    render() {

        return (
            <div className="result">
                <Grid container spacing={0}>
                    {this.renderResultCards(this.state.recommends)}
                </Grid>
            </div>
        )
    }
}



export default Result