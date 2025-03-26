
## **📌 Two-Sum Problem**  

### **Problem Statement**  
Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.  

- Each input has **exactly one solution**.  
- You **may not** use the same element twice.  
- The answer can be returned in **any order**.  

---

### **🚀 Examples & Explanation**  

#### **Example 1:**  
```plaintext
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
```

#### **Example 2:**  
```plaintext
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

#### **Example 3:**  
```plaintext
Input: nums = [3,3], target = 6
Output: [0,1]
```

---

### **⏳ Constraints**  
- `2 <= nums.length <= 10^4`  
- `-10^9 <= nums[i] <= 10^9`  
- `-10^9 <= target <= 10^9`  
- **Only one valid answer exists.**  

---

### **📝 Pseudocode**
```plaintext
hashmap -> map()
for index, number in array:
    difference -> target - number
    if difference is in hashmap:
        return [hashmap[difference], index]
    hashmap[number] = index
return []
```

---

### **🔍 Explanation**
1. **Using a HashMap (Dictionary):**  
   - We iterate through the list while keeping track of numbers and their indices.  
   - At each step, we compute `complement = target - num`.  
   - If the complement exists in the dictionary, we return its index along with the current index.  

2. **Why is this optimal?**  
   - **Time Complexity:** `O(N)`, since we traverse the list once.  
   - **Space Complexity:** `O(N)`, since we store elements in a dictionary.  

---

### **❌ Brute Force Approach (Not Recommended)**
```python
def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```
- **Time Complexity:** `O(N^2)`, as it checks all pairs.  
- **Inefficient for large inputs.**  

---

### **✅ Conclusion**
- The **hash map approach** provides an optimal `O(N)` solution.  
- Efficiently finds the two numbers that sum to the target in a single pass.  
- **Recommended for competitive programming and coding interviews.**  
