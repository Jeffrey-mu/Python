const http = require('http');
function  a(){
    console.log("dajiahao");
}
var server = new http.Server();
server.on('request',(req,res)=>{
    console.log(req.url);
    //设置应答头信息
    res.writeHead(200,{'Content-Type':'text/html'});
    res.write('hello we are family<br>');
    res.end('server already end\n');
});
//显示了三次这也证明了TCP的三次握手
server.on('connection',()=>{
    a();
});
server.on('close',()=>{
    console.log('server will close');
});
//关闭服务为了触发close事件
server.close();
server.listen(1000);
