<img src="Python Security program.JPG" alt="Security python IMG" style="width: 150px; height: 150; border-radius: 50%; object-fit: cover;">


# SSH Kicker
SSH KICKER is a Python script designed to help you manage SSH sessions on your system. It allows you to perform tasks such as checking if SSH is enabled, performing an nslookup, and kicking users off the computer by terminating their SSH sessions.

## Features

- Check if SSH is enabled on the system.
- Perform an nslookup to query DNS information.
- Terminate SSH sessions associated with specific IP addresses.
- Ability to stop the SSH service if desired.

## Requirements

- Python 3.x
- Linux Operating System
- Mac Operating System

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/WilSegale/SSH_Kicker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd SSH_Kicker
    ```

3. Run the setup script:

    ```bash
    python kickUserSetup.py
    ```
4. Run the python file for linux
    ```bash     
    python3 LinuxKick.py
    ```

5. Run the python file for MacOS
    ```bash
    python3 MacOSKick.py
    ```
## Usage
1. Run the script: `python kickUserSetup.py` 
2. Follow the prompts to select an action.
3. Depending on your choice, provide necessary inputs such as domain name or IP address.

## Contributing

Contributions are welcome! If you have any ideas for improvement or find any issues, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
