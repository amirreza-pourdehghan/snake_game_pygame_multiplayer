import socket, json


class Network:

    def __init__(self, host, port):
        self.port = port
        self.host = host
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s = s
        self.data = {}

    def start(self):
        self.s.connect((self.host, self.port))
        data = self.s.recv(4096).decode('ascii')
        self.data = json.loads(data)
        with open('config.json', 'w') as f:
            f.write(data)

    def send_data(self, keys):
        message = 'snake_' + str(self.data['id']) + '_'
        if len(keys) == 0:
            message = message + 'no_key'
        else:
            message = message + keys[0]

        data = {
            'keys': [message],
            'dead': False
        }

        self.s.sendall(json.dumps(data).encode('ascii'))

    def get_data(self):
        data = self.s.recv(4096).decode('ascii')
        data = data.replace("'", '"')

        return json.loads(data)