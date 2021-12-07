#!/usr/bin/python3
def list_division(list_1, list_2, list_len):
    i, res_list = 0, []
    while i < list_len:
        try:
            res = list_1[i] / list_2[i]
        except (ValueError, TypeError):
            res = 0
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            i += 1
            res_list.append(res)
    return res_list
