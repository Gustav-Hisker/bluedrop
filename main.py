from bless import BlessServer
import asyncio

from bless.backends.characteristic import BlessGATTCharacteristic

server = BlessServer(name="Test-BLE-Server", loop=asyncio.get_event_loop())
server.read_request_func = lambda characteristic, **kwargs: print(characteristic)
server.write_request_func = lambda characteristic, value, **kwargs: print(characteristic, value)

await server.start()