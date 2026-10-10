# DATA TYPES

# String
server_name = "web-01"
# Integer
port = 8080
# Boolean
is_running = True
# Float
cpu_usage = 75.5

# Print the values and their data types
print(server_name, type(server_name))
print(port, type(port))
print(is_running, type(is_running))
print(cpu_usage, type(cpu_usage))


# List of servers   
servers = ["server-01", "server-02", "db-01"]

print(servers)

print(len(servers))

print(servers[0])  # Accessing the first server


# F-strings (formatted strings)
print(f"Server Name: {server_name}, Port: {port}, Running: {is_running}, CPU Usage: {cpu_usage}%")