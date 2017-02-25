# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
'''

class Enum emulates Enumerations.

Enum instances contain _EnumNodes. These have two attributes:
asString and asInt.

Create one with

    Enum(list,*startvalue)
or: Enum(string,*startvalue)       (default for startvalue is 0)

e.g.:

WD = Enum(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], 1)
WD = Enum["Monday Tuesday Wednesday Thursday Friday Saturday Sunday", 1]

Typical use:

workdays = WD.irange(WD.Monday,WD.Friday)    # inclusive ranges are better
                                             # for Enums, hence "irange"
                                             # equivalent: workdays = WD[1:6]
for i in WD.each():
    if i in workdays:
        print i.asInt, i.asString + " is a work day"
    else:
        print i.asInt, i.asString + " is a weekend day."
print "There are ", len(WD), "days per week"
if "Monday" in WD: print "Monday is a valid name"
if not "August" in WD: print "August is not"

some systematic examples:

WD.Monday.asString       -->; 'Monday'
WD.Monday.asInt          -->; 1
WD.stringToInt('Monday') -->; 1
WD[2].asString           -->; 'Tuesday'
WD.intToString(2)        -->; 'Tuesday'
WD["Tuesday"].asInt      -->; 2
WD.Saturday > WD.Tuesday -->; 1
"Monday" in WD -->; 1
6 in WD -->; 1
0 in WD -->; 0
WD.each() gives you a list of all EnumNodes.
WD.eachString() -->; find out by yourself!

Note: You cannot create EnumNodes other than creating an Enum.
      The EnumNode class is considered private.
      Never not try to change attributes of these objects.
'''

################################################################

import types

class _EnumNode:
    def __init__(self,i,name):
        self.asInt=i
        self.asString=name

#    def __cmp__(self,left,right):
#        return cmp(left.asInt, right.asInt)

    def __str__(self):
        return self.asString

    def __repr__(self):
        return '('+str(self.asInt)+':'+self.asString+')'

    def __hash__(self):
        return self.asInt

class Enum:
    def __init__(self,stringList,start=0):
        if type(stringList)==types.StringType:
            stringList = stringList.split()
        self._start = start
        self._byString = {}
        self._byInt = [ None ] * (start + len(stringList))
        for i in range(len(stringList)):
            node = _EnumNode(i+start,stringList[i])
            setattr(self, stringList[i], node)
            self._byInt[i+start] = node
            self._byString[node.asString] = node

    def addAlternate(self,node,aString): # note: doesn't update '_byInt'
        self._byString[aString] = node

    def intToString(self,num):
        return self._byInt[num].asString

    def stringToInt(self,name):
        node = self._byString.get(name,None)
        if node: return node.asInt
        else: return None

    def __contains__(self,key):
        if type(key)==types.IntType:
            return key >= self._start # removed 'and key' (didn't allow a 0 start value)
        else: # else needed for strings
            return key in self._byString

    # missing methods...

    def __len__(self):
        return len(self._byInt)-self._start

    def __getitem__(self,key):
        if type(key)==types.StringType:
            return self._byString[key]
        else:
            return self._byInt[key]

    def irange(self, begin, end):
        return [self._byInt[i] for i in range(begin.asInt, end.asInt+1)]

    def each(self):
        return [node for node in self._byInt if node is not None]

    def eachString(self):
        return [node.asString for node in self.each()]


if __name__ == '__main__':
    # Typical use:

    WD = Enum('Monday Tuesday Wednesday Thursday Friday Saturday Sunday', 1)

    workdays = WD.irange(WD.Monday,WD.Friday)    # inclusive ranges are better
                                                 # for Enums, hence 'irange'
                                                 # equivalent: workdays = WD[1:6]
    print 'workdays: ', workdays
    print 'WD[1:6]: ', WD[1:6]
    for i in WD.each():
        if i in workdays:
            print i.asInt, i.asString + ' is a work day'
        else:
            print i.asInt, i.asString + ' is a weekend day.'

    print 'There are', len(WD), 'days per week'
    if 'Monday' in WD: print 'Monday is a valid name'
    if not 'August' in WD: print 'August is not'

    # some systematic examples:

    print 'WD.Monday.asString:', WD.Monday.asString
    print 'WD.Monday.asInt:', WD.Monday.asInt
    print "WD.stringToInt('Monday'):", WD.stringToInt('Monday')
    print 'WD[2].asString:', WD[2].asString
    print 'WD.intToString(2):', WD.intToString(2)
    print "WD['Tuesday'].asInt:", WD['Tuesday'].asInt
    print 'WD.Saturday > WD.Tuesday:', WD.Saturday > WD.Tuesday
    print "'Monday' in WD:", 'Monday' in WD
    print '6 in WD:', 6 in WD
    print '0 in WD:', 0 in WD
    print 'WD.each():', WD.each()
    print 'WD.eachString():', WD.eachString()
