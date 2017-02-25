#!/usr/bin/python
# -*- coding: utf-8 -*-

__version__ = '0.9.012'
__author__  = 'Alain Ferraro'
__date__    = '2010-02-20'


from BeautifulSoup import BeautifulStoneSoup
from enumerator import Enum
import time, datetime, decimal
import zlib

LanguageEnum = Enum(['AAR','ABK','ACE','ACH','ADA','AFA','AFH','AFR','AKA','AKK','ALB','ALE','ALG','AMH',
            'ANG','APA','ARA','ARC','ARG','ARM','ARN','ARP','ART','ARW','ASM','AST','ATH','AUS',
            'AVA','AVE','AWA','AYM','AZE','BAD','BAI','BAK','BAL','BAM','BAN','BAQ','BAS','BAT',
            'BEJ','BEL','BEM','BEN','BER','BHO','BIH','BIK','BIN','BIS','BLA','BNT','BOS','BRA',
            'BRE','BTK','BUA','BUG','BUL','BUR','CAD','CAI','CAR','CAT','CAU','CEB','CEL','CHA',
            'CHB','CHE','CHG','CHI','CHK','CHM','CHN','CHO','CHP','CHR','CHU','CHV','CHY','CMC',
            'COP','COR','COS','CPE','CPF','CPP','CRE','CRP','CUS','CZE','DAK','DAN','DAR','DAY',
            'DEL','DEN','DGR','DIN','DIV','DOI','DRA','DUA','DUM','DUT','DYU','DZO','EFI','EGY',
            'EKA','ELX','ENG','ENM','EPO','EST','EWE','EWO','FAN','FAO','FAT','FIJ','FIN','FIU',
            'FON','FRE','FRM','FRO','FRY','FUL','FUR','GAA','GAY','GBA','GEM','GEO','GER','GEZ',
            'GIL','GLA','GLE','GLG','GLV','GMH','GOH','GON','GOR','GOT','GRB','GRC','GRE','GRN',
            'GUJ','GWI','HAI','HAU','HAW','HEB','HER','HIL','HIM','HIN','HIT','HMN','HMO','HUN',
            'HUP','IBA','IBO','ICE','IDO','III','IJO','IKU','ILE','ILO','INA','INC','IND','INE',
            'INH','IPK','IRA','IRO','ITA','JAV','JPN','JPR','JRB','KAA','KAB','KAC','KAL','KAM',
            'KAN','KAR','KAS','KAU','KAW','KAZ','KBD','KHA','KHI','KHM','KHO','KIK','KIN',
            'KIR','KMB','KOK','KOM','KON','KOR','KOS','KPE','KRO','KRU','KUA','KUM','KUR',
            'KUT','LAD','LAH','LAM','LAO','LAT','LAV','LEZ','LIM','LIN','LIT','LOL','LOZ',
            'LTZ','LUA','LUB','LUG','LUI','LUN','LUO','LUS','MAC','MAD','MAG','MAH','MAI',
            'MAK','MAL','MAN','MAO','MAP','MAR','MAS','MAY','MDR','MEN','MGA','MIC','MIN',
            'MIS','MKH','MLG','MLT','MNC','MNI','MNO','MOH','MOL','MON','MOS','MUL','MUN',
            'MUS','MWR','MYN','NAH','NAI','NAP','NAU','NAV','NBL','NDE','NDO','NDS','NEP',
            'NEW','NIA','NIC','NIU','NNO','NOB','NON','NOR','NSO','NUB','NYA','NYM','NYN',
            'NYO','NZI','OCI','OJI','ORI','ORM','OSA','OSS','OTA','OTO','PAA','PAG','PAL',
            'PAM','PAN','PAP','PAU','PEO','PER','PHI','PHN','PLI','POL','PON','POR','PRA',
            'PRO','PUS','QAA','QUE','RAJ','RAP','RAR','ROA','ROH','ROM','RUM','RUN','RUS',
            'SAD','SAG','SAH','SAI','SAL','SAM','SAN','SAS','SAT','SCC','SCO','SCR','SEL',
            'SEM','SGA','SGN','SHN','SID','SIN','SIO','SIT','SLA','SLO','SLV','SMA','SME',
            'SMI','SMJ','SMN','SMO','SMS','SNA','SND','SNK','SOG','SOM','SON','SOT','SPA',
            'SRD','SRR','SSA','SSW','SUK','SUN','SUS','SUX','SWA','SWE','SYR','TAH','TAI',
            'TAM','TAT','TEL','TEM','TER','TET','TGK','TGL','THA','TIB','TIG','TIR','TIV',
            'TKL','TLI','TMH','TOG','TON','TPI','TSI','TSN','TSO','TUK','TUM','TUP','TUR',
            'TUT','TVL','TWI','TYV','UGA','UIG','UKR','UMB','UND','URD','UZB','VAI','VEN',
            'VIE','VOL','VOT','WAK','WAL','WAR','WAS','WEL','WEN','WLN','WOL','XHO','YAO',
            'YAP','YID','YOR','YPK','ZAP','ZEN','ZHA','ZND','ZUL','ZUN'])
 
CurrencyEnum = Enum(['AED','AFA','ALL','AMD','ANG','AOA','ARS','AUD','AWG','AZM','BAM','BBD','BDT','BGL','BHD',
            'BIF','BMD','BND','BOB','BRL','BSD','BTN','BWP','BYR','BZD','CAD','CDF','CHF','CLP','CNY',
            'COP','CRC','CUP','CVE','CYP','CZK','DJF','DKK','DOP','DZD','EEK','EGP','ERN','ETB','EUR',
            'FJD','FKP','GBP','GEL','GGP','GHC','GIP','GMD','GNF','GTQ','GYD','HKD','HNL','HRK','HTG',
            'HUF','IDR','ILS','IMP','INR','IQD','IRR','ISK','JEP','JMD','JOD','JPY','KES','KGS','KHR',
            'KMF','KPW','KRW','KWD','KYD','KZT','LAK','LBP','LKR','LRD','LSL','LTL','LVL','LYD','MAD',
            'MDL','MGF','MKD','MMK','MNT','MOP','MRO','MTL','MUR','MVR','MWK','MXN','MYR','MZM','NAD',
            'NGN','NIO','NOK','NPR','NZD','OMR','PAB','PEN','PGK','PHP','PKR','PLN','PYG','QAR','ROL',
            'RUR','RWF','SAR','SBD','SCR','SDD','SEK','SGD','SHP','SIT','SKK','SLL','SOS','SPL','SRG',
            'STD','SVC','SYP','SZL','THB','TJS','TMM','TND','TOP','TRL','TTD','TVD','TWD','TZS','UAH',
            'UGX','USD','UYU','UZS','VEB','VND','VUV','WST','XAF','XAG','XAU','XCD','XDR','XOF','XPD',
            'XPF','XPT','YER','YUM','ZAR','ZMK','ZWD'])

TransactionEnum = Enum(['ATM','CASH','CHECK','CREDIT','DEBIT','DEP',
                        'DIRECTDEBIT','DIRECTDEP','DIV','FEE','INT',
                        'OTHER','PAYMENT','POS','REPEATPMT','SRVCHG','XFER'
                        ])
 
SeverityEnum = Enum(['INFO','WARN','ERROR']) 

def DoChecksum(Adler32, data):
    #return zlib.adler32(data,65521)
    base = 65521
    s1 = Adler32 & 0xFFFF
    s2 = Adler32 / 0x10000
    for c in data:
        s1 = (s1 + ord(c)) % base
        s2 = (s1 + s2) % base
    result = s2 * 0x10000 + s1
    return result

def String2Cs(value):
    crc = 0xFFFFFFFF;
    crc = DoChecksum(crc, value)
    
    result = '%x' % (crc)

    return result.upper()
 
class Ofx(object):
    pass
 
class OfxProperty(object):
    def __init__(self, name, value, pptytype, liste=False, enum=None, enumArgs=None, *args, **kwds):
        self._valid = True
        self._liste = liste
        self._items = []
        self._pptyName = name
        self._pptyType = pptytype
        self._enumArgs = enumArgs
        if isinstance(value,datetime.datetime):
            self._value = value
            self._string = self._value.strftime('%Y%m%d%H%m%S')
#        elif isinstance(value,datetime):
#            self._value = value
#            self._string = self._value.strftime('%Y%m%d%H%m%S')
        elif isinstance(value,time.struct_time):
            self._value = value
            self._string = time.strftime('%Y%m%d%H%m%S',self._value)
        elif isinstance(value,datetime.date):
            self._value = value
            self._string = self._value.strftime('%Y%m%d')
        elif isinstance(value,float):
            self._value = value
            self._string = str(value)
        elif isinstance(value,decimal.Decimal):
            self._value = value
            self._string = str(value)
        elif isinstance(value,int):
            self._value = value
            self._string = str(value)
        elif isinstance(value,OfxProperty):
            self._value = value
            self._string = str(value)
        else:
            self._string = value.strip()
            self._value = self._string
        self._properties = {} # name, property
        if pptytype == 'int':
            if isinstance(value,int):
                pass
            else:
                if value:
                    try:
                        self._value = int(self._string)
                    except ValueError:
                        self._value = 0
                        self._valid = False
                else:
                    self._value = 0
        elif pptytype == 'date':
            if isinstance(value,datetime.datetime):
                pass
            else:
                tempstr = self._string.replace('-','')
                tempstr = tempstr.replace(':','')
                tempstr = tempstr.replace('T','')
                tempstr = tempstr.replace(' ','')
                if len(tempstr)==8 :
                    try :
                        self._value = time.strptime(tempstr, "%Y%m%d")
                    except ValueError:
                        self._valid = False
                elif len(tempstr)==14 :
                    try :
                        self._value = time.strptime(tempstr, "%Y%m%d%H%M%S")
                    except ValueError:
                        self._valid = False
                else:
                    self._value = time.localtime()
                    self._valid = False
        elif pptytype == 'float':
            if isinstance(value,float):
                pass
            elif isinstance(value,int):
                pass
            elif isinstance(value,decimal.Decimal):
                pass
            else:
                try :
                    self._value = float(value.strip())
                except ValueError:
                    self._value = 0
                    self._valid = False
        else:
            if self.pptyType == 'object':
                self._value = value
            else:
                if isinstance(self._value,str):
                    self._value = value.strip()
                else:
                    self._value = value
        if enum:
            if not(self._string in enum):
                self._valid = False
        self._pptyType = pptytype
        self._type = pptytype
        
    def norm_first(self, *args, **kwds):
        pass
        
    def norm_last(self, *args, **kwds):
        pass

        
    def __str__(self):
        return self._string
        
    def prettyPrint(self, level=0, tab=1):
        if level>0:
            result = ''.rjust(level*tab)
        else:
            result = ''
        if self._type=='object':
            result += "<%s>" % (self._string.upper())
        else:
            if self._string:
                result += "<%s>%s</%s>" % (self._pptyName.upper(),self._string,self._pptyName.upper())
            else:
                result += "<%s />" % (self._pptyName.upper())
            #print(type(self._string), self._string)
        if self._enumArgs:
            for pptyName in self._enumArgs:
                if self._properties.has_key(pptyName.asString):
                    ppty = self._properties[pptyName.asString]
                    if ppty:
                        result = result + '\n' + ppty.prettyPrint(level+1, tab)
                        if not(ppty.valid):
                            result = result + '(not valid)'
        if self._liste:
            for item in self._items:
                result = result + '\n' + item.prettyPrint(level+1, tab)
        if self._type=='object':
            result += "\n%s</%s>" % (''.rjust(level*tab),self._string.upper())
        return result
    
    def get_values2db(self, enum):
        result = {}
        for propname, prop in self._properties.iteritems():
            if propname in enum:
                value = prop.string
                value = value.replace( u'œ', 'oe') 
                value = value.replace("'", "''")
                if prop.pptyType == 'object':
                    pass
                elif prop.pptyType == 'date':
                    if isinstance(prop._value,datetime.datetime):
                        value = prop._value.strftime('%Y%m%d%H%m%S')
                    else:
                        value = time.strftime('%Y%m%d%H%m%S',prop._value)
                    result[propname] = value
                elif prop.pptyType == 'string':
                    result[propname] = "'%s'" % (value)
                else:
                    result[propname] = "%s" % (value)
        return result  

    def get_items(self):
        return self._items

    def get_pptyName(self):
        return self._pptyName

    def get_properties(self):
        return self._properties

    def get_pptyType(self):
        return self._pptyType

    def get_string(self):
        return self._string

    def GetValue(self):
        return self._value

    def get_valid(self):
        return self._valid

    def set_items(self, value):
        self._items = value

    def set_properties(self, value):
        self._properties = value

    def del_properties(self):
        del self._properties

    valid = property(get_valid, None, None, None)
    string = property(get_string, None, None, None)
    pptyName = property(get_pptyName, None, None, None)
    pptyType = property(get_pptyType, None, None, None)
    properties = property(get_properties, set_properties, del_properties, "properties's docstring")
    items = property(get_items, set_items, None, "items's docstring")

class Status(OfxProperty):
    def __init__(self, name, value, type, code=None, severity=None):
        self._enumArgs = Enum(['code','severity'])
        OfxProperty.__init__(self, name, value, type, enumArgs=self._enumArgs)        
        if not(code):
            code = 0
        self.code = OfxProperty('code',code,'int')       
        if not(severity):
            severity = 'INFO'
        self.severity = OfxProperty('severity',severity,'string')

    def get_code(self):
        return self._code


    def get_severity(self):
        return self._severity

    def get_severity_valid(self):
        return self._severity._valid


    def set_code(self, value):
        self._code = OfxProperty('code',value,'int')
        self._properties['code'] = self._code


    def set_severity(self, value):
        self._severity = OfxProperty('severity',value,'string',enum=SeverityEnum)
        self._properties['severity'] = self._severity


    def del_code(self):
        del self._code


    def del_severity(self):
        del self._severity

    code = property(get_code, set_code, del_code, "code's docstring")
    severity = property(get_severity, set_severity, del_severity, "severity's docstring")
    severity_valid = property(get_severity_valid, None, None, "severity's docstring")

class SignonResponse(OfxProperty):
    def __init__(self, name, value, type, dtserver=None, language=None, dtprofup=None, dtacctup=None):
        self._enumArgs = Enum(['status','dtserver','language','dtprofup','dtacctup'])
        OfxProperty.__init__(self, name, value, type, enumArgs=self._enumArgs)
        self.status = Status('status','status','object')
        if not(dtserver):
            dtserver = time.localtime()
        self.dtserver = OfxProperty('dtserver',dtserver,'date')
        if not(language):
            language = 'FRE'
        self.language = OfxProperty('language',language,'string')
        if not(dtprofup):
            dtprofup = dtserver
        self.dtprofup = OfxProperty('dtprofup',dtprofup,'date')
        if not(dtacctup):
            dtacctup = dtserver
        self.dtacctup = OfxProperty('dtacctup',dtacctup,'date')

    def get_status(self):
        return self._status


    def get_dtserver(self):
        return self._dtserver


    def get_language(self):
        return self._language

    def get_language_valid(self):
        return self._language._valid


    def get_dtprofup(self):
        return self._dtprofup


    def get_dtacctup(self):
        return self._dtacctup


    def set_status(self, value):
        self._status = value
        self._properties['status'] = self._status


    def set_dtserver(self, value):
        self._dtserver = OfxProperty('dtserver',value,'date')
        self._properties['dtserver'] = self._dtserver


    def set_language(self, value):
        self._language = OfxProperty('language',value,'string',enum=LanguageEnum)
        self._properties['language'] = self._language


    def set_dtprofup(self, value):
        self._dtprofup = OfxProperty('dtprofup',value,'date')
        self._properties['dtprofup'] = self._dtprofup


    def set_dtacctup(self, value):
        self._dtacctup = OfxProperty('dtacctup',value,'date')
        self._properties['dtacctup'] = self._dtacctup


    def del_status(self):
        del self._status


    def del_dtserver(self):
        del self._dtserver


    def del_language(self):
        del self._language


    def del_dtprofup(self):
        del self._dtprofup


    def del_dtacctup(self):
        del self._dtacctup

    status = property(get_status, set_status, del_status, "status's docstring")
    dtserver = property(get_dtserver, set_dtserver, del_dtserver, "dtserver's docstring")
    language = property(get_language, set_language, del_language, "file's language")
    language_valid = property(get_language_valid, None, None, "file's language validity")
    dtprofup = property(get_dtprofup, set_dtprofup, del_dtprofup, "dtprofup's docstring")
    dtacctup = property(get_dtacctup, set_dtacctup, del_dtacctup, "dtacctup's docstring")
 

class StatementTransactionResponse(OfxProperty):
    def __init__(self, name, value, type, 
                 bankid=None, branchid=None, acctid=None, accttype=None,
                 balamt=None, dtasof=None):
        self._enumArgs = Enum(['trnuid','status','stmtrs'])
        OfxProperty.__init__(self, name, value, type, enumArgs=self._enumArgs)
        self.status = Status('status','status','object')
        self.trnuid = OfxProperty('trnuid','00','string')
        self.stmtrs = StatementResponse('stmtrs','stmtrs','object', 
                                        bankid=bankid, branchid=branchid, acctid=acctid, accttype=accttype,
                                        balamt=balamt, dtasof=dtasof)

    def get_status(self):
        return self._status


    def get_trnuid(self):
        return self._trnuid


    def get_stmtrs(self):
        return self._stmtrs


    def set_status(self, value):
        self._status = value
        self._properties['status'] = self._status


    def set_trnuid(self, value):
        self._trnuid = OfxProperty('trnuid',value,'string')
        self._properties['trnuid'] = self._trnuid


    def set_stmtrs(self, value):
        self._stmtrs = value
        self._properties['stmtrs'] = self._stmtrs


    def del_status(self):
        del self._status


    def del_trnuid(self):
        del self._trnuid


    def del_stmtrs(self):
        del self._stmtrs

    status = property(get_status, set_status, del_status, "status's docstring")
    trnuid = property(get_trnuid, set_trnuid, del_trnuid, "trnuid's docstring")
    stmtrs = property(get_stmtrs, set_stmtrs, del_stmtrs, "stmtrs's docstring")

class StatementResponse(OfxProperty):
    def __init__(self, name, value, type, 
                 curdef=None, bankid=None, branchid=None, acctid=None, accttype=None,
                 balamt=None, dtasof=None):
        self._enumArgs = Enum(['curdef','bankacctfrom','banktranlist','ledgerbal',
                               'availbal'])
        OfxProperty.__init__(self, name, value, type, enumArgs=self._enumArgs)
        self.availbal = Bal('availbal','availbal','object',balamt=balamt,dtasof=dtasof)
        self.bankacctfrom = BankAccount('bankacctfrom','bankacctfrom','object', bankid, branchid, acctid, accttype)
        self._banktranlist = BankTranList('banktranlist','banktranlist','object')
        if not(curdef):
            curdef = 'EUR'
        self.curdef = OfxProperty('curdef',curdef,'string')
        self.ledgerbal = Bal('ledgerbal','ledgerbal','object',balamt=balamt,dtasof=dtasof)
        self._properties['banktranlist'] = self._banktranlist

    def get_availbal(self):
        return self._availbal


    def get_bankacctfrom(self):
        return self._bankacctfrom


    def get_banktranlist(self):
        return self._banktranlist


    def get_curdef(self):
        return self._curdef._value
    
    def get_curdef_valid(self):
        return self._curdef._valid


    def get_ledgerbal(self):
        return self._ledgerbal


    def set_availbal(self, value):
        self._availbal = value
        self._properties['availbal'] = self._availbal


    def set_bankacctfrom(self, value):
        self._bankacctfrom = value
        self._properties['bankacctfrom'] = self._bankacctfrom


    def set_banktranlist(self, value):
        self._banktranlist = value
        self._properties['banktranlist'] = self._banktranlist


    def set_curdef(self, value):
        self._curdef = OfxProperty('curdef',value,'string',enum=CurrencyEnum)
        self._properties['curdef'] = self._curdef


    def set_ledgerbal(self, value):
        self._ledgerbal = value
        self._properties['ledgerbal'] = self._ledgerbal


    def del_availbal(self):
        del self._availbal


    def del_bankacctfrom(self):
        del self._bankacctfrom


    def del_banktranlist(self):
        del self._banktranlist


    def del_curdef(self):
        del self._curdef


    def del_ledgerbal(self):
        del self._ledgerbal

    availbal = property(get_availbal, set_availbal, del_availbal, "availbal's docstring")
    bankacctfrom = property(get_bankacctfrom, set_bankacctfrom, del_bankacctfrom, "bankacctfrom's docstring")
    banktranlist = property(get_banktranlist, set_banktranlist, del_banktranlist, "banktranlist's docstring")
    curdef = property(get_curdef, set_curdef, del_curdef, "curdef's docstring")
    curdef_valid = property(get_curdef_valid, None, None, "curdef's docstring")
    ledgerbal = property(get_ledgerbal, set_ledgerbal, del_ledgerbal, "ledgerbal's docstring")
 
class BankAccount(OfxProperty):
    def __init__(self, name, value, type, bankid=None, branchid=None, acctid=None, accttype=None):
        self._enumArgs = Enum(['bankid','branchid','acctid','accttype','acctkey'])
        OfxProperty.__init__(self, name, value, type, enumArgs=self._enumArgs)
        if not(acctid):
            acctid = '055555A'
        self.acctid = OfxProperty('acctid',acctid,'string')
        if not(accttype):
            accttype = 'CHECKING'
        self.accttype = OfxProperty('accttype',accttype,'accttype')
        if not(bankid):
            bankid = '33333'
        self.bankid = OfxProperty('bankid',bankid,'bankid')
        if not(branchid):
            branchid = '00888'
        self.branchid = OfxProperty('branchid',branchid,'branchid')

    def get_acctid(self):
        return self._acctid


    def get_acctkey(self):
        return self._acctkey


    def get_accttype(self):
        return self._accttype


    def get_bankid(self):
        return self._bankid


    def get_branchid(self):
        return self._branchid


    def set_acctid(self, value):
        self._acctid = OfxProperty('acctid',value,'string')
        self._properties['acctid'] = self._acctid


    def set_acctkey(self, value):
        self._acctkey = OfxProperty('acctkey',value,'string')
        self._properties['acctkey'] = self._acctkey


    def set_accttype(self, value):
        self._accttype = OfxProperty('accttype',value,'string')
        self._properties['accttype'] = self._accttype


    def set_bankid(self, value):
        self._bankid = OfxProperty('bankid',value,'string')
        self._properties['bankid'] = self._bankid


    def set_branchid(self, value):
        self._branchid = OfxProperty('branchid',value,'string')
        self._properties['branchid'] = self._branchid


    def del_acctid(self):
        del self._acctid


    def del_acctkey(self):
        del self._acctkey


    def del_accttype(self):
        del self._accttype


    def del_bankid(self):
        del self._bankid


    def del_branchid(self):
        del self._branchid

    acctid = property(get_acctid, set_acctid, del_acctid, "acctid's docstring")
    acctkey = property(get_acctkey, set_acctkey, del_acctkey, "acctkey's docstring")
    accttype = property(get_accttype, set_accttype, del_accttype, "accttype's docstring")
    bankid = property(get_bankid, set_bankid, del_bankid, "bankid's docstring")
    branchid = property(get_branchid, set_branchid, del_branchid, "branchid's docstring")

class Bal(OfxProperty):
    def __init__(self, name, value, type, balamt=None, dtasof=None):
        self._enumArgs = Enum(['balamt','dtasof'])
        OfxProperty.__init__(self, name, value, type, enumArgs=self._enumArgs)
        if not(balamt):
            balamt = 0.0
        self.balamt = balamt
        if not(dtasof):
            dtasof = time.localtime()
        self.dtasof = dtasof

    def get_balamt(self):
        return self._balamt


    def get_dtasof(self):
        return self._dtasof


    def set_balamt(self, value):
        self._balamt = OfxProperty('balamt',value,'float')
        self._properties['balamt'] = self._balamt


    def set_dtasof(self, value):
        self._dtasof = OfxProperty('dtasof',value,'date')
        self._properties['dtasof'] = self._dtasof


    def del_balamt(self):
        del self._balamt


    def del_dtasof(self):
        del self._dtasof

    balamt = property(get_balamt, set_balamt, del_balamt, "balamt's docstring")
    dtasof = property(get_dtasof, set_dtasof, del_dtasof, "dtasof's docstring")
 
 
class StatementTransaction(OfxProperty):
    def __init__(self, name, value, type):
        self._enumArgs = Enum(['trntype','dtposted','dtuser','dtavail',
                               'trnamt','fitid','srvrtid','checknum',
                               'refnum','sic','payeeid','name','memo'])
        OfxProperty.__init__(self, name, value, type, enumArgs=self._enumArgs)
        self._checknum = None
        self._dtavail = None
        self._dtposted = None
        self._dtuser = None
        self._fitid = None    
        self._name = None   
        self._memo = None   
        self._namepayee = None   
        self._payeeid = None 
        self._refnum = None    
        self._sic = None      
        self._srvrtid = None    
        self._trnamt = None     
        self._trntype = None 
        
        
    def norm_first(self, *args, **kwds):
        OfxProperty.norm_first(self, *args, **kwds)
        
    def norm_last(self, *args, **kwds):
        newfitid = False
        splitFitid = None
        if self.fitid:
            oldfitid = self.fitid._string
            splitFitid = oldfitid.split(" ",2)
            if len(splitFitid)>1:
                if (splitFitid[0] != String2Cs(splitFitid[1])):
                    # calcul du fitid
                    newfitid = True
            else:
                newfitid = True
        else:
            newfitid = True
        if newfitid:
            # calcul du fitid
            if splitFitid:
                oldFITIDstart = splitFitid[0]
            else:
                oldFITIDstart = ''
            if oldFITIDstart=='':
                oldFITIDstart = "00000000"
            tmpFITID = ""
            tmpFITID = oldFITIDstart + "@"
            tmpFITID = tmpFITID + str(TransactionEnum.stringToInt(self.trntype.string)) + "@"
            if self.dtposted:
                tmpFITID = tmpFITID + self.dtposted.string
            tmpFITID = tmpFITID + "@"
            if self.trnamt:
                tmpFITID = tmpFITID + self.trnamt.string.replace(".", "")
            tmpFITID = tmpFITID + "@"
            if self.checknum:
                tmpFITID = tmpFITID + self.checknum.string
            tmpFITID = tmpFITID + "@"
            if self.refnum:
                tmpFITID = tmpFITID + self.refnum.string
            tmpFITID = tmpFITID + "@"
            if self.payeeid:
                tmpFITID = tmpFITID + self.payeeid.string
            tmpFITID = tmpFITID + "@"
            if self.name:
                tmpFITID = tmpFITID + self.name.string
            tmpFITID = tmpFITID + "@"
            if self.memo:
                tmpFITID = tmpFITID + self.memo.string
            #print(tmpFITID)
            crc = String2Cs(tmpFITID)
            newfitid = String2Cs(crc) + " " + crc + " " + oldFITIDstart + " " + self.dtposted.string + " " + self.trnamt.string.replace(".", "");
            self.fitid = newfitid
            #print(newfitid)
        OfxProperty.norm_last(self, *args, **kwds)

    def get_checknum(self):
        return self._checknum


    def get_dtavail(self):
        return self._dtavail


    def get_dtposted(self):
        return self._dtposted


    def get_dtuser(self):
        return self._dtuser


    def get_fitid(self):
        return self._fitid


    def get_name(self):
        return self._name


    def get_memo(self):
        return self._memo


    def get_namepayee(self):
        return self._namepayee


    def get_payeeid(self):
        return self._payeeid


    def get_refnum(self):
        return self._refnum


    def get_sic(self):
        return self._sic


    def get_srvrtid(self):
        return self._srvrtid


    def get_trnamt(self):
        return self._trnamt


    def get_trntype(self):
        return self._trntype


    def set_checknum(self, value):
        self._checknum = OfxProperty('checknum',value.strip(),'string')
        self._properties['checknum'] = self._checknum


    def set_dtavail(self, value):
        self._dtavail = OfxProperty('dtavail',value,'date')
        self._properties['dtavail'] = self._dtavail


    def set_dtposted(self, value):
        self._dtposted = OfxProperty('dtposted',value,'date')
        self._properties['dtposted'] = self._dtposted


    def set_dtuser(self, value):
        self._dtuser = OfxProperty('dtuser',value,'date')
        self._properties['dtuser'] = self._dtuser


    def set_fitid(self, value):
        self._fitid = OfxProperty('fitid',value.strip(),'string')
        self._properties['fitid'] = self._fitid


    def set_name(self, value):
        self._name = OfxProperty('name',value.strip(),'string')
        self._properties['name'] = self._name


    def set_memo(self, value):
        self._memo = OfxProperty('memo',value.strip(),'string')
        self._properties['memo'] = self._memo


    def set_namepayee(self, value):
        self._namepayee = OfxProperty('namepayee',value.strip(),'string')


    def set_payeeid(self, value):
        self._payeeid = OfxProperty('payeeid',value.strip(),'string')
        self._properties['payeeid'] = self._payeeid


    def set_refnum(self, value):
        self._refnum = OfxProperty('refnum',value.strip(),'string')
        self._properties['refnum'] = self._refnum


    def set_sic(self, value):
        self._sic = OfxProperty('sic',value,'string')
        self._properties['sic'] = self._sic


    def set_srvrtid(self, value):
        self._srvrtid = OfxProperty('srvrtid',value.strip(),'string')
        self._properties['srvrtid'] = self._srvrtid


    def set_trnamt(self, value):
        self._trnamt = OfxProperty('trnamt',value,'float')
        self._properties['trnamt'] = self._trnamt


    def set_trntype(self, value):
        self._trntype = OfxProperty('trntype',value.strip(),'string',enum=TransactionEnum)
        self._properties['trntype'] = self._trntype


    def del_checknum(self):
        del self._checknum


    def del_dtavail(self):
        del self._dtavail


    def del_dtposted(self):
        del self._dtposted


    def del_dtuser(self):
        del self._dtuser


    def del_fitid(self):
        del self._fitid


    def del_name(self):
        del self._name


    def del_memo(self):
        del self._memo


    def del_namepayee(self):
        del self._namepayee


    def del_payeeid(self):
        del self._payeeid


    def del_refnum(self):
        del self._refnum


    def del_sic(self):
        del self._sic


    def del_srvrtid(self):
        del self._srvrtid


    def del_trnamt(self):
        del self._trnamt


    def del_trntype(self):
        del self._trntype

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
 

class BankTranList(OfxProperty):
    def __init__(self, name, value, type):
        self._enumArgs = Enum(['dtstart','dtend','stmttrn'])
        OfxProperty.__init__(self, name, value, type, liste=True, enumArgs=self._enumArgs)
        self._dtstart = None
        self._dtend = None

    def get_dtstart(self):
        return self._dtstart


    def get_dtend(self):
        return self._dtend


    def set_dtstart(self, value):
        self._dtstart = OfxProperty('dtstart',value,'date')
        self._properties['dtstart'] = self._dtstart


    def set_dtend(self, value):
        self._dtend = OfxProperty('dtend',value,'date')
        self._properties['dtend'] = self._dtend


    def del_dtstart(self):
        del self._dtstart


    def del_dtend(self):
        del self._dtend

    dtstart = property(get_dtstart, set_dtstart, del_dtstart, "dtstart's docstring")
    dtend = property(get_dtend, set_dtend, del_dtend, "dtend's docstring")


class OfxRoot(OfxProperty): 
    def __init__(self, name, value, type, dtserver=None, 
                 bankid=None, branchid=None, acctid=None, accttype=None,
                 balamt=None, dtasof=None):
        self._enumArgs = Enum(['signonmsgsrsv1','bankmsgsrsv1'])
        OfxProperty.__init__(self, name, value, type, liste=True, enumArgs=self._enumArgs)
        self.signonmsgsrsv1 = SignonMsg('SIGNONMSGSRSV1','SIGNONMSGSRSV1','object',dtserver=dtserver)
        self.bankmsgsrsv1 = BankMsg('BANKMSGSRSV1','BANKMSGSRSV1','object', 
                                    bankid=bankid, branchid=branchid, acctid=acctid, accttype=accttype,
                                    balamt=balamt, dtasof=dtasof) 

    def get_signonmsgsrsv1(self):
        return self._signonmsgsrsv1


    def get_bankmsgsrsv1(self):
        return self._bankmsgsrsv1


    def set_signonmsgsrsv1(self, value):
        self._signonmsgsrsv1 = value
        self._properties['signonmsgsrsv1'] = self._signonmsgsrsv1


    def set_bankmsgsrsv1(self, value):
        self._bankmsgsrsv1 = value
        self._properties['bankmsgsrsv1'] = self._bankmsgsrsv1


    def del_signonmsgsrsv1(self):
        del self._signonmsgsrsv1


    def del_bankmsgsrsv1(self):
        del self._bankmsgsrsv1

    signonmsgsrsv1 = property(get_signonmsgsrsv1, set_signonmsgsrsv1, del_signonmsgsrsv1, "signonmsgsrsv1's docstring")
    bankmsgsrsv1 = property(get_bankmsgsrsv1, set_bankmsgsrsv1, del_bankmsgsrsv1, "bankmsgsrsv1's docstring")


class SignonMsg(OfxProperty): 
    def __init__(self, name, value, type, dtserver=None):
        self._enumArgs = Enum(['sonrs'])
        OfxProperty.__init__(self, name, value, type, liste=True, enumArgs=self._enumArgs)
        self.sonrs = SignonResponse('sonrs','sonrs','object',dtserver)

    def get_sonrs(self):
        return self._sonrs


    def set_sonrs(self, value):
        self._sonrs = value
        self._properties['sonrs'] = self._sonrs


    def del_sonrs(self):
        del self._sonrs

    sonrs = property(get_sonrs, set_sonrs, del_sonrs, "sonrs's docstring")


class BankMsg(OfxProperty): 
    def __init__(self, name, value, type, 
                 bankid=None, branchid=None, acctid=None, accttype=None,
                 balamt=None, dtasof=None):
        self._enumArgs = Enum(['stmttrnrs'])
        OfxProperty.__init__(self, name, value, type, liste=True, enumArgs=self._enumArgs)
        self.stmttrnrs = StatementTransactionResponse('stmttrnrs','stmttrnrs','object', 
                                                      bankid=bankid, branchid=branchid, acctid=acctid, accttype=accttype,
                                                      balamt=balamt, dtasof=dtasof)

    def get_stmttrnrs(self):
        return self._stmttrnrs


    def set_stmttrnrs(self, value):
        self._stmttrnrs = value
        self._properties['stmttrnrs'] = self._stmttrnrs


    def del_stmttrnrs(self):
        del self._stmttrnrs

    stmttrnrs = property(get_stmttrnrs, set_stmttrnrs, del_stmttrnrs, "stmttrnrs's docstring")

 
class OfxParser(object):
    
    @classmethod
    def load_property(cls, name, entity):
        ppty = None
        ppty_tag = entity.find(name)
        if hasattr(ppty_tag, 'contents'):
            if len(ppty_tag.contents)>0:
                ppty = ppty_tag.contents[0]
        return ppty
    
    @classmethod
    def parse(cls_, file_handle):
        ofx = BeautifulStoneSoup(file_handle)
        ofxRoot = OfxRoot('ofx','ofx','object')
                
        signon_ofx = ofx.find('signonmsgsrsv1')
        if signon_ofx:
            ofxRoot.signonmsgsrsv1.sonrs = cls_.parseSignonResponse(signon_ofx)
            
        bankmsg_ofx = ofx.find('bankmsgsrsv1')
        if bankmsg_ofx:
            ofxRoot.bankmsgsrsv1.stmttrnrs = cls_.parseStatementTransactionResponse(bankmsg_ofx)   
            
        return ofxRoot
    
 
    @classmethod
    def parseSignonResponse(cls_, signon_ofx):
        ''' Parse the <SIGNONMSGSRSV1> tag and return an SignonResponse object. '''
        
        signon_response = SignonResponse('sonrs','sonrs','object')   
                
        status_tag = signon_ofx.find('status')
        if hasattr(status_tag, 'contents'):
            signon_response.status = Status('status','status','object')
            code_tag = status_tag.find('code')
            if hasattr(code_tag, 'contents'):
                signon_response.status.code = code_tag.contents[0]
            severity_tag = status_tag.find('severity')
            if hasattr(severity_tag, 'contents'):
                signon_response.status.severity = severity_tag.contents[0]
                
        dtserver_tag = signon_ofx.find('dtserver')
        if hasattr(dtserver_tag, 'contents'):
            signon_response.dtserver = dtserver_tag.contents[0]
                
        language_tag = signon_ofx.find('language')
        if hasattr(language_tag, 'contents'):
            signon_response.language = language_tag.contents[0]
                
        dtprofup_tag = signon_ofx.find('dtprofup')
        if hasattr(dtprofup_tag, 'contents'):
            signon_response.dtprofup = dtprofup_tag.contents[0]
                
        dtacctup_tag = signon_ofx.find('dtacctup')
        if hasattr(dtacctup_tag, 'contents'):
            signon_response.dtacctup = dtacctup_tag.contents[0]
        
        return signon_response
    
    
    @classmethod
    def parseStatementTransactionResponse(cls_, bankmsg_ofx):
        statement_transaction_response = StatementTransactionResponse('stmttrnrs','stmttrnrs','object')  
                
        trnuid_tag = bankmsg_ofx.find('trnuid')
        if hasattr(trnuid_tag, 'contents'):
            statement_transaction_response.trnuid = trnuid_tag.contents[0]
                
        status_tag = bankmsg_ofx.find('status')
        if hasattr(status_tag, 'contents'):
            statement_transaction_response.status = Status('status','status','object')
            code_tag = status_tag.find('code')
            if hasattr(code_tag, 'contents'):
                statement_transaction_response.status.code = code_tag.contents[0]
            severity_tag = status_tag.find('severity')
            if hasattr(severity_tag, 'contents'):
                statement_transaction_response.status.severity = severity_tag.contents[0] 
                
        stmtrs_tag = bankmsg_ofx.find('stmtrs')
        if hasattr(stmtrs_tag, 'contents'):
            statement_transaction_response.stmtrs = cls_.parseStatementResponse(stmtrs_tag)
        
        return statement_transaction_response
 
    @classmethod
    def parseStatementResponse(cls_,stmtrs_tag):
        stmttrnKeys = {}
        statement_response = StatementResponse('stmtrs','stmtrs','object')
                
        curdef_tag = stmtrs_tag.find('curdef')
        if hasattr(curdef_tag, 'contents'):
            statement_response.curdef = curdef_tag.contents[0]
                
        bankacctfrom_tag = stmtrs_tag.find('bankacctfrom')
        if hasattr(bankacctfrom_tag, 'contents'):
            statement_response.bankacctfrom = BankAccount('bankacctfrom', 'bankacctfrom', 'object')
                    
            content = OfxParser.load_property('acctid', bankacctfrom_tag)
            if content : statement_response.bankacctfrom.acctid = content
            content = OfxParser.load_property('bankid', bankacctfrom_tag)
            if content : statement_response.bankacctfrom.bankid = content
            content = OfxParser.load_property('branchid', bankacctfrom_tag)
            if content : statement_response.bankacctfrom.branchid = content
            content = OfxParser.load_property('accttype', bankacctfrom_tag)
            if content : statement_response.bankacctfrom.accttype = content

            # banktranlist
                    
            banktranlist_tag = stmtrs_tag.find('banktranlist')
            if hasattr(banktranlist_tag, 'contents'):
                
                content = OfxParser.load_property('dtstart', banktranlist_tag)
                if content : statement_response.banktranlist.dtstart = content
                content = OfxParser.load_property('dtend', banktranlist_tag)
                if content : statement_response.banktranlist.dtend = content

                #statement_response.banktranlist = OfxProperty('banktranlist','banktranlist','object',liste=True)
                for stmt_transaction in stmtrs_tag.findAll('stmttrn'):
                    stmt_trn = StatementTransaction('stmttrn','stmttrn','object')
                    statement_response.banktranlist.items.append(stmt_trn)
                    
                    content = OfxParser.load_property('trntype', stmt_transaction)
                    if content : stmt_trn.trntype = content
                    content = OfxParser.load_property('dtposted', stmt_transaction)
                    if content : stmt_trn.dtposted = content  
                    content = OfxParser.load_property('dtuser', stmt_transaction)
                    if content : stmt_trn.dtuser = content  
                    content = OfxParser.load_property('dtavail', stmt_transaction)
                    if content : stmt_trn.dtavail = content  
                    content = OfxParser.load_property('trnamt', stmt_transaction)
                    if content : stmt_trn.trnamt = content   
                    content = OfxParser.load_property('fitid', stmt_transaction)
                    if content : stmt_trn.fitid = content   
                    content = OfxParser.load_property('srvrid', stmt_transaction)
                    if content : stmt_trn.srvrid = content  
                    content = OfxParser.load_property('checknum', stmt_transaction)
                    if content : stmt_trn.checknum = content                          
                    content = OfxParser.load_property('sic', stmt_transaction)
                    if content : stmt_trn.sic = content
                    content = OfxParser.load_property('payeeid', stmt_transaction)
                    if content : stmt_trn.payeeid = content                        
                    content = OfxParser.load_property('name', stmt_transaction)
                    if content : stmt_trn.name = content                      
                    content = OfxParser.load_property('memo', stmt_transaction)
                    if content : stmt_trn.memo = content

                    stmt_trn.norm_last()
                    if stmttrnKeys.has_key(stmt_trn.fitid.string):
                        #print('==>Doublon')
                        #print(stmt_trn.prettyPrint())
                        while stmttrnKeys.has_key(stmt_trn.fitid.string):
                            if stmt_trn.memo:
                                stmt_trn.memo = stmt_trn.memo.string +'.'
                            else:
                                stmt_trn.memo = '.'
                            stmt_trn.fitid = '0' + stmt_trn.fitid.string
                            stmt_trn.norm_last()
                            #print(stmt_trn.prettyPrint())
                    else:
                        stmttrnKeys[stmt_trn.fitid.string]=1
                        
            ledgerbal_tag = stmtrs_tag.find('ledgerbal')
            if hasattr(ledgerbal_tag, 'contents'):
                ledgerbal = Bal('ledgerbal','ledgerbal','object')  
                                
                content = OfxParser.load_property('balamt', ledgerbal_tag)
                if content : ledgerbal.balamt = content
                content = OfxParser.load_property('dtasof', ledgerbal_tag)
                if content : ledgerbal.dtasof = content

                statement_response.ledgerbal = ledgerbal
                        
            availbal_tag = stmtrs_tag.find('availbal')
            if hasattr(ledgerbal_tag, 'contents'):
                availbal = Bal('availbal','availbal','object') 
                                
                content = OfxParser.load_property('balamt', availbal_tag)
                if content : availbal.balamt = content
                content = OfxParser.load_property('dtasof', availbal_tag)
                if content : availbal.dtasof = content

                statement_response.availbal = availbal
    
        return statement_response
    

 
class QifParser(object):
    
    @classmethod
    def parse(cls_, stream, bankid='bankid', branchid='branchid',
              acctid='acctid', accttype='CHECKING'):
        
        qifstmt = {}
        enreg = 0
        
        if hasattr(stream, 'read'):        # It's a file-type object.
            fin = stream
        else:
            fin = open(stream,'r')
        

        for line in fin:
            linestrip = line.strip()
            if linestrip[0]== 'D':
                dtstart = linestrip[7:]+linestrip[4:6]+linestrip[1:3]
            elif linestrip[0]== 'T':
                balamt= linestrip[1:].replace(',','')
            elif line.strip()=='^':
                break
        dtend = dtstart
        fbalamt = float(balamt)
        ofxRoot = OfxRoot('ofx','ofx','object')
        bankacctfrom = ofxRoot.bankmsgsrsv1.stmttrnrs.stmtrs.bankacctfrom
        ledgerbal = ofxRoot.bankmsgsrsv1.stmttrnrs.stmtrs.ledgerbal
        availbal = ofxRoot.bankmsgsrsv1.stmttrnrs.stmtrs.availbal
        bankacctfrom.bankid   = bankid
        bankacctfrom.branchid = branchid
        bankacctfrom.acctid   = acctid
        bankacctfrom.accttype = accttype
        banktranlist = ofxRoot.bankmsgsrsv1.stmttrnrs.stmtrs.banktranlist
        
        for line in fin:
            #print(line.strip())
            linestrip = line.strip()
            if linestrip[0]== 'D':
                qifstmt['dtposted']= linestrip[7:]+linestrip[4:6]+linestrip[1:3]
                if qifstmt['dtposted'] < dtstart:
                    dtstart = qifstmt['dtposted']
                if qifstmt['dtposted'] > dtend:
                    dtend = qifstmt['dtposted']
            elif linestrip[0]== 'M':
                memo = linestrip[1:]
                try:
                    qifstmt['memo'] = memo.decode('utf-8')
                except:
                    qifstmt['memo'] = memo.decode('latin-1')
            elif linestrip[0]== 'T':
                qifstmt['trnamt']= linestrip[1:].replace(',','')
                fbalamt = fbalamt + float(qifstmt['trnamt']) 
            elif linestrip[0]== 'P':
                name = linestrip[1:]
                try:
                    qifstmt['name'] = name.decode('utf-8')
                except:
                    qifstmt['name'] = name.decode('latin-1')
            elif linestrip[0]== 'L':
                qifstmt['categ']= linestrip[1:]
            elif linestrip[0]== 'N':
                checknum = linestrip[1:]
                try :
                    qifstmt['checknum'] = int(checknum)
                    print(type(qifstmt['checknum']), qifstmt['checknum'])
                except:
                    qifstmt['checknum'] = checknum
            if line.strip()=='^':
                enreg = enreg + 1
                
                stmt_trn = StatementTransaction('stmttrn','stmttrn','object')
                stmt_trn.dtposted = qifstmt['dtposted']
                stmt_trn.trntype = 'OTHER'
                if qifstmt.has_key('memo'):
                    stmt_trn.memo = qifstmt['memo']
                if qifstmt.has_key('trnamt'):
                    stmt_trn.trnamt = qifstmt['trnamt']
                if qifstmt.has_key('name'):
                    stmt_trn.name = qifstmt['name']
                if qifstmt.has_key('checknum'):
                    stmt_trn.checknum = str(qifstmt['checknum'])
                    if isinstance(qifstmt['checknum'],int):
                        stmt_trn.trntype = 'CHECK'
                    elif qifstmt['checknum'] == 'XFER':
                        stmt_trn.trntype = 'XFER'
                    elif qifstmt['checknum'] == 'Virmt':
                        stmt_trn.trntype = 'REPEATMT'
                    elif qifstmt['checknum'] == 'VTMREC':
                        stmt_trn.trntype = 'CREDIT'
                    elif qifstmt['checknum'] == 'VIRT':
                        stmt_trn.trntype = 'XFER'
                    elif qifstmt['checknum'] == 'TIP':
                        stmt_trn.trntype = 'DEBIT'
                    elif qifstmt['checknum'] == 'SRVCHG':
                        stmt_trn.trntype = 'SRVCHG'
                    elif qifstmt['checknum'] == 'SERVICE':
                        stmt_trn.trntype = 'SRVCHG'
                    elif qifstmt['checknum'] == 'RETRCB':
                        stmt_trn.trntype = 'ATM'
                    elif qifstmt['checknum'] == 'REPEATMT':
                        stmt_trn.trntype = 'REPEATMT'
                    elif qifstmt['checknum'] == 'Prelvmt':
                        stmt_trn.trntype = 'PAYMENT'
                    elif qifstmt['checknum'] == 'Prelmvt':
                        stmt_trn.trntype = 'PAYMENT'
                    elif qifstmt['checknum'] == 'DEPOT':
                        stmt_trn.trntype = 'DEP'
                    elif qifstmt['checknum'] == 'DEP':
                        stmt_trn.trntype = 'DEP'
                    elif qifstmt['checknum'] == 'Carte':
                        stmt_trn.trntype = 'POS'
                    elif qifstmt['checknum'] == 'CREDIT':
                        stmt_trn.trntype = 'CREDIT'
                    elif qifstmt['checknum'] == 'CNInet':
                        stmt_trn.trntype = 'DEBIT'
                    elif qifstmt['checknum'] == 'CBInet':
                        stmt_trn.trntype = 'DEBIT'

                banktranlist.items.append(stmt_trn)
        banktranlist.dtstart = dtstart
        banktranlist.dtend = dtend
        ledgerbal.dtasof = dtend
        availbal.dtasof = dtend
        ledgerbal.balamt = fbalamt
        availbal.balamt = fbalamt
        
        return ofxRoot
 
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
         
    test(OfxParser.parse(file('../test.ofx')))  
    print('===')
    test(OfxParser.parse(file('../test.ofc')))
    print('===')
    ofxroot = OfxRoot('OFX','OFX','object',dtserver='20100205170222',
                      bankid='77777', branchid='00777', acctid='044444B',
                      balamt=123.45, dtasof='20100201170222')
    print(ofxroot.prettyPrint())
    print('===')
    testqif(QifParser.parse('../test.qif'))  

if __name__ == '__main__': 
    main()
