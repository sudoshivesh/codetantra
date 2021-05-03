#WAP that inverts a dictionary. 
#That is, it makes key of one dictionary value of another and vice versa. 

key=inputI"Enter elements seperated by ,(comma) for keys: ").split(',')
value=inputI"Enter elements seperated by ,(comma) for values ").split(',')
zip_iterator=zip(key,value)
my_dict=dict(zip_iterator)
print("Dict : ",my_dict)
inverted_dict={value: key for key,value in my_dict.items()}
print("Inverted Dict :",inverted_dict)
