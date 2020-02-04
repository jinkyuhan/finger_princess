import React from 'react';
import { AppBar, Container,Toolbar, Typography} from '@material-ui/core';
const Header = () => {
    return (
        <div className="Header">
            <Container maxwidth = "lg">
                <AppBar color= "secondary">
                    <Toolbar variant="dense">
                        {/* <IconButton edge="start" color="inherit" aria-label="menu">
                            <MenuIcon />
                        </IconButton> */}
                        <Typography variant="h6" color="inherit">
                            견적 상담
                        </Typography>
                    </Toolbar>
                </AppBar>
            </Container>
        </div>
    );
};

export default Header;