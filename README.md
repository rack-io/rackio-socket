# rackio-socket
A Rackio extension to add a SocketIO Server to Rackio

## Installation

```
pip install RackioSocket
```

## Usage

```python
from rackio import Rackio
from rackio_socket import RackioSocket

app = Rackio()

RackioSocket(app, 5005)

app.run(8028)
```

## SocketIO Client

After running your application it will serve the SocketIO through the *5005* port.

```javascript
var socket = io('http://localhost:5005');
```

## Adding new events to your applications

You can add your custom events using the decorator pattern.

```python
rs = RackioSocket()

@rs.event
def custom(sid):
    print("custom event " , sid)
    rs.emit("response", {"message": "this is the custom response"})


@rs.on("another custom")
def another_event(sid, data):

    response = processing(data)

    rs.emit('response', response)

```