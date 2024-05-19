# BLE UART Bridge

BLE UART Bridge is a Python utility that uses the `bleak` library to interact with BLE devices as a UART bridge via the GATT characteristic `0xff71`.

## Description

This project allows you to send data to a BLE device and receive responses from it in real-time using the GATT characteristic `0xff71`. The utility supports asynchronous handling of data input and device notifications.

## Installation

1. Ensure you have Python 3.7 or higher installed.
2. Install the required dependencies:
    ```sh
    pip install bleak
    ```

## Usage

1. Run the `main.py` script with the BLE device address:
    ```sh
    python main.py --address AA:BB:CC:DD:EE:FF
    ```
    Replace `AA:BB:CC:DD:EE:FF` with your actual BLE device address. If the address is not provided, the default address specified in the script will be used.

2. Enter the data you wish to send in the console. The device will receive the data, and responses from the device will be displayed in the console.

### Usage Examples

- With the device address specified:
    ```sh
    python main.py --address AA:BB:CC:DD:EE:FF
    ```
- Without specifying the address (default address will be used):
    ```sh
    python main.py
    ```
