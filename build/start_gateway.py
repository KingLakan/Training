import subprocess

def StartGateway():
    """Start Veristand silent gateway

    Returns:
        bool: true if Server running
    """
    Veristand_gateway_path = (r"c:\Program Files (x86)\National Instruments" 
                              r"\VeriStand 2020\veristand-server.exe")
    output = subprocess.check_output([Veristand_gateway_path,'start'])
    status_output = (output.decode(('UTF-8')).split()[0] + " " +
                     output.decode(('UTF-8')).split()[1])
    print(status_output)
    if status_output == "Server running":
        return True
    else:
        pass#exit(1)

if __name__ == "__main__":
    StartGateway()
    print("Gateway Started")