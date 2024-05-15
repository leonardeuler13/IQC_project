for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    if ((not i or j) and (i or j or not k) and (k or l) and (not j or not k or l) and (not l or not m) and (not k or not l or m)):
                        print(i, j, k, l, m)
