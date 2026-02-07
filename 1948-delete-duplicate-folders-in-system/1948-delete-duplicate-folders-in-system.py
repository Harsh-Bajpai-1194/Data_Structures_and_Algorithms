class TreeNode:  
    def __init__(self):  
        self.children = {}  
        self.path = None  
        self.hash = ""  
        self.deleted = False
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        root = TreeNode()  
        for path in paths:  
            node = root  
            for folder in path:  
                if folder not in node.children:  
                    node.children[folder] = TreeNode()  
                node = node.children[folder]  
                node.path = path  
        count = defaultdict(int)  
        def dfs(node):  
            if not node.children:  
                node.hash = ""  
                return node.hash  
            parts = []  
            for folder in sorted(node.children):  
                parts.append(folder + "(" + dfs(node.children[folder]) + ")")  
            node.hash = "".join(parts)  
            count[node.hash] += 1  
            return node.hash  
        dfs(root)  
        def mark(node):  
            if node.hash and count[node.hash] > 1:  
                node.deleted = True  
            for child in node.children.values():  
                mark(child)  
        mark(root)  
        res = []  
        def collect(node, path):  
            for folder, child in node.children.items():  
                if not child.deleted:  
                    new_path = path + [folder]  
                    if child.path:  
                        res.append(new_path)  
                    collect(child, new_path)  
        collect(root, [])  
        return res