from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Problem Description:

        You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

        Evaluate the expression. Return an integer that represents the value of the expression.

        Note that:

        The valid operators are '+', '-', '*', and '/'.
        Each operand may be an integer or another expression.
        The division between two integers always truncates toward zero.
        There will not be any division by zero.
        The input represents a valid arithmetic expression in a reverse polish notation.
        The answer and all the intermediate calculations can be represented in a 32-bit integer.
        """
        my_st = []
        
        for i in tokens:
            if i not in "+-*/":
                my_st.append(i)
            else:
                second_num = int(my_st.pop())
                first_num = int(my_st.pop())
                if i == "+":
                    my_st.append(first_num + second_num)
                if i == "-":
                    my_st.append(first_num - second_num)
                if i == "*":
                    my_st.append(first_num * second_num)
                if i == "/":
                    my_st.append(int(first_num / second_num))
                
        return int(my_st.pop())
    

if __name__ == "__main__":
    c = Solution()
    tokens = ["2","1","+","3","*"]
    a = c.evalRPN(tokens)
    print(a)