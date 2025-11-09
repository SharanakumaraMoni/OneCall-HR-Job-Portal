import random
import mysql.connector

# Function to generate a random 4-digit OTP
def generate_otp():
    return random.randint(1000, 9999)

# Function to send OTP to MySQL Database
def send_to_database(mobile_number, otp):
    # Establish a connection to your MySQL server
    connection = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="your_database"
    )

    # Create a cursor object using the cursor() method
    cursor = connection.cursor()

    # Insert OTP into the database
    insert_query = "INSERT INTO otps (mobile_number, otp) VALUES (%s, %s)"
    data = (mobile_number, otp)
    cursor.execute(insert_query, data)

    # Commit changes and close the connection
    connection.commit()
    connection.close()
    print("OTP Sent to MySQL Database: {}".format(otp))

# Main function
if __name__ == "__main__":
    # Get mobile number from user input
    mobile_number = input("Enter your mobile number: ")

    # Generate OTP
    otp = generate_otp()

    # Send OTP to MySQL Database
    send_to_database(mobile_number, otp)
