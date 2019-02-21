"""-*- coding: utf-8 -*-
 @Author  : Peter_Bonnie
 @FileName    : rpn.py
"""
"""
desc: write an interpreter for a reverse Polish notation calculator
      operators:+-*/
      
      1.Operands should be pushed onto a stack
      2.popped as needed when receive an operator
      3.each step should print the top element    
"""
"""define a stack class"""
class Stack(object):

    def __init__(self):
        """initial a stack"""
        self.stack=[]
    def get_top(self):
        """get top stack elements"""
        if not self.is_empty():
             return self.stack[self.stack_size()-1]

    def pop(self,index):
        """pop element from stack"""
        return self.stack.pop(index)

    def push(self,element):
        """push element onto stack"""
        self.stack.append(element)

    def output(self):
        """print the stack"""
        return self.stack

    def stack_size(self):
        """return the size of stack"""
        return len(self.stack)

    def is_empty(self):
        """judge the stack is empty or not"""
        if self.stack_size()==0:
            return True
        else:
            return False

if __name__=='__main__':

    import sys
    operators=['+','-','*','/','~']
    stack=Stack()

    """get input data"""
    elements=sys.stdin.readlines()
    # print(elements)

    for element in elements:
        elem=element.strip('\n')

        if elem in operators:
            if stack.is_empty():
                print("invalid operation")
            else:
                if elem=='~':
                    stack.pop(-1)
                else:
                    if stack.stack_size()==1:
                        print("invalid operation")
                    """pop two elems from stack"""
                    a=stack.pop(-1)
                    b=stack.pop(-1)

                    """if receive the following operators,then run corresponding code"""
                    if elem=='+':
                        c=a+b
                        stack.push(c)
                    elif elem=='-':
                        c=b-a
                        stack.push(c)
                    elif elem=='*':
                        c=b*a
                        stack.push(c)
                    elif elem=='/':
                        try:
                          c=b/a
                        except:
                           raise ZeroDivisionError("division by zero")
                        else:
                           stack.push(c)
                    print(stack.get_top())
        else:
            stack.push(int(element))
            print(stack.get_top())















