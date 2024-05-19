import asyncio
from bleak import BleakClient
import platform
import argparse

UART_SERVICE_UUID = "0000ff70-0000-1000-8000-00805f9b34fb"
UART_CHARACTERISTIC_UUID = "0000ff71-0000-1000-8000-00805f9b34fb"


class BLEUARTBridge:
    def __init__(self, address):
        self.address = address
        self.client = BleakClient(address)

    async def connect(self):
        await self.client.connect(timeout=60)
        print(f"Connected to {self.address}")

    async def disconnect(self):
        await self.client.disconnect()
        print(f"Disconnected from {self.address}")

    async def write_data(self, data):
        await self.client.write_gatt_char(UART_CHARACTERISTIC_UUID, data, response=True)
        # print(f"Sent: {data}")

    async def notification_handler(self, sender, data):
        print(data.decode(), end="")

    async def start_notifications(self):
        await self.client.start_notify(UART_CHARACTERISTIC_UUID, self.notification_handler)
        print("Started notifications")

    async def stop_notifications(self):
        await self.client.stop_notify(UART_CHARACTERISTIC_UUID)
        print("Stopped notifications")


async def user_input_handler(bridge):
    while True:
        user_input = await asyncio.to_thread(input, "")
        if user_input.lower() == "exit":
            break
        await bridge.write_data(user_input.encode())


async def main(address):
    bridge = BLEUARTBridge(address)
    await bridge.connect()

    try:
        await bridge.start_notifications()

        await user_input_handler(bridge)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await bridge.stop_notifications()
        await bridge.disconnect()


def detect_os():
    os_name = platform.system()
    if os_name == "Darwin":
        return "macOS"
    elif os_name == "Linux":
        return "Linux"
    else:
        return "Unknown"


if __name__ == "__main__":
    address = "D8:47:18:36:DA:F6"
    if detect_os() == "macOS":
        address = "5DC6A5C3-9CDC-644B-8F7D-F3771B027198"

    parser = argparse.ArgumentParser(description="BLE UART Bridge")
    parser.add_argument('--address', type=str, default=address,
                        help='BLE device address (default: 00:00:00:00:00:00)')
    args = parser.parse_args()
    asyncio.run(main(args.address))
