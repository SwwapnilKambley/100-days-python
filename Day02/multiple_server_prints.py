server_names = ["web-01", "web-02", "db-01"]
regions = ["us-east1", "us-east1", "us-west2"]
statuses = ["running", "stopped", "running"]


for i in range(len(server_names)):
    print(f"Server {server_names[i]} in {regions[i]} is {statuses[i]}.")

print(f"Total servers checked: {len(server_names)}")