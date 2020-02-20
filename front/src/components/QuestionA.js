import React from 'react';
import server from '../config'
import axios from 'axios'
import {
    FormGroup,
    FormControl,
    FormControlLabel,
    FormLabel,
    Checkbox,
    Button
} from '@material-ui/core'



class QuestionA extends React.Component {
    state = {
        games: {}
    }

    FormControls = []

    handlePrevious = () => {
        this.props.goPreviousSurvey();
    }
    handleNext = function () {
        this.props.setParentAnswer("games", this.state.games)
        this.props.goNextSurvey()
    }

    handleChange = function (name) {
        this.setState(current => {
            let newGames = current.games;
            newGames = { ...newGames, [name]: !(current.games[name]) }
            return {
                games: newGames
            }
        })
    }

    getGames = async () => {
        const BASEURL = server.getBASEURL();
        let data;
        try {
            const res = await axios.get(`${BASEURL}/fp_api/games/`)
            data = res.data
        }
        catch (Error) {
            console.log(Error)
        }
        return data
    }

    //setState는 절대로 반복문 안에서 호출하지 않는다.
    loadGames = (data) => {
        let newGames = {}
        for (let idx in data) {
            newGames[data[idx].name] = false;
        }
        this.setState({
            games: newGames
        })
    }

    renderForms = (games) => {
        let FormControls = []
        for (let gameName in games) {
            FormControls.push(
                <FormControlLabel
                        key = {gameName}
                        control={<Checkbox
                        checked={games.gameName}
                        onChange={() => this.handleChange(gameName)}
                    ></Checkbox>}
                    label={gameName}
                />
            )
        }
        return FormControls
    }

    // Data 구독은 did mount에서
    async componentDidMount() {
        const data = await this.getGames()
        this.loadGames(data)
    }

    render() {
        return (
            <div id="QuestionA">
                <FormControl>
                    <FormLabel component="legend">Check all the games you play</FormLabel>
                    <FormGroup>
                        {this.renderForms(this.state.games)}
                    </FormGroup>
                </FormControl>
                <div>
                    <Button onClick={() => { this.handleNext() }} variant='contained'>다음</Button>
                </div>
            </div>
        );
    }
}

export default QuestionA