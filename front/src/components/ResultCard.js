import React from 'react';
import {
    Card,
    CardMedia,
    CardContent,
    Typography,
    Link
} from '@material-ui/core'

class ResultCard extends React.Component {

    constructor(props) {
        super(props)
        this.item = props.laptop
    }

    render() {
        return (
            <dir className="ResultCard">
                <Card
                    style={{
                        maxWidth: 345
                    }}>
                    <CardMedia
                        image={this.item.img}
                        title="#"
                        style={{
                            height: 140,
                            width:140
                        }} />
                    <CardContent>
                        <Typography gutterBottom variant="h5" component="h2">
                            <Link href={this.item.url}>{this.item.name}</Link>
                        </Typography>
                        <Typography variant="body2" color="textSecondary" component="p">
                            추천하는 노트북의 id 는 {String(this.item.id)} 입니다.<br />
                            추천하는 노트북의 요구 램은 {String(this.item.ram)} 입니다.<br />
                        </Typography>
                    </CardContent>
                </Card>
            </dir>
        )
    }
}

export default ResultCard