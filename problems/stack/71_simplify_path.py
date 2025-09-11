"""
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.
"""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirs = [d for d in path.split('/') if d]
        stack = []
        for directory in dirs:
            if directory == '.':
                continue
            if directory == '..':
                # don't pop if we are at the root already
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(directory)
        
        return "/" + "/".join(stack)

        # push the dir
        # ignore .
        # pop the ..
        

if __name__ == "__main__":
    sol = Solution()
    
    assert sol.simplifyPath("/home/") == "/home"
    assert sol.simplifyPath("/home//foo/") == "/home/foo"
    assert sol.simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures"
    assert sol.simplifyPath("/../") == "/"
    assert sol.simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d"
    
    print("All test cases passed!")