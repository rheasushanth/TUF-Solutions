# [141. Rabin Karp Algorithm](https://takeuforward.org/practice/dsa/rabin-karp-algorithm)

![Difficulty: Unspecified](https://img.shields.io/badge/Difficulty-Unspecified-6b7280?style=for-the-badge)

---

## 📝 Problem Statement

Given a string text and a string pattern, implement the **Rabin-Karp** algorithm to find the starting index of all occurrences of pattern in text. If pattern is not found, return an empty list.

### Example 1:

Input: text = "ababcabcababc", pattern = "abc"

Output: [2, 5, 10]

Expalanation : The pattern "abc" is found at indices 2, 5, and 10 in the text.

### Example 2:

Input: text = "hello", pattern = "ll"

Output: [2]

Explanation: The pattern "ll" is found at index 2 in the text.

Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

### Constraints

- 1<= text.length, pattern.length <=5*10^4

---

## 💡 Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

---

<p align="center">
  Generated with ❤️ by <a href="https://github.com/Arora-Sir">Mohit Arora</a> &nbsp;|&nbsp; Practice on <a href="https://takeuforward.org/pricing?affiliate=arorasir">TakeUForward (TUF+)</a> &nbsp;|&nbsp; ⭐ <a href="https://github.com/Arora-Sir/TUFHub">Star TUFHub on GitHub</a>
</p>
