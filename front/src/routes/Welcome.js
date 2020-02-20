import React from 'react'
import { Grid } from '@material-ui/core'
// import '../App.css'
import WelcomeCard from '../components/WelcomeCard'

class Welcome extends React.Component {
    render() {
        return (
            <div className="Welcome">
                <Grid container spacing={3} className="wallpaper" style={{backgroundImage:`url("https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=693&q=80")`, backgroundPosition:'center'}}>
                    <Grid item xs={12} />
                    <Grid item xs={12} >
                        <h1 style={{ color: "white" }}>Hello world </h1>
                        <WelcomeCard/>
                    </Grid>
                    <Grid item xs={12} />
                </Grid>
            </div>
        )
    }
}




export default Welcome;