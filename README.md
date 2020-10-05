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

## Swagger UI

After running your application it will serve the SocketIO through the *5005* port.

```javascript
var socket = io('http://localhost:5005');
```
