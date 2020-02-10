import React from 'react';
import { AppBar, Container, Toolbar, Typography } from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles';

const styles = {
    root: {
        fontFamily: ''
    },
    appbar: {
        alignItems: 'center'
    }
};
class Header extends React.Component {

    render() {
        const { classes } = this.props;
        return (
            <div className={classes.root}>
                <Container maxwidth="lg">
                    <AppBar color="secondary" className={classes.appbar}>
                        <Toolbar variant="dense">
                            {/* <IconButton edge="start" color="inherit" aria-label="menu">
                            <MenuIcon />
                        </IconButton> */}
                            <Typography variant="h6" color="inherit">
                                Finger Princess
                            </Typography>
                        </Toolbar>
                    </AppBar>
                </Container>
            </div>
        )
    };
};

export default withStyles(styles)(Header);