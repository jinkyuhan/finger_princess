import React from 'react';
import {
    Card,
    CardActions,
    CardContent,
    Button,
    //Grid,
    Typography
} from '@material-ui/core';
import "../App.css";
// const useStyles = makeStyles({
//   root: {
//     minWidth: 275,
//   },
//   bullet: {
//     display: 'inline-block',
//     margin: '0 2px',
//     transform: 'scale(0.8)',
//   },
//   title: {
//     fontSize: 14,
//   },
//   pos: {
//     marginBottom: 12,
//   },
// });

class WelcomeCard extends React.Component {
    // classes = useStyles();

    render() {
        return (
            <Card >
                <CardContent>
                    <Typography color="textSecondary" gutterBottom>
                        안녕
                    </Typography>
                    <Typography variant="h5" component="h2">
                        컴맹들아
                    </Typography>
                    <Typography color="textSecondary">
                        도와줄까
                     </Typography>

                    <Typography variant="body2" component="p">
                        ㅎㅎ
                    </Typography>
                </CardContent>
                <CardActions>
                    <Button size="small" color="primary" id="getin-button" href='#questions'>Learn More</Button>
                </CardActions>
            </Card>
        )
    };
}

export default WelcomeCard;