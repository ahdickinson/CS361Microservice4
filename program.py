import os
import time

PIPELINE = "pipeline.txt"               # enter pipeline location + file extension
ACCDIR = "accounts"                     # enter directory location
SLEEP_INTERVAL = 0.1                    # replace with number of seconds program should wait between checks
os.makedirs(ACCDIR, exist_ok=True)      # not raising error if account directory exists



# functions, trying to split up to make modifying easier



# easy writing

def write_response(message: str):
    with open(PIPELINE, "w") as file:
        file.write(message + "\n")



# load stored account data

def load_accdata(username: str):
    userdata_file = os.path.join(ACCDIR, username, "userdata.txt")
    if not os.path.exists(userdata_file):
        return None, None
    with open(userdata_file, "r") as file:
        lines = file.read().strip().split("|")
        return lines[0], lines[1]



# create account

def create_account(username: str, password: str):
    path = os.path.join(ACCDIR, username)
    if not os.path.exists(path):
        os.makedirs(path)
        userdata_file = os.path.join(path, "userdata.txt")
        with open(userdata_file, "w") as f:
            f.write(f"{username}|{password}")
        write_response(f"OK : Account '{username}' created at {path}")
    else:
        write_response(f"ERROR : Account '{username}' already exists")



# find account

def find_account(username: str):
    path = os.path.join(ACCDIR, username)
    if os.path.exists(path):
        write_response(f"OK : Account found at {path}")
    else:
        write_response(f"ERROR : Account '{username}' not found")



# login

def login(username: str, password: str):
    path = os.path.join(ACCDIR, username)
    if not os.path.exists(path):
        write_response(f"ERROR : Account '{username}' does not exist")
        return
    stored_user, stored_pass = load_accdata(username)
    if stored_pass != password:
        write_response(f"ERROR : Incorrect password for '{username}'")
        return
    write_response(f"OK : Login successful for '{username}'")



# parse commands

def parse_command(line: str):
    if line.startswith("CREATE ACCOUNT : "):
        payload = line.split("CREATE ACCOUNT : ")[1]
        username, password = payload.split("|", 1)
        create_account(username.strip(), password.strip())
    elif line.startswith("FIND ACCOUNT : "):
        username = line.split("FIND ACCOUNT : ")[1].strip()
        find_account(username)
    elif line.startswith("LOGIN : "):
        payload = line.split("LOGIN : ")[1]
        username, password = payload.split("|", 1)
        login(username.strip(), password.strip())
    elif line.startswith(("ERROR : ", "OK : ")):
        return
    else:
        write_response("ERROR : Unknown command '{line}'")



# easy reading

def read_commands():
    with open(PIPELINE, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]




# main

def main():
    while True:
        commands = read_commands()
        for command in commands:
            parse_command(command)
        time.sleep(SLEEP_INTERVAL)


if __name__ == "__main__": main()