def packer(**kwargs):
    print(kwargs)

def unpacker(first_name= None, last_name=None):
    if first_name and  last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name!")

packer(name='Kenneth', num=42, spanishinquisition = None)
unpacker(**{"last_name":"love", "first_name":"kenneth"})
