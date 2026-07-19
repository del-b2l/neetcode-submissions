class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        print("New test case:", nums, k)
        lastSeen = set()
        l = 0

        for r in range(len(nums)):
            # print(f"r={r}, l={l}, set={lastSeen}, current={nums[r]}")
            if r - l > k:
                lastSeen.remove(nums[l])
                # print(f"r={r}, l={l}, set={lastSeen}, removed={nums[l]}")
                l += 1
            if nums[r] in lastSeen:
                return True
            lastSeen.add(nums[r])
            # print(f"r={r}, l={l}, set={lastSeen}, after={nums[r]}\n")
        return False