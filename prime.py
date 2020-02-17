from mpi4py import MPI
import time
import sys

# Attach to the cluster and find out which node I am and how big cluster is
comms = MPI.COMM_WORLD
rank = comms.Get_rank()
cluster_size = comms.Get_size()

# Number to start on, based on the node's rank
start = (rank * 2) + 1

# When to stop
end = int(sys.argv[1])

# Make a note of the start time
start = time.time()

# List of discovered primes for this node
primes = []

# Loop through the numbers using rank number to divide the work
for candidate_number in range(start, end, cluster_size * 2):

    # Log progress in steps
    # print(candidate_number)

    # Assume this number is prime
    found_prime = True

    # Go through all previous numbers and see if any divide without remainder
    for div_number in range(2, candidate_number):
        if candidate_number % div_number == 0:
            found_prime = False
            break

    # If we get here, nothing divided, so it's a prime number
    if found_prime:
        # Uncomment the next line to see the primes as they are found (slower)
        print('Node ' + str(rank) + ' found ' + str(candidate_number))
        primes.append(candidate_number)

# Once complete, send results to the controller
results = comms.gather(primes, root=0)

# If node is controller, show results
if rank == 0:

    # Duration
    end = round(time.time() - start, 2)

    print('Find all primes up to: ' + str(end))
    print('Nodes: ' + str(cluster_size))
    print('Time elasped: ' + str(end) + ' seconds')

    # Each process returned an array, so lets merge them
    merged_primes = [item for sublist in results for item in sublist]
    merged_primes.sort()
    print('Primes discovered: ' + str(len(merged_primes)))
    # Uncomment the next line to see all the prime numbers
    print('Primes found:')
    print(merged_primes)
