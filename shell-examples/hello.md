Start Uvicorn with the command line
$ uvicorn hello:app --reload

Test /hi in the browser
http://localhost:8000/hi

Test /hi with Requests
>>> import requests
>>> r = requests.get("http://localhost:8000/hi")
>>> r.json()
'Hello? World?'

Test /hi with HTTPX, which is almost identical to Requests
>>> import httpx
>>> r = httpx.get("http://localhost:8000/hi")
>>> r.json()
'Hello? World?'

Test /hi with HTTPie
$ http localhost:8000/hi
HTTP/1.1 200 OK
content-length: 15
content-type: application/json
date: Thu, 30 Jun 2022 07:38:27 GMT
server: uvicorn
"Hello? World?"
Use the -b argument in Example 3-8 to skip the response headers and print only the
body.

Test /hi with HTTPie, printing only the response body
$ http -b localhost:8000/hi
"Hello? World?"

Test /hi with HTTPie and get everything
$ http -v localhost:8000/hi

GET /hi HTTP/1.1
Accept: /
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: localhost:8000
User-Agent: HTTPie/3.2.1

HTTP/1.1 200 OK
content-length: 15
content-type: application/json
date: Thu, 30 Jun 2022 08:05:06 GMT
server: uvicorn
"Hello? World?"

An HTTP request
GET /hi HTTP/1.1
Accept: /
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: localhost:8000
User-Agent: HTTPie/3.2.1
This request contains the following:
• The verb (GET) and path (/hi)
• Any query parameters (text after any ? in this case, none)
• Other HTTP headers
• No request body content
FastAPI unsquirrels these into handy definitions:
Header
The HTTP headers
Path
The URL
Query
The query parameters (after the ? at the end of the URL)
Body
The HTTP body

Test /hi/Mom in the browser
localhost:8000/hi/Mom

Test /hi/Mom with HTTPie
$ http localhost:8000/hi/Mom
HTTP/1.1 200 OK
content-length: 13
content-type: application/json
date: Thu, 30 Jun 2022 08:09:02 GMT
server: uvicorn
"Hello? Mom?"

Test /hi/Mom with Requests
>>> import requests
>>> r = requests.get("http://localhost:8000/hi/Mom")
>>> r.json()
'Hello? Mom?'


[]: # (======= second part ==================)

Test /hi/Mom in the browser
localhost:8000/hi/Mom

Test /hi/Mom with HTTPie
$ http localhost:8000/hi/Mom
HTTP/1.1 200 OK
content-length: 13
content-type: application/json
date: Thu, 30 Jun 2022 08:09:02 GMT
server: uvicorn
"Hello? Mom?"

Test /hi/Mom with Requests
>>> import requests
>>> r = requests.get("http://localhost:8000/hi/Mom")
>>> r.json()
'Hello? Mom?'

[]: # (======= third part ==================)

Test with your browser
localhost:8000/hi?who=Mom

with HTTPie

$ http -b localhost:8000/hi?who=Mom
"Hello? Mom?"
In Example 3-18, you can call HTTPie with a query parameter argument (note the
==).

with HTTPie and params

$ http -b localhost:8000/hi who==Mom
"Hello? Mom?"
You can have more than one of these arguments for HTTPie, and it’s easier to type
these as space-separated arguments.

 show the same alternatives for Requests

>>> import requests
>>> r = requests.get("http://localhost:8000/hi?who=Mom")
>>> r.json()
'Hello? Mom?'

 with Requests and params

>>> import requests
>>> params = {"who": "Mom"}
>>> r = requests.get("http://localhost:8000/hi", params=params)
>>> r.json()
'Hello? Mom?'
