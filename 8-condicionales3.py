#operadores and y or
usuario_logeado =True
usuario_admin = True
if usuario_logeado and usuario_admin:
    print('Administrador')
elif usuario_logeado:
    print('Acceso al sistema')
else:
    print('Debes iniciar secion')
