import socket  # importing library

target = input('IP address to scan: ')
portrange = input('Enter the Range  : ')

lower_value = int(portrange.split('-')[0]) # you can rather take lower_ip and higher_ip for ranges
value_higher = int(portrange.split('-')[1])

print('Scanning host ', target, 'from port',lower_value, 'to port', value_higher)

for port in range(lower_value, value_higher):
    s = socket.socket( ) # Blank for ipv4 and TCP

    status = s.connect_ex((target, port))
    if(status == 0):
        print('*** Port',port,'- IS OPEN ***')
    else:
        print('Port',port,'-  IS CLOSED')
    s.close()