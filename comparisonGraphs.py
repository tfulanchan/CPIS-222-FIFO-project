import random
# psutil is a library that obtain information about CPU utilization
import psutil
# Matplotlib is a library for creating static, animated, and interactive visualizations
import matplotlib.pyplot as plt

# Function to simulate page reference string
def simulate_page_reference_string(n, method):
    if method == 'manual':
        # Get page reference string from user input
        page_reference_string = input("Enter page reference string (comma-separated): ")
        page_reference_string = list(map(int, page_reference_string.split(',')))
    elif method == 'uniform':
        # Generate page reference string using uniform distribution
        page_reference_string = [random.randint(0, 9) for i in range(n)]
    elif method == 'gaussian':
        # Generate page reference string using Gaussian distribution
        page_reference_string = [int(random.gauss(4, 2)) % 10 for i in range(n)]
    else:
        raise ValueError("Invalid method")

    return page_reference_string

# Function to simulate page replacement algorithm
def simulate_page_replacement_algorithm(page_reference_string, num_frames, algorithm):
    memory_status = {}
    page_faults = 0

    for page in page_reference_string:
        if page in memory_status:
            # Page is already present in memory
            pass
        else:
            # Page is not present in memory, so a page fault occurs
            page_faults += 1

            if len(memory_status) < num_frames:
                # There is a free frame, so load the page into it
                memory_status[page] = True
            else:
                # All frames are occupied, so use a page replacement algorithm to select a frame to replace
                if algorithm == 'LRU':
                    # Least Recently Used algorithm
                    oldest_page = min(memory_status, key=memory_status.get)
                    del memory_status[oldest_page]
                    memory_status[page] = True
                elif algorithm == 'FIFO':
                    # First In First Out algorithm
                    oldest_page = next(iter(memory_status))
                    del memory_status[oldest_page]
                    memory_status[page] = True
                else:
                    raise ValueError("Invalid algorithm")

    return page_faults

# Function to simulate page replacement algorithm for multiple values of Number of Frames and Number of Job Pages
def simulate_page_replacement_algorithm_comparison(njp_range, nf_range, method):
    # Initialize data arrays
    lru_page_faults_nf = []
    fifo_page_faults_nf = []
    lru_page_faults_njp = []
    fifo_page_faults_njp = []

    # Fix NJP and vary NF
    njp = 20
    for nf in nf_range:
        # Simulate page reference string using LRU algorithm
        page_reference_string = simulate_page_reference_string(njp, method)
        lru_page_faults = simulate_page_replacement_algorithm(page_reference_string, nf, 'LRU')
        # Append the list lru_page_faults to the list lru_page_faults_nf
        # The list lru_page_faults_nf stores a sequence of lists in a single list
        lru_page_faults_nf.append(lru_page_faults)

        # Simulate page reference string using FIFO algorithm
        page_reference_string = simulate_page_reference_string(njp, method)
        fifo_page_faults = simulate_page_replacement_algorithm(page_reference_string, nf, 'FIFO')
        fifo_page_faults_nf.append(fifo_page_faults)

    # Fix NF and vary NJP
    nf = 4
    for njp in njp_range:
        # Simulate page reference string using LRU algorithm
        page_reference_string = simulate_page_reference_string(njp, method)
        lru_page_faults = simulate_page_replacement_algorithm(page_reference_string, nf, 'LRU')
        lru_page_faults_njp.append(lru_page_faults)

        # Simulate page reference string using FIFO algorithm
        page_reference_string = simulate_page_reference_string(njp, method)
        fifo_page_faults = simulate_page_replacement_algorithm(page_reference_string, nf, 'FIFO')
        fifo_page_faults_njp.append(fifo_page_faults)

    # Plot graphs
    # Create a new figure object with a size of 10 inches by 5 inches
    plt.figure(figsize=(10, 5))

    # Create a new subplot within a figure object with a layout of 1 row and 2 columns
    # Set the current subplot to the first column
    plt.subplot(1, 2, 1)
    # Create the line plot of LRU within the subplot
    # with the x values represented by the nf_range variable and the y values represented by the lru_page_faults_nf variable
    # The label parameter is used to specify the label for the plot
    plt.plot(nf_range, lru_page_faults_nf, label='LRU')
    # Create the line plot of FIFO within the subplot
    plt.plot(nf_range, fifo_page_faults_nf, label='FIFO')
    # Set the label for the x-axis of a plot to "Number of frames (NF)"
    plt.xlabel('Number of frames (NF)')
    # Set the label for the y-axis of a plot to "Number of page faults"
    plt.ylabel('Number of page faults')
    plt.title('Comparison of LRU and FIFO algorithms (NJP=20)')
    # Add a legend to the plot
    plt.legend()

    # Set the current subplot to the second column
    plt.subplot(1, 2, 2)
    plt.plot(njp_range, lru_page_faults_njp, label='LRU')
    plt.plot(njp_range, fifo_page_faults_njp, label='FIFO')
    plt.xlabel('Number of job pages (NJP)')
    plt.ylabel('Number of page faults')
    plt.title('Comparison of LRU and FIFO algorithms (NF=4)')
    plt.legend()

    # Display the plot that has been created using other functions such as plot(), xlabel(), ylabel(), and legend()
    plt.show()



# Get input arguments from user
n = int(input("Enter number of pages: "))
method = input("Enter page reference string generation method (manual/uniform/gaussian): ")

# Set range of NJP and NF
# Create a range of numbers from 2 to 20
# Assign the range of numbers to the variable njp_range
njp_range = range(2, 21)
# Create a range of numbers from 2 to 10
# Assign the range of numbers to the variable nf_range
nf_range = range(2, 11)

# Simulate page replacement algorithm for multiple values of NF and NJP
simulate_page_replacement_algorithm_comparison(njp_range, nf_range, method)

# Get current memory usage of the program
memory_usage = psutil.virtual_memory().used
print("Current memory usage:", memory_usage)
