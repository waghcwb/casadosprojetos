# somente esqueleto para futuras funções
# após a compra do host, definimos o melhor banco de dados
class Users():
    error = None

    @classmethod
    def new_user(cls, first_name, last_name, email, password, group='admin', avatar='default.png'):

        try:
            print('new_user')

        except Exception as e:
            if e.args[0] == 1062:
                cls.error = 'Usuário já existe'
                return False
            cls.error = e.args[1]
            return False
        else:
            return True

    @staticmethod
    def is_activate(email):
        resp = []
        if resp[0]:
            return True
        return False

    @classmethod
    def is_logged(cls, email, password):
        resp = []
        if not resp:
            cls.error = 'Usuário com esse email não existe'
            return False
        if resp:
            return True
        cls.error = 'Usuário ou senha incorretos'
        return False

    @staticmethod
    def set_activate(email):
        try:
            print('UPDATE users SET activated=%s WHERE email=%s')
        except Exception as e:
            print(e)
        return None

    @staticmethod
    def get_user_name(email):
        return True

    @staticmethod
    def get_user_id(email):
        resp = []
        if resp:
            return resp[0]
        return
