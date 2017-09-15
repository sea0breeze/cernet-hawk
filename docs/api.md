## 1. 

GET /search/{searchStr}

e.g. 
``
GET /search/ip=444
``

ok

``json
{
    "status" : "ok",
    "data" : [
        {
            "ip" : "8.8.8.8",
            "addr" : "Beijin",
            "services" : ["ssh/22", "http/80"],
            "domain" : "xxx.com",
            "os" : "Ubuntu"
        }, {
            "ip": "114.114.114.114"
            "addr" : "Shanghai",
            "services" : ["stmp/25", "https/443"],
            "domain" : "hxax.com",
            "os" : "Windows"
        }
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

GET /detail/{ip}

ok

``json
{
    "status" : "ok",
    "data" : [
        {
            "port" : 80,
            "name" : "http",
            "banner" : {
                "app" : "jquery",
                "title" : "simple http"
            }
        }, {
            "port" : 21,
            "name" : "ftp",
            "banner" : {
                "version" : "vsftp"
            }
        },
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
