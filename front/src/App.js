import React from 'react';
import Survey from './components/Survey'
import Header from './components/Header'
import './App.css'
import { Grid } from '@material-ui/core'
class App extends React.Component {
  render() {
    return (
      <div className="App" >
        <Grid container spacing={3}>
          <Grid item xs={12}>
           <Header />
          </Grid>
          <Grid item xs={12}>
            <Survey />
          </Grid>
        </Grid>
      </div>
    )
  }
}

export default App;