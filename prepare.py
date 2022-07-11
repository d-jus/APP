from numpy import array, delete

def recon_length(vector: list):
    if len(vector) == 16:
        return True
    if len(vector) == 12:
        return False
    else:
        raise ValueError("vector must have corect the length")

def clean_vector(vector, short = False):
    if recon_length(vector) and short == False:
        return list(vector)  
    if recon_length(vector) and short:
        return list(delete(vector,[10, 11, 12, 13])) 
    else:
        return list(vector) 

#print(clean_vector([56,	9.1,	0,	0.3,	0.5,	0.6,	20,	20,	30,	1.1,	0,	0], short=True))