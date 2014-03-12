__author__ = 'Apollo117'
import SpiceyPy as spice
import ctypes
testArray = [-11,0,22,750]

print(spice.stypes.listtointvector(testArray))

print(spice.bsrchi(-11, 4, testArray))
print(spice.bsrchi(22, 4, testArray))
print(spice.bsrchi(751, 4, testArray))
print(spice.bsrchi(750, 4, testArray))


testArray = [-11.0,0.0,22.0,750.0]

print(spice.bsrchd(-11.0, 4, testArray))
print(spice.bsrchd(22.0, 4, testArray))
print(spice.bsrchd(751.0, 4, testArray))
print(spice.bsrchd(750.0, 4, testArray))

print("Test BSRCHC")
testCharArray = ["BOHR", "EINSTEIN", "FEYNMAN", "GALILEO", "NEWTON"]


testar = spice.stypes.listtocharvector(testCharArray)
print(testar)
print(testar)
print([x for x in testar])
newtest = ((ctypes.c_char * 10)*3)
print(newtest)

print(spice.stypes.listtosmartstrarray(testCharArray))





# print([x for x in testCharArray])
# print(spice.bsrchc("BOHR", 5, 10, testCharArray))
#
# print("Test shellc")
# print(spice.shellc(6, 8, testCharArray))
#
# print("test bschoi")
# testArray = [100,1,10,10000,1000]
# order =[1,2,0,4,3]
# print(spice.bschoi(1000, 5, testArray, order))
# print("")
# print(spice.brckti(-1,1,10))
# print(spice.brckti(29,1,10))
# print(spice.brckti(3,-10,10))
# print(spice.brckti(3,-10,-1))