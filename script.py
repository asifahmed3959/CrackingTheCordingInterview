# Function to generate permutations
def generate_permutations(nums):
    # Base case: if the list is empty or has one element, return the list itself
    def back_track(curr):
        if len(curr) == len(nums):
            ans.append(curr.copy())
            return

        for num in nums:
            if num not in curr:
                curr.append(num)
                back_track(curr)
                curr.pop()

    ans = []
    back_track([])
    return ans



# Example usage
arr = [1, 2, 3]
permutations = generate_permutations(arr)

# Print the permutations
for perm in permutations:
    print(perm)
