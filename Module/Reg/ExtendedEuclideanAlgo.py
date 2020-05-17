
def EEA_int(r0, r1):
    """
    EEA for integers 
    """
    oldr0 = r0
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    i = 1
    ri = 0
    si = 0
    ti = 0
    qi_1 = 0

    while(True):
        i = i + 1
        ri = r0%r1
        qi_1 = (r0-ri)/r1

        si = s0 - qi_1*s1
        ti = t0 - qi_1*t1


        s0 = s1
        s1 = si
        t0 = t1
        t1 = ti
        r0 = r1
        r1 = ri
        if(ri == 0):
            break
    ri = r0

    si = s0;
    ti = t0;
    
    if(ti < 0):
        ti = oldr0 + ti;
    print("EEA output: gcd="+str(ri) + ", inverse="+str(ti))
    return ri, ti       #ri is the gcd, ti is the inverse

def EEA_poly(r0, r1):
    """
    EEA for polynomials
    """
    pass