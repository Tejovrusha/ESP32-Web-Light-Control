# ESP32 Web Light Control

A simple IoT project that uses an **ESP32** running **MicroPython** to host a web server for controlling multiple LEDs through a web browser over Wi-Fi.

## Features

-  Built-in HTTP web server
-  Wi-Fi connectivity
-  Control four LEDs from any device on the same network
-  Toggle LEDs ON/OFF with a single click
-  Written entirely in MicroPython
-  Simple HTML/CSS web interface

---

## Hardware Requirements

- ESP32 Development Board
- 4 × LEDs
- 4 × 220Ω Resistors
- Breadboard
- Jumper Wires
- USB Cable

---

## Software Requirements

- MicroPython Firmware for ESP32
- Thonny IDE (or any MicroPython-compatible IDE)

---

## GPIO Pin Configuration

| LED | GPIO Pin |
|-----|----------|
| LED 1 | GPIO 18 |
| LED 2 | GPIO 19 |
| LED 3 | GPIO 21 |
| LED 4 | GPIO 5 |

---

## Project Structure

```
ESP32-Webserver-LED-Control/
│
├── boot.py        # Connects ESP32 to Wi-Fi
└── code.py        # Runs the web server and controls LEDs
```

---

## How It Works

1. The ESP32 connects to the specified Wi-Fi network using `boot.py`.
2. An HTTP web server starts on port **80**.
3. Visiting the ESP32's IP address in a web browser displays a control page.
4. Clicking a button sends an HTTP request.
5. The ESP32 detects the request and toggles the corresponding LED.

---

## Setup

### 1. Flash MicroPython

Install the latest MicroPython firmware on your ESP32.

### 2. Upload the Files

Upload the following files to the ESP32:

- `boot.py`
- `main.py`

### 3. Configure Wi-Fi

Open `boot.py` and replace the Wi-Fi credentials with your own:

```python
ssid = "Your_WiFi_Name"
password = "Your_WiFi_Password"
```

### 4. Run the Project

Restart the ESP32.

The Serial Console will display something similar to:

```
Connection successful
('192.168.1.105', '255.255.255.0', '192.168.1.1', '8.8.8.8')
```

Open the displayed IP address in your browser:

```
http://192.168.1.105
```

---

## Web Interface

The webpage contains four buttons:

- LED 1
- LED 2
- LED 3
- LED 4

Each button toggles the corresponding LED connected to the ESP32.

---

## Example Circuit

| LED | ESP32 GPIO |
|------|------------|
| LED 1 | GPIO 18 |
| LED 2 | GPIO 19 |
| LED 3 | GPIO 21 |
| LED 4 | GPIO 5 |

Connect each LED in series with a **220Ω resistor** to the corresponding GPIO pin.

---

## Future Improvements

- Add ON/OFF status indicators
- Individual ON and OFF buttons
- Responsive UI with Bootstrap
- Password-protected web interface
- Mobile-friendly dashboard
- Relay module support for controlling AC appliances
- MQTT integration
- Home Assistant compatibility


---

Developed as a MicroPython IoT project using the ESP32 to demonstrate browser-based hardware control over Wi-Fi.
