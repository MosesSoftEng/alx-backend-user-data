# :book: 0x01. Basic authentication.
## :page_with_curl: Topics Covered.
1. REST API Authentication Mechanisms.


# :computer: Tasks.
## [0. Simple-basic-API]()
### :page_with_curl: Task requirements.
Download and start your project from this archive.zip

In this archive, you will find a simple API with one model: User. Storage of these users is done via a serialization/deserialization in files.
#### Setup and start server

```
bob@dylan:~$ pip3 install -r requirements.txt
...
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Serving Flask app "app" (lazy loading)
...
bob@dylan:~$
```

#### Use the API (in another tab or in your browser)
```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/status HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 16
< Access-Control-Allow-Origin: *
< Server: Werkzeug/1.0.1 Python/3.7.5
< Date: Mon, 18 May 2020 20:29:21 GMT
< 
{"status":"OK"}
* Closing connection 0
bob@dylan:~$
```

### :wrench: Task setup.
```bash
# Download zip file to current directory.
curl -O https://intranet.alxswe.com/rltoken/2o4gAozNufil_KjoxKI5bA

# Install unzip package
apt install unzip

# Extract SimpleAPI content to current directory.
unzip -j ec2f874b061bd3a2915949f081f4f5f055104f20.zip SimpleAPI
cd SimpleAPI

pip3 install -r requirements.txt

API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

### :heavy_check_mark: Solution
> [:point_right: 0-async_generator.py](0-async_generator.py)


## [1. Error handler: Unauthorized](api/v1/app.py)
### :page_with_curl: Task requirements.
What the HTTP status code for a request unauthorized? 401 of course!

Edit api/v1/app.py:

*    Add a new error handler for this status code, the response must be:
    *    a JSON: {"error": "Unauthorized"}
    *    status code 401
    *    you must use jsonify from Flask

For testing this new error handler, add a new endpoint in api/v1/views/index.py:

*    Route: GET /api/v1/unauthorized
*    This endpoint must raise a 401 error by using abort - Custom Error Pages

By calling abort(401), the error handler for 401 will be executed.

In the first terminal:
```
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In a second terminal:
```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/unauthorized"
{
  "error": "Unauthorized"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/unauthorized" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/unauthorized HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 401 UNAUTHORIZED
< Content-Type: application/json
< Content-Length: 30
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sun, 24 Sep 2017 22:50:40 GMT
< 
{
  "error": "Unauthorized"
}
* Closing connection 0
bob@dylan:~$
```

### :wrench: Task setup.
```bash
# Start server.
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app

# Tests.
curl "http://0.0.0.0:5000/api/v1/unauthorized"
```

### :heavy_check_mark: Solution
> [:point_right: 1-async_comprehension.py](1-async_comprehension.py)


## [2. Error handler: Forbidden](api/v1/app.py)
### :page_with_curl: Task requirements.
What the HTTP status code for a request where the user is authenticate but not allowed to access to a resource? 403 of course!

Edit api/v1/app.py:

*    Add a new error handler for this status code, the response must be:
    *    a JSON: {"error": "Forbidden"}
    *    status code 403
    *    you must use jsonify from Flask

For testing this new error handler, add a new endpoint in api/v1/views/index.py:

*    Route: GET /api/v1/forbidden
*    This endpoint must raise a 403 error by using abort - Custom Error Pages

By calling abort(403), the error handler for 403 will be executed.

In the first terminal:
```
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In a second terminal:
```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/forbidden"
{
  "error": "Forbidden"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/forbidden" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/forbidden HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 403 FORBIDDEN
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sun, 24 Sep 2017 22:54:22 GMT
< 
{
  "error": "Forbidden"
}
* Closing connection 0
bob@dylan:~$
```

### :wrench: Task setup.
```bash
# Start server.
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app

# Tests.
curl "http://0.0.0.0:5000/api/v1/forbidden"
```

### :heavy_check_mark: Solution
> [:point_right: 2-measure_runtime.py](2-measure_runtime.py)

# :man: Author and Credits.
This project was done by [SE. Moses Mwangi](https://github.com/MosesSoftEng). Feel free to get intouch with me;

:iphone: WhatsApp [+254115227963](https://wa.me/254115227963)

:email: Email [moses.soft.eng@gmail.com](mailto:moses.soft.eng@gmail.com)

:thumbsup: A lot of thanks to [ALX-Africa Software Engineering](https://www.alxafrica.com/) program for the project requirements.
