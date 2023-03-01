usuario_autenticado = False
usuario_admin = False

if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sitema')
else:
    print('Debes iniciar sesion')            