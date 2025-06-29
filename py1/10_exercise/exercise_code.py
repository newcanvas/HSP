def sort_mass(x):
    ind = 0
    
    while ind < len(x):
        for i in range(ind, len(x)):    
            if i == ind:
                  min10 = x[ind]
                  min_ind = ind
                    
            elif x[i] < min10:
                min10 = x[i]
                min_ind = i
                
        x[ind], x[min_ind] = x[min_ind], x[ind]
        ind += 1
    return x
