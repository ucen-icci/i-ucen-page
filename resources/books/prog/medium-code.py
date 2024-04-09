version = 2.0
# variable defined
if version == 2.0:
    print("Version ok!")
# version = 2.0 print this
elif version < 1.7:
    print("NOoOoOoOOoO")
# version < 1.7 print this
elif version < 2.0:
    print("Version not ok!")
# version < 2.0 print this LOOK THE ORDER
else:
    print("version not found ")
# exclusion print this
mensaje = "good version" if version == 2.0 else "bad version"
# better sintax for if & else. //
print(mensaje)
#
a01 = False
a02 = True
a03 = 2.0
if not a01 and (a02 or a03 == 2.0):
    print("done!")
# and = multiples variable / # or = uno of two / # not = cancel this
vod = 1.7
if vod >= 1.5 and vod <= 6.5:
    print("you got it")
# best way for this!!!!! #
if 15 <= vod <= 65:
    print("YOU GOT IT AND BETTER")
# more efficient way
for numero in range(5):
    print(numero)
