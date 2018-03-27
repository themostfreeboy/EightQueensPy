def conflict(state,nextX):
    nextY=len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in range (0,nextY-i):
            return True
    return False

def queens(num=8,state=()):
    for pos in range(num):
        if not conflict(state,pos):
            if len(state)==num-1:
                yield (pos,)
            else:
                for result in queens(num,state+(pos,)):
                    yield (pos,)+result

#def queens(num=8,state=()):
#    if len(state)==num-1:
#        for pos in range(num):
#            if not conflict(state,pos):
#                yield pos
#    else:
#        for pos in range(num):
#            if not conflict(state,pos):
#                for result in queens(num,state+(pos,)):
#                    yield(pos,)+result

def prettyprint(solution):
    def line(pos,length=len(solution)):
        return '. '*(pos)+'X '+'. '*(length-pos-1)
    for pos in solution:
        print line(pos)

def main():
    result=list(queens(8))
    number=len(result)
    print 'result:'
    print result
    print 'number:'+str(number)
    for solution in result:
        print prettyprint(solution)

if(__name__=="__main__"):main()
