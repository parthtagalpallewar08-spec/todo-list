# The account_ids list must be sorted for binary search to work correctly.
account_ids = [1001, 1003, 1006, 1007, 1010, 1012, 1015]

def linear_search(account_ids, target):
    """Searches for a target in a list using Linear Search."""
    for i in range(len(account_ids)):
        if account_ids[i] == target:
            # Found the target, return the position (1-indexed for user clarity)
            return f"Target {target} found at position {i + 1} (Linear Search)."
    
    # Target not found
    return f"Target {target} not found (Linear Search)."

def binary_search(account_ids, target):
    """Searches for a target in a SORTED list using Binary Search."""
    low = 0
    high = len(account_ids) - 1
    
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        
        if account_ids[mid] == target:
            # Found the target
            return f"Target {target} found at position {mid + 1} (Binary Search)."
        elif account_ids[mid] < target:
            # Target is in the upper half
            low = mid + 1
        else: # account_ids[mid] > target
            # Target is in the lower half
            high = mid - 1
            
    # Target not found
    return f"Target {target} not found (Binary Search)."

# --- Execution ---
try:
    # Get the target ID from the user
    target_id = int(input("Enter customer account ID to search: "))
    
    # Run the searches
    print(linear_search(account_ids, target_id))
    print(binary_search(account_ids, target_id))

except ValueError:
    print("Invalid input. Please enter a number for the account ID.")