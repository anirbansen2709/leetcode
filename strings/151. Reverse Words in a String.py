class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ""
        word = ""
        for char in s:
            if char != " ":
                word += char
            elif char == " " and word != "":
                answer = word + " " + answer
                word = ""
        if word != "":
            answer = word + " " + answer
        return answer[:-1]

# TC - O(n)
# SC - O(n)
