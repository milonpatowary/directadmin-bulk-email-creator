# DirectAdmin Bulk Email Creator

This Python script (create_emails.py) automates the creation of email accounts on a DirectAdmin server using the DirectAdmin API. It reads email account data from a CSV file and creates the accounts in bulk.

## Features

Reads email account information (domain, username, password) from a CSV file.
Uses the DirectAdmin CMD_API_POP to create email accounts.
Handles errors during account creation.
Provides a summary of successful and failed account creations.

## Prerequisites

Python 3.x
requests library: Install using pip install requests
A DirectAdmin server with the CMD_API_POP enabled.
A CSV file containing the email account data.

## Installation

1.  Clone the repository:
    bash
    git clone <repository_url>
    cd directadmin-bulk-email-creator
    

2.  Install the required Python library:
    bash
    pip install -r requirements.txt
    

## Usage

1.  Prepare your CSV file (email_accounts.csv):
    The CSV file should contain the following columns:
        domain: The domain name for the email account.
        user: The username (local part) of the email account.
        password: The password for the email account.
    Example:
        csv
        domain,user,password
        domain1.com,user1,Pass1!
        domain2.com,user2,Pass2@
        domain3.com,user3,Pass3#
        

2.  Configure the script:
    Open create_emails.py and modify the following variables in the 
	
	# --- Configuration --- section:
        directadmin_host: The hostname or IP address of your DirectAdmin server (e.g., "yourdirectadminurl:2222").
        directadmin_username: Your DirectAdmin administrator username.
        directadmin_password: Your DirectAdmin administrator password.
        csv_file_path: The path to your CSV file (e.g., "email_accounts.csv" or "data/email_accounts.csv").

3.  Run the script:
    bash
    python create_emails.py
    

    The script will read the CSV file, create the email accounts on the DirectAdmin server, and display the results.

## Important Notes

Security: Store your DirectAdmin credentials securely. Avoid hardcoding them directly in the script if possible (consider using environment variables).
Error Handling: The script includes basic error handling, but you should monitor the output for any errors during account creation.

DirectAdmin API: Ensure that the CMD_API_POP is enabled on your DirectAdmin server and that the user you are using has the necessary permissions.

Password Complexity: Ensure that the passwords in your CSV file meet the password complexity requirements of your DirectAdmin server.


## Author

Milon Patowary