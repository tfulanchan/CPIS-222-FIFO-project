# The random module provides functions for generating random numbers and performing random selections
import random
# The psutil provides an interface for retrieving information on running processes and system utilization
import psutil

# Function to simulate page reference string
def simulate_page_reference_string(n, method):
    if method == 'manual':
        # Get page reference string from user input
        # Prompt the user to enter a comma-separated string of values and assign the resulting string to the variable page_reference_string
        page_reference_string = input("Enter page reference string (comma-separated): ")
        # Call the split() method on the page_reference_string variable with the separator ',' to split the string into a list of substrings
        # Pass the resulting list of substrings to the map() function along with the int() function to convert each substring to an integer
        # The map() function applies the int() function to each element of the list and returns a new list of integers
        # The list() function converts the resulting map object into a list of integers
        # Assign the list of integers to the variable page_reference_string
        page_reference_string = list(map(int, page_reference_string.split(',')))
    elif method == 'uniform':
        # Generate page reference string using uniform distribution
        # Generate a list of n random integers between 0 and 9 (inclusive) with a length of n
        # The randint() function from the random module generates random integers between two endpoints, which are 0 and 9
        # The resulting list is assigned to the variable page_reference_string
        page_reference_string = [random.randint(0, 9) for i in range(n)]
    elif method == 'gaussian':
        # Generate page reference string using Gaussian distribution
        # The gauss() function from the random module generates random numbers from a Gaussian distribution
        # The mean of the distribution is 4 and the standard deviation is 2
        # Calculate the modulo (the remainder when dividing) of the resulting random number with 10 to ensure that it falls between 0 and 9
        page_reference_string = [int(random.gauss(4, 2)) % 10 for i in range(n)]
    else:
        raise ValueError("Invalid method")

    return page_reference_string

# Function to simulate page replacement algorithm, take three parameters:
# page_reference_string is a list of integers that represents the page reference string for the simulation
# num_frames is an integer that represents the number of page frames available for the simulation 
# algorithm is a string that specifies which page replacement algorithm to use for the simulation
def simulate_page_replacement_algorithm(page_reference_string, num_frames, algorithm):
    # creates an empty dictionary with no key-value pairs and assigns it to the variable memory_status
    # A dictionary is a collection of key-value pairs, where each key is unique and maps to a corresponding value
    # Initialize an empty dictionary that will be used to store the memory status during the simulation of the page replacement algorithm
    memory_status = {}
    page_faults = 0

    # a for loop in Python that iterates over the elements of the page_reference_string list
    # the page_reference_string list represents the sequence of page references that the algorithm will process
    # Iterate over each page in the sequence and perform the necessary operations
    # Check if the page is already in memory, select a page to evict if necessary, and update the memory status
    for page in page_reference_string:
        # Check if the page variable is a key in the memory_status dictionary
        # the memory_status dictionary represents the current state of the memory, where each key is a page that is currently in memory, 
        # and the corresponding value is some information about that page, such as its last access time or its location in physical memory 
        # If the current page reference page is already in memory, skips the page fault handling code since no page needs to be evicted
        # If page is not in memory_status, the page fault handling code is executed to select a page to evict 
        # and update the memory_status dictionary.
        if page in memory_status:
            # Page is already present in memory
            pass
        else:
            # Page is not present in memory, so a page fault occurs
            page_faults += 1

            # Check if the length of the memory_status dictionary is less than the num_frames variable
            # The len() function is used to get the number of items in the memory_status dictionary
            if len(memory_status) < num_frames:
                # There is a free frame, so load the page into it
                # the memory_status dictionary represents the current state of the memory where each key is a page that is currently in memory
                # Update the memory_status dictionary to indicate that the page is now in memory by setting its value to True
                memory_status[page] = True
            else:
                # All frames are occupied, so use a page replacement algorithm to select a frame to replace
                if algorithm == 'LRU':
                    # Least Recently Used algorithm
                    # Find the oldest page in memory based on its last access time, so that it can be replaced by a new page
                    # The min() function is used to find the minimum value in the dictionary, which is the oldest page in memory,
                    # based on the values returned by the memory_status.get method
                    # The key parameter specify the function that is used to extract the values from the dictionary
                    # The memory_status.get method extract the values which represent the last access time of each page
                    oldest_page = min(memory_status, key=memory_status.get)
                    # Remove the oldest page from memory based on its last access time, so that it can be replaced by a new page
                    del memory_status[oldest_page]
                    # Update the memory_status dictionary to indicate that the page is now in memory by setting its value to True
                    memory_status[page] = True
                elif algorithm == 'FIFO':
                    # First In First Out algorithm
                    # Traverse through all the values and retrieve the first key in the memory_status dictionary,
                    # then assign it to the variable oldest_page
                    # The iter() function create an iterator object for the dictionary
                    # The next() function retrieve the first key in the dictionary
                    oldest_page = next(iter(memory_status))
                    del memory_status[oldest_page]
                    # Update the memory_status dictionary to indicate that the page is now in memory by setting its value to True
                    memory_status[page] = True
                else:
                    raise ValueError("Invalid algorithm")

        # Print memory status
        # Output the string "Memory status: " to the console without adding a newline character at the end of the string
        # Start the next line of output on the same line as the memory status information that is printed later in the program
        # The end parameter specifies the character that should be used to separate the printed text from the next line of output
        print("Memory status: ", end="")
        # Create a loop that iterates over a sequence of numbers generated by the range() function
        # Assign each value in the sequence to the variable frame which can be used in the body of the loop
        # The range() function generates a sequence of numbers that can be used to control the number of iterations in a loop
        for frame in range(num_frames):
            # Check if the variable frame is a key in the memory_status dictionary
            # The in keyword checks if the key is present in the dictionary
            # If the key is present, the in keyword returns True, otherwise it returns False
            if frame in memory_status:
                print(frame, end=" ")
            else:
                print("-", end=" ")
        # Output the current memory status and the results of a page replacement algorithm to the console
        print()

    # Exit the function
    return page_faults

# Get input arguments from user
n = int(input("Enter number of pages: "))
method = input("Enter page reference string generation method (manual/uniform/gaussian): ")
num_frames = int(input("Enter number of available frames: "))
algorithm = input("Enter page replacement algorithm (LRU/FIFO): ")

# Simulate page reference string
# Call the simulate_page_reference_string() function with the arguments n and method
# refer to above for details
page_reference_string = simulate_page_reference_string(n, method)

# Simulate page replacement algorithm
# Call the function simulate_page_replacement_algorithm() 
# with the arguments page_reference_string, num_frames, and algorithm
# Assign the return value of the function to the variable page_faults
# refer to above for details
page_faults = simulate_page_replacement_algorithm(page_reference_string, num_frames, algorithm)

# Output number of page faults
print("Number of page faults:", page_faults)

# Get current memory usage of the program
# Using the psutil module, assign the amount of memory currently being used by the system to the variable memory_usage
memory_usage = psutil.virtual_memory().used
print("Current memory usage:", memory_usage)