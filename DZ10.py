class GamingError(Exception):
    def _str__(self):
        return f"Ми не можем грати разом"


def check_gaming(amount_of_gaming,limit_game):
    if amount_of_gaming>limit_game:
        return " хватить"
    else:
        raise GamingError(amount_of_gaming)

gaming=120
check_gaming(gaming, 300)
