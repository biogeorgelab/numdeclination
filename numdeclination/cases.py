class Nominative(object):
    name = "именительный"
    singular = True

class Genitive(object):
    name = "родительный"
    singular = True

class Dative(object):
    name = "дательный"
    singular = True

class Accusative(object):
    name = "винительный"
    singular = True

class Instrumental(object):
    name = "творительный"
    singular = True
    
class Prepositional(object):
    name = "предложный"
    singular = True


class ConvertedNumber(object):
    number = 0
    case = None
    word = ''