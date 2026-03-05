'''
construindo a logica do not
'''

var_1 = True 
var_2 = False


print('var_1 {} quando negada fica {}'.format(var_1, not var_1))
print('var_2 {} quando negada fica {}'.format(var_2, not var_2))

'''
construindo a logica do and (E)
'''

var_1_t = True 
var_1_f = False
var_2_t = True
var_2_f = False

print('quando var_1_t é {} E var_2_t {} o resultado é {}'.format(var_1_t,var_2_t,var_1_t and var_2_t))
print('quando var_1_f é {} E var_2_t {} o resultado é {}'.format(var_1_f,var_2_t,var_1_f and var_2_t))
print('quando var_1_t é {} E var_2_f {} o resultado é {}'.format(var_1_t,var_2_f,var_1_t and var_2_f))
print('quando var_1_f é {} E var_2_f {} o resultado é {}'.format(var_1_f,var_2_f,var_1_f and var_2_f))

'''
construindo logica do or (OU)
'''

print('quando var_1_t é {} OU var_2_t {} o resultado é {}'.format(var_1_t,var_2_t,var_1_t or var_2_t))
print('quando var_1_f é {} OU var_2_t {} o resultado é {}'.format(var_1_f,var_2_t,var_1_f or var_2_t))
print('quando var_1_t é {} OU var_2_f {} o resultado é {}'.format(var_1_t,var_2_f,var_1_t or var_2_f))
print('quando var_1_f é {} OU var_2_f {} o resultado é {}'.format(var_1_f,var_2_f,var_1_f or var_2_f))

'''
multiplas regras de logica
'''

var_1_t = True
var_1_f = False
var_2_t = True
var_2_f = False

var_resultado = ((var_1_t and var_2_f) or ((var_1_f or var_2_t) and (not var_2_f)))
print('O resultado da logica é {}'.format(var_resultado))


A = False
B = False
regra = ((not A) and B) or ((not B) and A)
print(A, B, regra)

A = False
B = True
regra = ((not A) and B) or ((not B) and A)
print(A, B, regra)

A = True
B = False
regra = ((not A) and B) or ((not B) and A)
print(A, B, regra)

A = True
B = True
regra = ((not A) and B) or ((not B) and A)
print(A, B, regra)

A = True
B = True
C = True
D = True
regra_d_c = ((not D) and C)
regra_a_c = not (A and (not C))
regra_b_d = B or D 
regra = (regra_a_c or regra_b_d) and regra_d_c
print(A,B,C,D, regra)

regra = ((not (A and (not C)) or (B or D)) and ((not D) and C))
print(A,B,C,D, regra)
         
regra_AC = A and (not C)
regra_BD = B or D
regra_CD = ((not D) and C)

regras = (not regra_AC or regra_BC) and regra_CD
print(A,B,C,D, regras)




regra = (not (A and (not C)) or (B or D)) and ((not D) and C)
print(A,B,C,D, regra)

valores = [True, False]
for A in valores: 
    for B in valores:
        for C in valores:
            for D in valores:
                regra_d_c = ((not D) and C)
                regra_a_c = not (A and (not C))
                regra_b_d = B or D
                regras = (regra_a_c or regra_b_d) and regra_d_c
                print(A,B,C,D, regra)











