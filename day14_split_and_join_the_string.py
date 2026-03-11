def get_String():
    n="This is a string"
    words=n.split(" ")
    final_string="-".join(words)
    return final_string
print("The final string is:", get_String())
