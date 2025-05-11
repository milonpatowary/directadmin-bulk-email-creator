import requests
import csv
import sys

# --- Configuration ---
directadmin_host = "yourdirectadminurl.com:2222"
directadmin_username = "yourusername"  # Replace with your DirectAdmin username
directadmin_password = "yourpass"  # Replace with your DirectAdmin password
csv_file_path = "email_accounts2.csv"  # Replace with your CSV file path

# --- Function to create a DirectAdmin POP account ---
def create_pop_account(domain, user, password, quota="0"):
    url = f"https://{directadmin_host}/CMD_API_POP"
    auth = (directadmin_username, directadmin_password)
    data = {
        "action": "create",
        "domain": domain,
        "user": user,
        "passwd": password,
        "passwd2": password,
        "quota": quota
    }
    response = None # Initialize response
    try:
        response = requests.post(url, auth=auth, data=data)
        response.raise_for_status()
        print(f"Successfully created: {user}@{domain} - Response: {response.text}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error creating {user}@{domain}: {e}")
        if response:
          print(f"Response text: {response.text}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

# --- Read email accounts from CSV and create them ---
def create_accounts_from_csv(file_path):
    try:
        with open(file_path, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            if not all(k in reader.fieldnames for k in ('domain', 'user', 'password')):
                print("Error: CSV file must contain 'domain', 'user', and 'password' columns.")
                sys.exit(1)

            success_count = 0
            failure_count = 0
            for row in reader:
                domain = row['domain']
                user = row['user']
                password = row['password']
                if create_pop_account(domain, user, password):
                    success_count += 1
                else:
                    failure_count += 1
            print(f"Successfully created {success_count} accounts. Failed to create {failure_count} accounts.")

    except FileNotFoundError:
        print(f"Error: CSV file not found at {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    create_accounts_from_csv(csv_file_path)