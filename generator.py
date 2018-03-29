from random import uniform


def Generate(name, type, price=300):
    # Read in the file
    with open(type+'.txt', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('{{ name }}', name)
    filedata = filedata.replace('{{ type }}', type)

    filedata = filedata.replace('{{ review1 }}', str(uniform(8, 10)))
    filedata = filedata.replace('{{ review2 }}', str(uniform(8, 10)))
    filedata = filedata.replace('{{ review3 }}', str(uniform(8, 10)))
    filedata = filedata.replace('{{ review4 }}', str(uniform(8, 10)))
    filedata = filedata.replace('{{ review5 }}', str(uniform(8, 10)))

    filedata = filedata.replace('{{ priceHigh }}', str(uniform(price + 8, price + 10)))
    filedata = filedata.replace('{{ priceLow }}', str(uniform(price - 8, price - 10)))

    return filedata


print(Generate('Sony Experia', 'mobile'))
