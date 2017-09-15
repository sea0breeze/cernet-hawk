## 1. 

GET /search/{searchStr}

ok

``json
{
    "status" : "ok",
    "data" : [
        "8.8.8.8",
        "114.114.114.114"
    ]
}
``
error

``json
{
    "status" : "error",
    "msg" : "error msg"
}
``

GET /detail/ip

ok

``json
{
    "status" : "ok",
    "data" : {
        "ip" : "8.8.8.8",
        "port" : 80,
        "name" : "http",
        "banner" : {
            "app" : "jquery"
        }
    }
}
``

error

``json
{
    "status" : "error",
    "msg" : "error msg"
}
``
