class Node :
    def_init_(self,val):
    self.val=val
    self.left=self.right=None
    def build(expr):
        stack=[]
        for ch in reverced(expr):
            node=Node(ch)
            if ch.isalpha()or ch.isdigit():
                stack.append(node)
            else:
                if len(stack)<2:
                    raise ValueError(f"Invalid prefix expresssion:insufficient operands for operator'{ch}'")
                node.left=stack.pop()
                node.right=stack.pop()
                stack.append(node)
                if len(stack)!=1:
                    raise ValueError("Invalid prefix expression:too many operands or operators.")
                return stack[0]
            def postorder_nonrec(root):
                if not root:
                    return
                s1,s2=[root],[]
                while s1:
                    node=s1.pop()
                    s2.append(node.left)
                    while s2:
                        print(s2.pop().val,end='')
                        def delete_tree(root):
                            """Recursively delete all nodes."""
                            if root is None:
                                return
                            delete_tree(root.left)
                            delete_tree(root.right)
                            root.left=None
                            root.right=None
                            if_name_=="_main_":
                            expr="+*abc"
                            try:
                                root=built(expr)
                                print("Postorder Traversal (NonRecursive):")
                                postorder_nonrec(root)
                                delete_tree(root)
                                print("\nTree deleted successfully.")
                            except ValueError as e:
                                print("Error.",e)
