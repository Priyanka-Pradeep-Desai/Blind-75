## 📌 **Find All Anagrammatic Substrings**  
### **Problem Statement**  
Given a string `s`, find all substrings that have anagrams in the original string.  
Return a list of these anagrammatic substrings in any order.  

### 🚀 **Examples & Explanation**  
#### **Example 1:**  
**Input:** `s = "abccba"`  
**Output:** `["ab", "ba", "bc", "cb", "abc", "cba", "bcc", "ccb", "abcc", "ccba", "abccb", "bccba"]`  
**Explanation:**  
These substrings have at least one anagram elsewhere in the string.  

### ⏳ **Constraints**  
- 2 ≤ leq s.length ≤ leq 10^4
- `s` consists of lowercase English letters only.  

---

## ❌ **Brute Force Approach (Not Recommended)**  
```python
from collections import defaultdict
class Solution:
    def substringAnagrams(self, s):
        anagrams = defaultdict(set)

        # generate all substrings of s
        for start in range(len(s)):
            for end in range(start, len(s)):
                substring = s[start : end + 1]
                anagrams[''.join(sorted(substring))].add(substring)

        res = []
        for anagramSet in anagrams.values():
            if len(anagramSet) > 1:
                res.extend(list(anagramSet))

        return sorted(res, key = lambda x : (len(x), x))

S = Solution()
print(S.substringAnagrams('abccba'))
```
**Time Complexity:** **O(N³ log N)** → **Inefficient for large inputs**.  

---

## 📝 **Optimized Code Pseudocode**  
```plaintext
Initialize result list
For each possible substring length from 2 to n:
    Initialize character frequency array of size 26
    Initialize a hashmap to store frequency patterns and starting indices
    
    Process the first substring of the current length
    Add its frequency pattern to the hashmap

    Slide the window across the string:
        Remove the outgoing character from frequency array
        Add the new incoming character

        If the updated frequency pattern exists in the hashmap:
            Append matching substrings to result list

        Store the current window’s start index in hashmap
    
Return result list
```

---

## 🔍 **Explanation**  
**Using Sliding Window + Hash Map:**  
- We **track character frequencies** in a **sliding window** rather than sorting substrings.  
- **Hash map stores frequency patterns** as tuples to identify anagrams efficiently.  
- Instead of generating and sorting all substrings, we update frequencies in **O(1) time** per move.  

### **Why is this optimal?**  
✅ **Avoids sorting (\(O(k \log k)\))**  
✅ **Sliding window updates in O(1) time**  
✅ **Uses hash map for fast lookups**  

---

## ⏳ **Complexity Analysis**  
- **Time Complexity:** **O(N²)**  
  - Outer loop runs **O(N)** (substring lengths).  
  - Inner loop runs **O(N)** (sliding window updates).  
  - Each update takes **O(1)** → Total **O(N²)**.  

- **Space Complexity:** **O(N)**  
  - Dictionary stores unique **frequency patterns** instead of all substrings.  

---

## ✅ **Conclusion**  
- **Sliding Window + Hash Map** reduces unnecessary sorting and recomputation.  
- Provides a much faster **O(N²) solution** compared to the brute force **O(N³ log N)** approach.  
- Recommended for **competitive programming** and **interview problems**. 🚀  
