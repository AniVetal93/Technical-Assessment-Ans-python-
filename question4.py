import re

def is_valid_number_plate(plate):
    """
    Check if the number plate is valid according to Indian private vehicle format.
    
    :param plate: The vehicle number plate as a string.
    :return: True if valid, False otherwise.
    """
    # Define the regex pattern for the number plate format
    pattern = r'^[A-Z]{2} \d{2} [A-Z]{2} \d{4}$'
    
    # Use regex to match the pattern
    if re.match(pattern, plate):
        return True
    return False

# Main function to run the program
if __name__ == "__main__":
    plate = input("Enter the vehicle number plate: ").strip()
    
    if is_valid_number_plate(plate):
        print("The number plate is valid.")
    else:
        print("The number plate is invalid.")
