led1=Pin(18, Pin.OUT)
led2=Pin(19, Pin.OUT)
led3=Pin(21, Pin.OUT)
led4=Pin(5, Pin.OUT)

def web_page():
  html = """<html><head> <title>ESP32</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #127131; border: none;
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  </style></head><body> <h1>ESP Light Controlling</h1>
  <p><a href="/?led1"><button class="button">LED 1</button></a></p>
  <p><a href="/?led2"><button class="button">LED 2</button></a></p>
  <p><a href="/?led3"><button class="button">LED 3</button></a></p>
  <p><a href="/?led4"><button class="button">LED 4</button></a></p></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  led_1 = request.find('/?led1')
  led_2 = request.find('/?led2')
  led_3 = request.find('/?led3')
  led_4 = request.find('/?led4')
  if led_1 == 6:
    led1.value(not led1.value())
  if led_2 == 6:
    led2.value(not led2.value())
  if led_3 == 6:
    led3.value(not led3.value())
  if led_4 == 6:
    led4.value(not led4.value())
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
