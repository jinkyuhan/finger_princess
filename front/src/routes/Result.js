import React from 'react'
import { Grid } from '@material-ui/core'
import ResultCard from '../components/ResultCard'
import axios from 'axios'
import server from '../config'

class Result extends React.Component {

    state = {
        surveyResult:{},
        recommends: []
    }
    constructor(props){
        super(props);
        this.state.surveyResult = props.data;
    }

    getRecommends = async () => {
        const BASEURL = server.getBASEURL();
        let recommends = [];
        try {
            const res = await axios.post(`${BASEURL}/fp_api/services/recommend/`, this.state.surveyResult)
            recommends = res.data
        } catch(err){
            console.log(err)
        }
        console.log(recommends)
        console.log(recommends.length)
        if (recommends.length == 0) {
            alert('검색된 노트북이 없습니다.')
            window.history.back()
        }
        return recommends
    }

    renderResultCards = (recommends) => {
        let resultCards = []
        recommends.map((recommendedItem) => {
            resultCards.push(
                <Grid key={recommendedItem.id} item xs={12}>
                    <ResultCard laptop={recommendedItem} />
                </Grid >
            )
            return null
        })
        return resultCards;
    }

    async componentDidMount() {
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