def inferior(row):
    ''' Maps dur_des to left time in censoring interval.

    Args:
        dur_des (integer): Values from 1-6

    Returns: 
        inferior: left time in censoring interval.
    '''

    if row['dur_des'] == 1:
        inferior = 0
    elif row['dur_des'] == 2:
        inferior = 1
    elif row['dur_des'] == 3:
        inferior = 3
    elif row['dur_des'] == 4:
        inferior = 6
    elif row['dur_des'] == 5:
        inferior = 12        
    else:
        inferior = -1
    return inferior







def superior(row):
    if row['dur_des'] == 1:
        val = 1
    elif row['dur_des'] == 2:
        val = 3
    elif row['dur_des'] == 3:
        val = 6
    elif row['dur_des'] == 4:
        val = 12
    elif row['dur_des'] == 5:
        val = 99  
    else:
        val = -1
    return val

def imp_med(row):
    if row['dur_des'] == 1:
        val = 0.5
    elif row['dur_des'] == 2:
        val = 1.5
    elif row['dur_des'] == 3:
        val = 3
    elif row['dur_des'] == 4:
        val = 6
    elif row['dur_des'] == 5:
        val = 12  
    else:
        val = -1
    return val

def macro_region(row):
    #centro
    if row['ent'] == 9 or row['ent'] == 15 or row['ent'] == 13 or row['ent'] == 17 or row['ent'] == 21 or row['ent'] == 22 or row['ent'] == 29:
        val = 0
    #centro-occidente
    elif row['ent'] == 6 or row['ent'] == 11 or row['ent'] == 14 or row['ent'] == 16 or row['ent'] == 18:
        val = 1 
    #centro-norte
    elif row['ent'] == 1 or row['ent'] == 24 or row['ent'] == 32:
        val = 2   
    # sur
    elif row['ent'] == 7 or row['ent'] == 12 or row['ent'] == 20:
        val = 3           
    # este
    elif row['ent'] == 30 or row['ent'] == 27:
        val = 4   
    # península
    elif row['ent'] == 4 or row['ent'] == 23 or row['ent'] == 31:
        val = 5   
    # noreste
    elif row['ent'] == 19 or row['ent'] == 28:
        val = 6          
    # noroeste
    elif row['ent'] == 2 or row['ent'] == 3 or row['ent'] == 25 or row['ent'] == 26:
        val = 7             
    # norte
    elif row['ent'] == 5 or row['ent'] == 8 or row['ent'] == 10:
        val = 8            
    else:
        val = -1
    return (val)

def genero(row):
    if row['sex'] == '1':
        val = 0
    elif row['sex'] == '2':
        val = 1
    else:
        val = -1
    return val

def etapa_vida(row):
    if row['eda']  < 25:
        val = 0
    elif (row['eda'] >= 25) & (row['eda'] < 45):
        val = 1
    elif (row['eda'] >= 45) & (row['eda'] < 65):
        val = 2
    elif (row['eda'] >= 65):
        val = 3
    else:
        val = -1
    return val

def chamacos(row):
    if row['n_hij'] == '0':
        val = 0
    elif row['n_hij'] == '1':
        val = 1
    elif row['n_hij'] == '2':
        val = 2
    elif row['n_hij'] == '3':
        val = 3
    elif row['n_hij'] == '4':
        val = 4
    elif row['n_hij'] == '5':
        val = 5
    elif row['n_hij'] == '6':
        val = 6
    elif row['n_hij'] == '7':
        val = 7
    elif row['n_hij'] == '8':
        val = 8
    elif row['n_hij'] == '9':
        val = 9    
    elif row['n_hij'] == '10':
        val = 10     
    elif row['n_hij'] == '11':
        val = 11           
    elif row['n_hij'] == '12':
        val = 12
    else:
        val = -1
    return val

def ant_lab(row):
    if row['d_ant_lab'] == 1:
        val = 0
    elif row['d_ant_lab'] == 2:
        val = 1
    else:
        val = -1
    return val

def niv_ed(row):
    if row['cs_p13_1'] == '1' or row['cs_p13_1'] == '2' or row['cs_p13_1'] == '3':
        val = 0
    elif row['cs_p13_1'] == '4' or row['cs_p13_1'] == '5':
        val = 1
    elif row['cs_p13_1'] == '6' or row['cs_p13_1'] == '7': 
        val = 2
    elif row['cs_p13_1'] == '8' or row['cs_p13_1'] == '9':
        val = 3
    else:
        val = 100
    return val

def edad(row):
    if row['eda'] >= 15 or row['eda'] == '2' or row['eda'] == '3':
        val = 0
    elif row['cs_p13_1'] == '4' or row['cs_p13_1'] == '5':
        val = 1
    elif row['cs_p13_1'] == '6' or row['cs_p13_1'] == '7' or row['cs_p13_1'] == '8' or row['cs_p13_1'] == '9':
        val = 2
    else:
        val = -1
    return v