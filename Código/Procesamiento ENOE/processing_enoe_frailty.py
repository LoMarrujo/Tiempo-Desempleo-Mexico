import numpy as np


def inferior(row):
    '''Maps dur_des, by row, to left time in censoring interval.

    Args:
        dur_des (integer): Values from 1-6

    Returns: 
        inferior (integer): left time in censoring interval.
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
    '''Maps dur_des, by row, to right time in censoring interval.

    Args:
        dur_des (integer): Values from 1-6

    Returns: 
        inferior (integer): right time in censoring interval.
    '''

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


def parentesco(row):
    ''' Maps par_c, by row, to household relaionships of interest.

    Args:
        par_c (integer): see Instructivo de Codificación de Parentescos (2021) of INEGI.

    Returns: 
        parentesco (string): parentesco.
    '''

    if row['par_c'] == 101:
        parentesco_ = 'jefe'
    elif ((row['par_c'] == 201) | (row['par_c'] == 202) | (row['par_c'] == 203)):
        parentesco_ = 'espo'
    elif ((
        row['par_c'] == 301) | (row['par_c'] == 302) | (
        row['par_c'] == 303) | (row['par_c'] == 304) | (
        row['par_c'] == 408) | (row['par_c'] == 409
                                )):
        parentesco_ = 'desc'
    else:
        parentesco_ = np.nan
    return parentesco_


def macro_region(row):
    '''Returns a integer label for the macro-region of the individual.

    Args:
        ent (integer): see Instructivo de Codificación of INEGI for ENOE.

    Returns:
        region_int (integer): label for macro-region.
    '''
    vals_region_centro = [9, 15, 13, 17, 21, 22, 29]
    vals_region_centro_occidente = [6, 11, 14, 16, 18]
    vals_region_centro_norte = [1, 24, 32]
    vals_region_sur = [7, 12, 20]
    vals_region_este = [30, 27]
    vals_region_peninsula = [4, 23, 31]
    vals_region_noreste = [19, 28]
    vals_region_noroeste = [2, 3, 25, 26]
    vals_region_norte = [5, 8, 10]

    if row['ent'] in (vals_region_centro):
        region_int = 0
    elif row['ent'] in (vals_region_centro_occidente):
        region_int = 1
    elif row['ent'] in (vals_region_centro_norte):
        region_int = 2
    elif row['ent'] in (vals_region_sur):
        region_int = 3
    elif row['ent'] in (vals_region_este):
        region_int = 4
    elif row['ent'] in (vals_region_peninsula):
        region_int = 5
    elif row['ent'] in (vals_region_noreste):
        region_int = 6
    elif row['ent'] in (vals_region_noroeste):
        region_int = 7
    elif row['ent'] in (vals_region_norte):
        region_int = 8
    else:
        region_int = -1
    return region_int


def genero(row):
    '''Returns a integer label for the gender of the individual.

    Args:
        sex (integer): see Instructivo de Codificación of INEGI for ENOE.

    Returns:
        gender (integer): gender label.
    '''
    if row['sex'] == '1':
        gender = 0
    elif row['sex'] == '2':
        gender = 1
    else:
        gender = -1
    return gender


def etapa_vida(row):
    '''Returns a integer label for the life stage of the individual.

    Args:
        eda (integer): see Instructivo de Codificación of INEGI for ENOE.

    Returns:
        etapa (integer): life stage label.
    '''
    if row['eda'] < 25:
        etapa = 0
    elif (row['eda'] >= 25) & (row['eda'] < 45):
        etapa = 1
    elif (row['eda'] >= 45):
        etapa = 2
    else:
        etapa = -1
    return etapa


def chamacos(row):
    '''Returns the number of children of the individual.
    This function also maps non-valid integers to -1.

    Args:
        n_hij (integer): see Instructivo de Codificación of INEGI for ENOE.

    Returns:
        chamacos (integer): number of children.
    '''
    chamacos = ['00', '0', '1', '2', '3', '4']
    chamacos_2 = ['5', '6', '7', '8', '9', '10', '11', '12']

    if row['n_hij'] in chamacos:
        chamacos = int(row['n_hij'])
    elif row['n_hij'] in chamacos_2:
        chamacos = 5
    else:
        chamacos = -1
    return chamacos


def ant_lab(row):
    '''Returns the label for work experience of the individual.

    Args:
        d_ant_lab (integer): see Instructivo de Codificación of INEGI for ENOE.

    Returns:
        ant_lab (integer): number of children.
    '''

    if row['d_ant_lab'] == 1:
        ant_lab = 0
    elif row['d_ant_lab'] == 2:
        ant_lab = 1
    else:
        ant_lab = -1
    return ant_lab


def niv_ed(row):
    '''Returns the label for education level of the individual.

    Args:
        cs_p13_1 (string): see Instructivo de Codificación of INEGI for ENOE.

    Returns:
        niv_ed (integer): education level.
    '''
    if row['cs_p13_1'] == '1' or row['cs_p13_1'] == '2' or row['cs_p13_1'] == '3':
        niv_ed = 0
    elif row['cs_p13_1'] == '4' or row['cs_p13_1'] == '5':
        niv_ed = 1
    elif row['cs_p13_1'] == '6' or row['cs_p13_1'] == '7':
        niv_ed = 2
    elif row['cs_p13_1'] == '8' or row['cs_p13_1'] == '9':
        niv_ed = 3
    else:
        niv_ed = -1
    return niv_ed
