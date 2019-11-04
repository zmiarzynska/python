def flatten(sequence):
    lista=[]
    for item in sequence:

        if isinstance(item,(list,tuple)):

            lista+=flatten(item)
        else:
            lista.append(item)
    return lista


sekwencja=[1,(2,3),[],[4,(5,6,7)]]

print(flatten(sekwencja))

