## A simple physical sensor device simulator with using WebSocket communication protocol.

- Connects to a WebSocket server
- If a get_temp request comes, then creates a random temperature result
- And sends the result with the "house/sensor_result" header back
- This simulator is running on a free tier amazon server(ec2-18-195-119-211.eu-central-1.compute.amazonaws.com) 
- And you can send WebSocket requests to "house/sensor" channel to get a result

- Usage:
    ~~~~
    git clone https://github.com/BurakDmb/WebSocket-Basic-Device-Simulator.git
    cd WebSocket-Basic_Device-Simulator
    pip3 install paho-mqtt
    python3 main.py
    ~~~~

- Also you can use this command to use this script in background
  ~~~~
  nohup python3 main.py &
  ~~~~
- And you can kill using:
  ~~~~
  ps -aux | grep main.py
  kill PID(the pid of main.py process)
  ~~~~