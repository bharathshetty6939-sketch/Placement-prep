tools=["Nmap", "Metasploit", "Wireshark"]
n=input("Enter the new tool name:")
tools.append(n)
index = int(input("Enter an index number between 0 and 3: "))
print(f"Tool at index {index} is: {tools[index]}")

# Loop through the list and print each tool
print("\nAll tools in the list:")
for tool in tools:
    print(tool)
