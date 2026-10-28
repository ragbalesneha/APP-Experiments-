# ==========================================
# Assignment No: 13
# Name: Sneha Ragbale
# Class: SY08
# Roll No: [54]
# ==========================================

# Step 1: Import the required modules
import gc
import tracemalloc
import time

# Step 2: Define a class for creating cyclic objects
class Node:
    def __init__(self):
        # Each node will store a reference to another node
        self.reference = None

if __name__ == "__main__":
    # Step 3: Start memory tracking
    # tracemalloc helps us measure Python memory allocations.
    tracemalloc.start()

    # Step 4: Create objects that refer to each other
    def create_cycles(number):
        for i in range(number):
            # Create two objects
            a = Node()
            b = Node()

            # Make the objects refer to each other
            # This creates a reference cycle.
            a.reference = b
            b.reference = a

            # When the function ends, the local variables disappear.
            # The objects still refer to each other, so the cycle
            # cannot be cleaned up by reference counting alone.

    # Step 5: Create many cyclic objects
    create_cycles(10000)

    # Step 6: Measure memory before manual collection
    current_before, peak_before = tracemalloc.get_traced_memory()

    # Display memory in kilobytes
    print("Memory before GC:",
        round(current_before / 1024, 2), "KB")

    # Step 7: Measure the time taken by manual garbage collection
    start_time = time.perf_counter()

    # Request garbage collection manually
    collected = gc.collect()

    # Calculate the time taken in seconds
    gc_time = time.perf_counter() - start_time

    # Step 8: Measure memory after collection
    current_after, peak_after = tracemalloc.get_traced_memory()

    # Step 9: Display the results
    print("Objects collected:", collected)

    print("Memory after GC:",
        round(current_after / 1024, 2), "KB")

    print("Peak traced memory:",
        round(peak_after / 1024, 2), "KB")

    print("GC execution time:",
        round(gc_time, 6), "seconds")

    # Step 10: Stop memory tracking
    tracemalloc.stop()