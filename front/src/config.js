const serverConfig ={
    SERVERIP:"http://35.200.9.121",
    SERVERPORT:8000,
    getBASEURL:function(){
        return `${this.SERVERIP}:${this.SERVERPORT}`;
    }
}

module.exports=serverConfig;