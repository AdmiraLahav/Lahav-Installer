import json
import hashlib
import os
import secrets

CREDS_FILE = "creds.json"

def load_creds():
    if not os.path.exists(CREDS_FILE):
        return {"users": {}}
    with open(CREDS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_creds(data):
    with open(CREDS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def generate_salt() -> str:
    return secrets.token_hex(16)  # 32 hex chars, 128-bit salt

def hash_password(password: str, salt: str) -> str:
    return hashlib.sha256((salt + password).encode("utf-8")).hexdigest()

def signup(username: str, password: str) -> bool:
    data = load_creds()

    if username in data["users"]:
        print("User already exists")
        return False

    salt = generate_salt()
    pwd_hash = hash_password(password, salt)

    data["users"][username] = {
        "salt": salt,
        "password": pwd_hash
    }

    save_creds(data)
    print("Signup successful")
    return True

def login(username: str, password: str) -> bool:
    data = load_creds()

    if username not in data["users"]:
        print("User not found")
        return False

    user = data["users"][username]
    salt = user["salt"]
    stored_hash = user["password"]

    if stored_hash == hash_password(password, salt):
        print("Login successful")
        return True
    else:
        print("Wrong password")
        return False

def main():
    while True:
        choice = input("1 = signup, 2 = login, q = quit: ").strip()

        if choice == "q":
            break

        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if choice == "1":
            signup(username, password)
        elif choice == "2":
            login(username, password)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
