class Stack():
    def __init__(self):
        self.dat=[]
    def pop(self):
        return self.dat.pop()
    def put(self, t):
        self.dat.append(t)
        return
    def look(self):
        return self.dat[-1]
    def take(self):
        return self.dat
    def empty(self):
        if len(self.dat)==0: return True
        else: return False
def parse(s):
    temp={'+':1, '-':1, '*':2, '/':2, '=':-1, '(':3, ')':0}
    st=Stack()
    out=[]
    if '=' in s:
        ind=s.index('=')
        while s[-1]!='=':
            
    for i in s:
        if i.isdigit():
            out.append(int(i))
        else:
            if i==')':
                while True:        #push out all items before a opening bracket
                    t=st.pop()
                    if t!='(': out.append(t)
                    else: break
                continue
            if st.empty():
                st.put(i)
            else:
                t=st.look()
                if temp[t]<temp[i]:
                    st.put(i)
                else:
                    f=True
                    while f and not st.empty():
                        t=st.pop()
                        if temp[t]>temp[i] and t!='(': out.append(t)
                        else:
                            f=False
                            st.put(t)
                    else: st.put(i)
        print(st.take(), out)
    while not st.empty():
        out.append(st.pop())
    return out[::-1]
    
def calc(s):
    ops='+-*//^'
    st=Stack()
    while len(s)>0:
        t=s.pop()
        if type(t)==int:
            st.put(t)
        else:
            a=st.pop()
            b=st.pop()
            op=t
        
            if op=='+': c=a+b
            elif op=='-': c=b-a
            elif op=='*': c=a*b
            elif op=='/': c=b/a
            elif op=='//': c=b//a
            elif op=='^': c=b**a
            st.put(c)
            print(st.take(), s)
    return st.take()
s=input()

s=parse(s)
print(s, 'wwssw')
print(*calc(s))
            
        
