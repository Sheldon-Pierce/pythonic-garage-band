class Musician:
    def __init__(self):
        self.instrument = None
        self.name = None

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'


class Band:

    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        new_list = []
        for i in self.members:
            new_list.append(i.play_solo())
        return new_list

    @classmethod
    def to_list(cls):
        # all_bands = []
        return cls.instances


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = 'guitar'

    def __repr__(self):
        return f'{__class__.__name__} instance. Name = {self.name}'

    @staticmethod
    def get_instrument():
        return "guitar"

    @staticmethod
    def play_solo():
        return 'face melting guitar solo'


class Bassist(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = 'bass'

    def __repr__(self):
        return f'{__class__.__name__} instance. Name = {self.name}'

    @staticmethod
    def get_instrument():
        return "bass"

    @staticmethod
    def play_solo():
        return 'bom bom buh bom'


class Drummer(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = 'drums'

    def __repr__(self):
        return f'{__class__.__name__} instance. Name = {self.name}'

    @staticmethod
    def get_instrument():
        return "drums"

    @staticmethod
    def play_solo():
        return 'rattle boom crash'


if __name__ == '__main__':
    pass
