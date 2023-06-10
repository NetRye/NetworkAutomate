# NetworkAutomate
A Script to Automate Change Management of Network Devices such as Routers and Switches

# Network Device Configuration Script

This Python script is designed to automate the configuration of network devices, specifically Cisco IOS devices, using the Netmiko library and a provided Excel file containing the device IP addresses and corresponding configuration commands.

## Prerequisites

Before running this script, make sure you have the following:

1. Python: Ensure that Python is installed on your system. You can download Python from the official Python website (https://www.python.org) and follow the installation instructions.

2. Required Packages: Install the necessary Python packages by running the following commands:

```
pip install pandas
pip install netmiko
```

3. Example Excel File: An example Excel file named "devices-config-examples.xlsx" is included in the repository to help you understand the required format. You can find it in the same location where you found this script. You can use this file as a template and modify it according to your network devices and configuration needs.

## Usage

1. Import Libraries: The script begins by importing the required libraries. Ensure that you have installed the necessary packages, including `pandas`, `netmiko`, `getpass`, and `tkinter`.

2. Select Excel File: The script prompts you to select the Excel file that contains the device information and configuration commands. A file dialog window will appear, allowing you to browse and select the desired file.

3. Read Excel Data: The script uses the `pandas` library to read the selected Excel sheet into a DataFrame, making it easier to manipulate and access the data.

4. User Authentication: Enter your username and password when prompted by the script. This information will be used to authenticate and establish connections with the network devices.

5. Configure Commands: The script extracts the IP addresses and configuration commands from the DataFrame and stores them in a dictionary. It filters out any empty commands or cells in the Excel sheet.

6. Connect to Devices: The script iterates over each IP address and its corresponding commands. It uses the `Netmiko` library to establish a connection with each network device using SSH.

7. Execute Commands: For each device, the script sends the configuration commands and saves the output to a file named "output.txt". The output is also displayed in the terminal window.

8. Handle Exceptions: The script includes error handling to manage potential exceptions, such as timeouts or authentication errors when connecting to devices. Any encountered errors will be recorded in the output file and displayed in the terminal.

## Output

The script generates an output file named "output.txt" in the same directory as the script. The file contains the output of each executed command for every network device, as well as any encountered errors during the process.

Additionally, the script prints the output and error messages to the terminal in real-time, allowing you to monitor the progress and identify any issues.

It's important to review the output file and terminal messages to ensure that the configuration commands were applied successfully and to address any errors that may have occurred.

## Disclaimer

This script is provided as-is and without any warranty. It is your responsibility to review and test the script before using it in a production environment. The author assumes no liability for any damages or issues arising from the use of this script.

Please use this script responsibly and ensure that you have appropriate permissions and authorization to access and modify network devices.

## Example Excel File

To help you get started, an example Excel file named "devices-config-Example.xlsx" is included in the repository. It demonstrates the required format for the Excel file, with the first column containing the IP addresses of the network devices and subsequent columns containing the configuration commands.

Feel free to modify this example file or create your own Excel file following the same format to suit your network devices and configuration requirements.

## Conclusion

This network device configuration script automates the process of configuring Cisco Routers and Switches although it can be easily used for any vendor. 
