# Get rid of null bytes
def remove_nulls(thefile):

    file_nulls = open(thefile, "r")
    x = file_nulls.read().count("\x00")
    print("there are ", x, " nulls")
    file_nulls.seek(0)
    data = file_nulls.read()

    file_nulls.close()

    file_clean = open("<name of cleaned file>", "w")
    file_clean.write(data.replace('\x00', ''))
    file_clean.close()


def locate_utf8_errors(thefile):

    with open(thefile, 'rb') as ifh:
        for i, line in enumerate(ifh, 1):
            try:
                s = line.decode('utf-8')
            except UnicodeDecodeError as err:
                print('thefile: ERROR AT LINE', i, repr(line))
                break




def main():
    file1 = "<file to examine>.csv"
    file2 = "<file to examine>.csv"

    #   remove_nulls(file1)
    locate_utf8_errors(file2)



if __name__ == '__main__':
    main()
