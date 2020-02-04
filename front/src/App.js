import React from 'react';
import Survey from './components/Survey'
import Navigation from './components/Navigation'
import './App.css'
import { Grid } from '@material-ui/core'
class App extends React.Component {
  render() {
    return (
      <div className="App" >
        <Grid container spacing={3}>
          <Grid item xs={12}>
          </Grid>
          <Grid item xs={3}>
            <Navigation />
          </Grid>
          <Grid item xs={9}>
            <Survey />
          </Grid>
        </Grid>

      </div>
    )
  }
}

export default App;