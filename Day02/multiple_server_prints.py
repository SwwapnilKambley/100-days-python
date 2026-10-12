statuses = ["running", "stopped", "running", "degraded", "stopped"]
running = 0 
for index in statuses:
    if index == "running":
        print("✅ Server is healthy")
        running += 1
    elif index == "stopped":
        print("❌ Server is down")
    elif index == "degraded":
        print("⚠️ Server needs attention")


print()
print(f"Running servers = {running}")