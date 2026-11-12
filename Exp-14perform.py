import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("login.log"),
        logging.StreamHandler()
    ]
)

# User login details
username = "admin"
password = "1234"

# Login process
logging.debug("Login process started")

user = input("Enter username: ")
pwd = input("Enter password: ")

logging.info("User entered login details")

if user == username:
    logging.debug("Username is correct")

    if pwd == password:
        print("Login Successful!")
        logging.info("User logged in successfully")
    else:
        print("Incorrect Password!")
        logging.error("Invalid password entered")

else:
    print("User not found!")
    logging.warning("Invalid username entered")

logging.critical("Login system test completed")