detect_threat=["Trojan", "Adware", "Spyware", "Rootkit", "Ransomware"]
detect_threat.sort()
print("detected threats are:",detect_threat)
detect_threat.remove("Adware")
print("After Removing Adware",detect_threat)
detect_threat.pop()
print("Neutralizing ...:",detect_threat)
print("remaing threats are:")
print(detect_threat)