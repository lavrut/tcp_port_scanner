# tcp_port_scanner

This implementation takes a host and a list of ports as input and returns the status of each port (open or closed). The user can input the host to be scanned and the list of ports separated by commas. The function scan_ports loops through the list of ports and uses a socket to check the status of each port. If the connection to the port is successful, the port is considered open, otherwise it is considered closed.

if __name__ == '__main__': is a common idiom used in Python to check if a script is being executed as the main program or if it is being imported as a module into another program.

When a Python script is executed, the __name__ attribute of the script is set to '__main__'. If the script is imported as a module into another program, the __name__ attribute is set to the name of the module. By using the if __name__ == '__main__': check, you can ensure that code inside this block will only be executed when the script is run as the main program and not when it is imported as a module into another program.

For example, in the code snippet you provided, the scan_ports function can be reused in other programs by importing the script as a module. When this script is imported as a module, the code inside if __name__ == '__main__': will not be executed, and the function can be called directly. However, if the script is executed as the main program, the code inside the if block will be executed, allowing the user to input the host and port list to be scanned.
