class stack:
    def __init__(self,n):
        self.l =[]
        self.n= n
    def push(self,a):
        if self.isfull():
            return
        return self.l.append(a)
    def popit(self):
        if self.isempty():
            return
        return self.l.pop()
    def peek(self):
        if self.isempty():
            return
        return self.l[-1]
    def isfull(self):
        if len(self.l)==self.n:
            return True
        return False
    def isempty(self):
        if len(self.l)==None:
            return True
        return False

st = stack(5)
st.push(1)
st.push(2)
st.push(3)
st.push(4)
print(st.l)
st.popit()
print(st.l)
print(st.peek())