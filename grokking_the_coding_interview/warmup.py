"""Grokking The Coding Interview Warmup"""

class Solution:
    def containsDuplicate(self, nums):
        """
        Return True if nums contains duplicate, False otherwise

        Time complexity
        len(n) = O(n)
        len(set(n)) = O(n)
        O(n) + O(n) = O(n) time

        Space complexity
        len(set(n)) = O(n) space
        """
        return len(nums) != len(set(nums))


    def checkIfPangram(self, sentence):
        """
        Return True if sentence is a pangram, False otherwise

        Time complexity
        sentence.lower() = O(n)
        for loop = O(n)
        len(unique_letter_set) = O(n)
        O(n) + O(n) + O(n) = O(n) time

        Space complexity
        sentence.lower() = O(n)
        unique_letter_set.add(ch) in for loop  = O(26) = O(1)
        O(n) + O(1) = O(n) space
        """
        if isinstance(sentence, str):
            unique_letter_count = 26
            unique_letter_set = set()
            sentence_lower = sentence.lower()

            for ch in sentence_lower:
                if ch.isalpha():
                    unique_letter_set.add(ch)

            return len(unique_letter_set) == unique_letter_count
        
    
    def reverseVowels(self, s: str) -> str:
        """
        Return s with vowels reversed

        Time complexity
        list(s) = O(n)
        len(c) = 0(1)  # len function maintains length information internally
        while loop = 1/2 length of n = O(n)
        .. in vowels = constant time because num of vowels is a constant and does not
        change with size of n


        Space complexity
        """
        if isinstance(s, str):
            vowels = ["a", "e", "i", "o", "u"]
            c = list(s)
            left_pointer = 0
            right_pointer = len(c) - 1

            while left_pointer < right_pointer and left_pointer != right_pointer:
                if c[left_pointer].lower() in vowels and c[right_pointer].lower() in vowels:
                    c[left_pointer], c[right_pointer] = c[right_pointer], c[left_pointer]
                    left_pointer += 1
                    right_pointer -= 1

                else:
                    if c[left_pointer].lower() not in vowels:
                        left_pointer += 1

                    if c[right_pointer].lower() not in vowels:
                        right_pointer -= 1

            reversed_vowels = "".join(c)
            return reversed_vowels
