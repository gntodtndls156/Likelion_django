var http = require("http");

http.createServer(function(request, response) {
    response.writeHead(200, {'content-Type' : 'text/plain; charset=utf8'});
    response.end("hello world 할로");
}).listen(8080);

console.log("server running at http://127.0.0.1:8080");