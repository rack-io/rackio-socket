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

RackioSocket(app)

app.run(8028)
```

## Swagger UI

After running your application it will serve the socket through the *5005* port.

```
ws://localhost:5005
```
