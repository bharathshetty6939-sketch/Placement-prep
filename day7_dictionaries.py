server_info={"ip": "192.168.1.1","status": "Active","threat_level": "Low"}
print("Server_info:",server_info)
print("Changing status to.....")
server_info["status"]="Maintenance"
print(server_info["status"])
print("Adding new value to dictionaries")
server_info["up time"]="99.9%"
print("Updated server register")
print(server_info)
