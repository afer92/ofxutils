#!/usr/bin/env python
from ofxutils.ofxutils import *

def main():
    def test(ofx):
        print(ofx.prettyPrint())
    def testqif(qif):
        print(qif.prettyPrint())

#    crc = 'F1C11404'
#    print(String2Cs(crc),crc)
#    for i in range(0,16):
#        teststr = '0618@%s@20100115@-225900@@@@TRESOR PUBLIC@PRLV TRESOR PUBLIC   92 IMPOT' % (i)
#        print(teststr)
#        print('10BC1466', String2Cs(teststr))
         
    test(OfxParser.parse(file('Test.ofx')))  
    print('===')
    test(OfxParser.parse(file('Test.ofc')))
    print('===')
    ofxroot = OfxRoot('OFX','OFX','object',dtserver='20100205170222',
                      bankid='77777', branchid='00777', acctid='044444B',
                      balamt=123.45, dtasof='20100201170222')
    print(ofxroot.prettyPrint())
    print('===')
    testqif(QifParser.parse('Test.qif'))  

if __name__ == '__main__': 
    main()
