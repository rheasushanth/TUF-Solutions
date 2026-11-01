# [65. Merge two Sorted Lists](https://takeuforward.org/practice/dsa/merge-sorted-lists-)

![Difficulty: Unspecified](https://img.shields.io/badge/Difficulty-Unspecified-6b7280?style=for-the-badge)

---

## 📝 Problem Statement

Given the heads of two linked lists, list1 and list2, where each linked list has its elements sorted in non-decreasing order, **merge** them into a single sorted linked list and return the head of the merged linked list.

### Example 1:

**Input:** list1 = head -> 2 -> 4 -> 7 -> 9, list2 = head -> 1 -> 2 -> 5 -> 6

**Output:** head -> 1 -> 2 -> 2 -> 4 -> 5 -> 6 ->7 -> 9

**Explanation:** head -> <u>1</u> -> <u>2</u> -> 2 -> 4 -> <u>5</u> -> <u>6</u> ->7 -> 9, the underlined nodes come from list2, the others come from list1.

### Example 2:

**Input:** list1 = head -> 1 -> 2 -> 3 -> 4, list2 = head -> 5 -> 6 -> 10

**Output:** head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 10

**Explanation:** head -> 1 -> 2 -> 3 -> 4 -> <u>5</u> -> <u>6</u> -> <u>10</u>, the underlined nodes come from list2, the others come from list1.

Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

### Constraints

- 0 <= number of nodes in list1, list2 <= 5 * 10^4
- -10^4 <= ListNode.val <= 10^4
- list1 and list2 are sorted in non-decreasing order.

---

## 💡 Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$
- **Space Complexity:** $\mathcal{O}(1)$

---

<p align="center">
  Generated with ❤️ by <a href="https://github.com/Arora-Sir">Mohit Arora</a> &nbsp;|&nbsp; Practice on <a href="https://takeuforward.org/pricing?affiliate=arorasir">TakeUForward (TUF+)</a> &nbsp;|&nbsp; ⭐ <a href="https://github.com/Arora-Sir/TUFHub">Star TUFHub on GitHub</a>
</p>
