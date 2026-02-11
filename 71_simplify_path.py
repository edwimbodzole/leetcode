class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        lst = path.split('/')
        stack = []
        for d in lst:
            if d == "..":
                if stack:
                    stack.pop()
            elif d != "" and d != ".":
                stack.append(d)

        return "/" + "/".join(stack)
        """
        stack = []
        curr = ""

        for d in path + "/":
            if d == "/":
                if curr == "..":
                    if stack:
                        stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""
            else:
                curr += d

        return "/" + "/".join(stack)
