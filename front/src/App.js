import React from 'react';
import { HashRouter, Route } from 'react-router-dom';
import Welcome from './routes/Welcome';
import Questions from './routes/Questions'
import Result from './routes/Result'
class App extends React.Component {
  state = {
    answer: {
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
      newState.answer[key] = value;
      return newState;
    })
    console.log(this.state.answer)
  }
  render() {
    return (
      <HashRouter>
        <Route path='/' exact={true} component={Welcome} />
        {/* <Route path='/questions' exact={ true } component={ Questions } /> */}
        <Route path='/questions' exact={true} render={() => (
          <Questions setParentAnswer={this.setAnswer} />
        )
        } />
        {/* <Route path='/result' exact= { true } component={ Result }/> */}
        <Route path='/result' exact={true} render={() => (
          <Result data={this.state.answer} />
        )
        } />
      </HashRouter>
    )
  }
}

export default App;