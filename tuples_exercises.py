

host_port = (
    "127.0.0.1", 3000
)

print(host_port)

print(type(host_port))

print(host_port[0])
print(host_port[1])

red_rgb = (
    255, 0, 0
)

print(red_rgb[0])

single_value = 44
print(type(single_value))
single_value = ()
print(type(single_value))

print(host_port[:1])

print(host_port[-2:])


#host_port[0] = 23
#print(host_port)

service_endpoint = ("auth.server.dev.local",[80])
print(f"host {service_endpoint[0]} port {service_endpoint[1]}")
#service_endpoint[2] = 44
#print(service_endpoint)

x = list(service_endpoint)
x[1] = "443"
service_endpoint = tuple(x)
print(service_endpoint)