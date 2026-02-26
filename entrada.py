usuario = input(' digite seu nome\n')
sobrenome = input('digite seu sobrenome\n')
nascimento = input('data de nascimento\n')
universidade = input('universidade\n')
email = str(usuario.lower() + '.' + sobrenome.lower() + '@' + universidade.lower() + '.br')
print(email)
a_c = email.count('a')
e_c = email.count('e')
i_c = email.count('i')
o_c = email.count('o')
u_c = email.count('u')
senha = 'a' + str(a_c) + 'e' + str(e_c) + 'i' + str(i_c) + 'o' + str(o_c) + 'u' + str(u_c)
print('o seu email é: {}'.format(e_mail))
print('a seua senha é: {}'.format(senha))
print('a sua senha e e-mail são: {}:{}'.format(senha,e-mail))



var_str_problematica - '  MELANCIA      '
var_str_espaco = var_str_problematica.strip()
print(var_str_problematica)
print(var_str_sem_espaco) 

