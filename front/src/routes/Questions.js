import React from 'react';
import Survey from '../components/Survey'
import Header from '../components/Header'
import { Grid } from '@material-ui/core'
import { withStyles } from '@material-ui/core/styles';

const styles = {
  root: {
    fontFamily: 'Nanum Gothic',
  }
}

class Questions extends React.Component {

  render() {
    const {classes} = this.props;
    return (
      <div className={classes.root}>
        <Grid container spacing={ 3 } >
          <Grid item xs={ 12 }>
            <Header />
          </Grid>
          <Grid item xs={ 12 }>
            <Survey setParentAnswer={this.props.setParentAnswer}/>
          </Grid>
        </Grid>
      </div>
    )
  }
}

export default withStyles(styles)(Questions);