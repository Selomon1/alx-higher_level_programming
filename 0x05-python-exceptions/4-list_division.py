#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            divid = my_list_1[i]/my_list_2[i]
        except ZeroDivisionError:
            print('division by 0')
            divid = 0
        except TypeError:
            print('wrong type')
            divid = 0
        except IndexError:
            print('out of range')
            divid = 0
        finally:
            new_list.append(divid)
    return new_list
