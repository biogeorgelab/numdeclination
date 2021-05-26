from .cases import *

class NumDeclination:
    print("Добро пожаловать в NumDeclination! Данный модуль поможет вам со склонением слов по числу.")

    @staticmethod
    def declinate(number, words: list, type: int = 1):
        if 0 >= type or type > 6:
            raise ValueError("Тип должен быть от 1 до 5.")

        if not isinstance(number, (int, float)) or isinstance(number, bool):
            raise ValueError('Указанное вами число не является int или float.')

        number2 = int(number)
        
        string = str(number2)
        last_digits = string[-2:]

        cases_dict = {
            1: [Nominative, Genitive, Genitive],
            2: [Genitive, Genitive, Genitive],
            3: [Dative, Dative, Dative],
            4: [Instrumental, Instrumental, Instrumental],
            5: [Prepositional, Prepositional, Prepositional],
        }

        cases = cases_dict[type]
        case = ConvertedNumber()
        case.number = number
        if last_digits[0] == '1' and len(last_digits) == 2:
            case.word = words[2]
            case.case = cases_dict[type][2]
            case.case.singular = False
        else:
            if len(last_digits) == 1:
                ld = last_digits[0]
            else:
                ld = last_digits[1]
            if int(ld) == 1:
                case.word = words[0]
                case.case = cases_dict[type][0]
            elif int(ld) in [2, 3, 4]:
                case.word = words[1]
                case.case = cases_dict[type][1]
            else:
                case.word = words[2]
                case.case = cases_dict[type][2]
                case.case.singular = False

        return case
            