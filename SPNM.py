import pandas as pd
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
from getpass import getpass
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Prompt the user to select the Excel file
root = Tk()
root.withdraw()
file_path = askopenfilename(title = "Select Excel file")

# Read the Excel sheet into a pandas DataFrame
df = pd.read_excel(file_path)

# Prompt the user for their username and password
username = input("Enter your username: ")
password = getpass("Enter your password: ")

# Create a dictionary to store the commands for each IP address
ip_commands_dict = {}

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Get the IP address of the switch from the first column
    ip = row[0]
    
    # Get the commands to run from the rest of the row
    commands = list(row[1:])
    
    # Filter out empty commands
    commands = [str(command) for command in commands if not pd.isna(command)]
    
    # Check if the IP address is already in the dictionary
    if ip in ip_commands_dict:
        # If it is, append the commands to the list of commands
        ip_commands_dict[ip].extend(commands)
    else:
        # If it's not, create a new entry for the IP address and its commands
        ip_commands_dict[ip] = commands
        
# Create a file to save the output to
output_file = open("output.txt", "w")

# Loop through each IP address and its commands in the dictionary
for ip, commands in ip_commands_dict.items():
    # Create a dictionary of parameters for Netmiko
    netmiko_params = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': username,
        'password': password
    }
    
    try:
        # Connect to the switch using Netmiko
        with ConnectHandler(**netmiko_params) as net_connect:
            # Send the commands and save the output to the file and print it to the terminal
            output = net_connect.send_config_set(commands, exit_config_mode=False)
            output_file.write(f"Output for {ip}:\n")
            output_file.write(output)
            output_file.write("\n")
            print(f"Output for {ip}:")
            print(output)
            print()
            
    except NetmikoTimeoutException:
        # If there's a timeout exception, print an error message to the terminal and write it to the file
        output_file.write(f"Timeout error connecting to {ip}\n")
        print(f"Timeout error connecting to {ip}")
        
    except NetmikoAuthenticationException:
        # If there's an authentication exception, print an error message to the terminal and write it to the file
        output_file.write(f"Authentication error connecting to {ip}\n")
        print(f"Authentication error connecting to {ip}")
        
    except Exception as e:
        # If there's any other exception, print the error message to the terminal and write it to the file
        output_file.write(f"Error connecting to {ip}: {str(e)}\n")
        print(f"Error connecting to {ip}: {str(e)}")
        
# Close the file
output_file.close()
