def massdriver(activate: list) -> int:
    
    nums = {}
    repeats = []

    for i in range(len(activate)):
        if activate[i] in nums and nums[activate[i]] not in repeats:
            repeats.append(nums[activate[i]])
        elif activate[i] not in nums:
            nums[activate[i]] = i

    if repeats:
        return min(repeats)
    
    return -1

