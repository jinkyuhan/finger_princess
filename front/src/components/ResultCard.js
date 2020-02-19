import React from 'react';
import {
    Card,
    CardMedia,
    CardContent,
    Typography
} from '@material-ui/core'

class ResultCard extends React.Component {
    state = {
        laptop: {
            name:"",
            weight:"",
            cpu:"",
            gpu:"",
            ram:"",
            ssd:"",
            hdd:"",
            resolution:"",
            size:"",
            price:""
        }
    }

    render() {
        return (
            <dir className="ResultCard">
                <Card
                    style={ {
                        maxWidth: 345
                    } }>
                    <CardMedia
                        image="https://images.unsplash.com/photo-1504707748692-419802cf939d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1330&q=80"
                        title="#"
                        style={ {
                            height: 140
                        } } />
                    <CardContent>
                        <Typography gutterBottom variant="h5" component="h2">
                            {this.state.laptop.name}
                        </Typography>
                        <Typography variant="body2" color="textSecondary" component="p">
                            Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging
                            across all continents except Antarctica
                        </Typography>
                    </CardContent>
                </Card>
            </dir>
        )
    }
}

export default ResultCard