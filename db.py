
def save_to_file(txt, date, name = 'SSN_prognozy.txt', long = True):
    if long:
        _msg = "wartość czynników:"
    else:
        _msg = "wartość czynników (tylko predyspozycja):"
    massage = ("{0} {1} \t {2} \n".format(_msg, date, txt))
    with open(name, 'a') as file:
        file.write(massage)


if __name__ == "__main__":
    save_to_file('some text..', [2,4,5,6,7,3,7,3])
    save_to_file('some text.. short', [2,4,5,6,7,3], long = False)