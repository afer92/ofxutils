# ofxtools
Parse ofx, ofc and qif files and utilities tools

## Installation

```bash
apt-get install libxml2-dev libxslt1-dev python-dev
```

```bash
apt-get install python-lxml
```

```bash
pip install ofxutils
```
## Get started

### Import

```
from ofxutils.ofxtools import *
```
### Parsing example

```
from ofxutils.ofxtools import *

def main():
    def test(ofx):
        print(ofx.prettyPrint())
    def testqif(qif):
        print(qif.prettyPrint())

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
```

## Classes

### class OfxProperty(object)

#### Methods

```
    def __init__(self, name, value, pptytype, liste=False, enum=None, enumArgs=None, *args, **kwds)
    def __str__(self)
    def prettyPrint(self, level=0, tab=1)
    def get_values2db(self, enum)
    ...
```

#### Properties

```
    valid = property(get_valid, None, None, None)
    string = property(get_string, None, None, None)
    pptyName = property(get_pptyName, None, None, None)
    pptyType = property(get_pptyType, None, None, None)
    properties = property(get_properties, set_properties, del_properties, "properties's docstring")
    items = property(get_items, set_items, None, "items's docstring")
```

### class Status(OfxProperty)

#### Properties

```
    code = property(get_code, set_code, del_code, "code's docstring")
    severity = property(get_severity, set_severity, del_severity, "severity's docstring")
    severity_valid = property(get_severity_valid, None, None, "severity's docstring")
```

### class SignonResponse(OfxProperty)

#### Properties

```
    status = property(get_status, set_status, del_status, "status's docstring")
    dtserver = property(get_dtserver, set_dtserver, del_dtserver, "dtserver's docstring")
    language = property(get_language, set_language, del_language, "file's language")
    language_valid = property(get_language_valid, None, None, "file's language validity")
    dtprofup = property(get_dtprofup, set_dtprofup, del_dtprofup, "dtprofup's docstring")
    dtacctup = property(get_dtacctup, set_dtacctup, del_dtacctup, "dtacctup's docstring")
```

### class StatementTransactionResponse(OfxProperty)

#### Properties

```
    status = property(get_status, set_status, del_status, "status's docstring")
    trnuid = property(get_trnuid, set_trnuid, del_trnuid, "trnuid's docstring")
    stmtrs = property(get_stmtrs, set_stmtrs, del_stmtrs, "stmtrs's docstring")
```

### class StatementResponse(OfxProperty)

#### Properties

```
    availbal = property(get_availbal, set_availbal, del_availbal, "availbal's docstring")
    bankacctfrom = property(get_bankacctfrom, set_bankacctfrom, del_bankacctfrom, "bankacctfrom's docstring")
    banktranlist = property(get_banktranlist, set_banktranlist, del_banktranlist, "banktranlist's docstring")
    curdef = property(get_curdef, set_curdef, del_curdef, "curdef's docstring")
    curdef_valid = property(get_curdef_valid, None, None, "curdef's docstring")
    ledgerbal = property(get_ledgerbal, set_ledgerbal, del_ledgerbal, "ledgerbal's docstring")
```

### BankAccount(OfxProperty)

#### Properties

```
    acctid = property(get_acctid, set_acctid, del_acctid, "acctid's docstring")
    acctkey = property(get_acctkey, set_acctkey, del_acctkey, "acctkey's docstring")
    accttype = property(get_accttype, set_accttype, del_accttype, "accttype's docstring")
    bankid = property(get_bankid, set_bankid, del_bankid, "bankid's docstring")
    branchid = property(get_branchid, set_branchid, del_branchid, "branchid's docstring")
```

### Bal(OfxProperty)

#### Properties

```
    balamt = property(get_balamt, set_balamt, del_balamt, "balamt's docstring")
    dtasof = property(get_dtasof, set_dtasof, del_dtasof, "dtasof's docstring")
```

### class StatementTransaction(OfxProperty)

#### Properties

```
    checknum = property(get_checknum, set_checknum, del_checknum, "checknum's docstring")
    dtavail = property(get_dtavail, set_dtavail, del_dtavail, "dtavail's docstring")
    dtposted = property(get_dtposted, set_dtposted, del_dtposted, "dtposted's docstring")
    dtuser = property(get_dtuser, set_dtuser, del_dtuser, "dtuser's docstring")
    fitid = property(get_fitid, set_fitid, del_fitid, "fitid's docstring")
    name = property(get_name, set_name, del_name, "memo's docstring")
    memo = property(get_memo, set_memo, del_memo, "memo's docstring")
    namepayee = property(get_namepayee, set_namepayee, del_namepayee, "namepayee's docstring")
    payeeid = property(get_payeeid, set_payeeid, del_payeeid, "payeeid's docstring")
    refnum = property(get_refnum, set_refnum, del_refnum, "refnum's docstring")
    sic = property(get_sic, set_sic, del_sic, "sic's docstring")
    srvrtid = property(get_srvrtid, set_srvrtid, del_srvrtid, "srvrtid's docstring")
    trnamt = property(get_trnamt, set_trnamt, del_trnamt, "trnamt's docstring")
    trntype = property(get_trntype, set_trntype, del_trntype, "trntype's docstring")
```

### class BankTranList(OfxProperty)

#### Properties

```
    dtstart = property(get_dtstart, set_dtstart, del_dtstart, "dtstart's docstring")
    dtend = property(get_dtend, set_dtend, del_dtend, "dtend's docstring")
```

### class OfxRoot(OfxProperty)

#### Properties

```
    signonmsgsrsv1 = property(get_signonmsgsrsv1, set_signonmsgsrsv1, del_signonmsgsrsv1, "signonmsgsrsv1's docstring")
    bankmsgsrsv1 = property(get_bankmsgsrsv1, set_bankmsgsrsv1, del_bankmsgsrsv1, "bankmsgsrsv1's docstring")
```

### class SignonMsg(OfxProperty)

#### Properties

```
    sonrs = property(get_sonrs, set_sonrs, del_sonrs, "sonrs's docstring")
```

### BankMsg(OfxProperty)

#### Properties

```
    stmttrnrs = property(get_stmttrnrs, set_stmttrnrs, del_stmttrnrs, "stmttrnrs's docstring")
```

### class OfxParser(object)

#### Methods

```
    def load_property(cls, name, entity)
    def parse(cls_, file_handle)
    def parseSignonResponse(cls_, signon_ofx)
    def parseStatementTransactionResponse(cls_, bankmsg_ofx)
    def parseStatementResponse(cls_,stmtrs_tag)
```

### QifParser(object)

#### Methods

```
    def parse(cls_, stream, bankid='bankid', branchid='branchid',
              acctid='acctid', accttype='CHECKING')
```
    
    
   
