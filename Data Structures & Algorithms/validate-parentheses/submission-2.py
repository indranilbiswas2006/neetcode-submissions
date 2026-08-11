class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        # Maps each closing bracket to its matching opening bracket
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:

            # If c is a closing bracket
            if c in closeToOpen:

                # Check that the stack is not empty and that
                # the most recent opening bracket matches c
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  # Remove the matching opening bracket
                else:
                    return False

            else:
                # If c is an opening bracket, add it to the stack
                stack.append(c)

        # Valid only if every opening bracket was matched, so then stack would be empty 
        return len(stack) == 0