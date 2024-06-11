class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Problrm description:

        Given two strings s and t, return true if they are equal when both are typed into empty text editors.
        
        '#' means a backspace character.

        Note that after backspacing an empty text, the text will continue empty.
        """
        lst_s = []
        lst_t = []

        ls, lt = len(s), len(t)

        for i in range(ls):
            if s[i] != "#":
                lst_s.append(s[i])
            else:
                if lst_s:
                    lst_s.pop()

        for i in range(lt):
            if t[i] != "#":
                lst_t.append(t[i])
            else:
                if lst_t:
                    lst_t.pop()

        if lst_s == lst_t:
            return True
        else:
            return False