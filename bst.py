"""-*- coding: utf-8 -*-
 @author  : Peter_Bonnie
 @fileName    : bst.py
"""
"""
desc: implement a binary search tree class,give some commmand line,eg:i stands for insert,and q is query
"""
"""
mainly operations following the steps:
    insert:
    1.judge the tree is null or not
    2.if null ,then create new tree,else insert the value in suit place.
    query:
    1.if found,print found and its trace,else print not found.
"""
class TNode(object):

    def __init__(self,key):
        self.key=key
        self.rChild=None
        self.lChild=None

class Binary_Search(object):

    def __init__(self):
        pass

    """when receive command i,call this function"""
    def insert(self,root,key):

        if root==None:
            root=TNode(key)
        else:
            if key<root.key:
                root.lChild=self.insert(root.lChild,key)
            elif key>root.key:
                root.rChild=self.insert(root.rChild,key)
        return root

    """when receive command q,call this function"""
    def query(self,root,key,trace_list=list()):

        if root==None:
            print("not found")
            return 0
        if root.key==key:
            if len(trace_list)==0:
                print("found: root")
            else:
                print("found: "+' '.join(trace_list))
            return 0
        elif key<root.key:
            trace_list.append('l')
            return self.query(root.lChild,key,trace_list)
        elif key>root.key:
            trace_list.append('r')
            return self.query(root.rChild,key,trace_list)

"""run the code"""
if __name__=="__main__":

    import sys
    """define an object of Binary_Search"""
    bst = Binary_Search()
    root = None

    """step1:receive command line"""
    command_lines=sys.stdin.readlines()
    for line in command_lines:
        # print(line.strip('\n').split(" "))
        command_line,number=line.strip('\n').split(" ")
        number=int(number)
        """step2:judge insert or query"""
        if command_line=='i':
            """execute the insert operation"""
            root=bst.insert(root=root,key=number)
        elif command_line=='q':
            """execute the query operation"""
            bst.query(root=root,key=number,trace_list=[])
        else:
            print("invalid input")

