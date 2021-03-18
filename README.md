# sipri
A simple way to access Stockholm International Peace Research Institute's (SIPRI) trade register API and return a CSV file.

```
>>>import sipri
>>> data = sipri.sipri_data()
>>> data
'tidn,buyercod,sellercod,odat,odai,onum,onai,ldat,term,desig2,wcat,desc,coprod,nrdel,nrdelai,delyears,buyer,seller,status,tivunit,tivorder,tivdel\n63890,AUS,AST,2015,,1100,X,0,N/A,M16,EN,Diesel engine,L,0,,,Australia,Austria,N,0.02,22,0\n62447,BAN,AST,2017,X,6,,0,N/A,DA40,AC,Light aircraft,L,,,,Bangladesh,Austria,N,0.15,0.9,0\n58981,CZR,AST,2017,,20,,2020,LIC,Pandur-2,AV,APC,L,16,X,2020,Czechia,Austria,N,0.31,6.2,4.96\n64172,FRA,AST,2019,X,4,,2020,N/A,Camcopter S-100,AC,UAV,L,4,,2020,France,Austria,N,0.2,0.8,0.8\n62594,INS,AST,2019,,23,,0,VIA,Pandur-2,AV,IFV,,,,,Indonesia...
```
<br>
Sipri_data allows you to quickly pull from SIPRI's API and return a comma seperated string for easy transfer to a CSV or pandas dataframe. The sipri package is safe and only uses requests as an external package.

_Couldn't I have just done this myself?_
* Absolutly, there is nothing special about this package. Normaly when you access SIPRI's trade registar the data is returened in a rich text file (rtf). Parsing a rtf is not a great experience. When I was searching for a way to get the data in some other way, I found there were lots of other people asking the same quesiton. So, I decided to make this package in hopes of helping future analysts. Plus, I've never made a python package before so I thought this would be an easy one to start with.

## Getting Started

Sipri is available on PyPI:

```$ python -m pip install sipri```

Sipri only supports Python 3.5+, but probably will work on Python 2.7 as well.

## Keyword Arguments

```sipri.sipri_data(low_year='2020',high_year='2020',seller='',buyer='',armanent_category='any',buyers_or_sellers='',filetype='csv',include_open_deals='on',sum_deliveries='off')```

* low_year:(optional) This is the year you want the query to start with (defaults to '2020').<br>
* high_year:(optional) This is the year you want the query to end with (defaults to '2020').<br>
* seller: (optional) The entity/country selling equipment (defaults to all entity/country) see the entity/country list below for all possible three letter values and corresponding name.<br>
* buyer: (optional) The entity/country buying equipment (defaults to all entity/country) see the entity/country list below for all possible three letter values and corresponding name.<br>
* armanent_category: (optional) The specific equipment category tracked by SIPRI (defaults to 'any'). Equipment category list is provided below.<br>
* buyers_or_sellers: (optional) Sorts the data by sellers or buyers (this is important if you choose 'rtf' as a file type).<br>
* filetype: (optional) accepted values are 'csv'(default value) or 'rtf'.
* include_open_deals: (optional) accepted values are 'on'(default value) or 'off'.<br>
* sum_deliveries: (optional) accepted values are 'on' or 'off'(default value) this will sum all deliveries if 'on' is selected.<br>

### "Countries/Entities List (only use the two or three letter values)    
```
"AFG" = Afghanistan
"AU"= African Union**
"ALB" = Albania
"ALG" = Algeria
"ANG" = Angola
"ARG" = Argentina
"ARM" = Armenia
"AUS" = Australia
"AST" = Austria
"AZB" = Azerbaijan
"BAS" = Bahamas
"BAH" = Bahrain
"BAN" = Bangladesh
"BAR" = Barbados
"BLR" = Belarus
"BEL" = Belgium
"BLZ" = Belize
"BEN" = Benin
"BHU" = Bhutan
"BOL" = Bolivia
"BOS" = Bosnia-Herzegovina
"BOT" = Botswana
"BRA" = Brazil
"BRU" = Brunei
"BUL" = Bulgaria
"BF "= Burkina Faso
"BDI" = Burundi
"CAP" = Cabo Verde
"CMB" = Cambodia
"CAM" = Cameroon
"CAN" = Canada
"CAR" = Central African Republic
"CHA" = Chad
"CHE" = Chile
"CHI" = China
"COL" = Colombia
"COM" = Comoros
"CON" = Congo
"COS" = Costa Rica
"IVO" = Cote d'Ivoire
"CRO" = Croatia
"CUB" = Cuba
"CYP" = Cyprus
"CZR" = Czechia
"DRC" = DR Congo
"XSD" = Darfur rebels (Sudan)*
"DEN" = Denmark
"DJI" = Djibouti
"DOM" = Dominican Republic
"ECU" = Ecuador
"EGY" = Egypt
"SAL" = El Salvador
"EQU" = Equatorial Guinea
"ERI" = Eritrea
"EST" = Estonia
"ETH" = Ethiopia
"FJI" = Fiji
"FIN" = Finland
"FRA" = France
"GAB" = Gabon
"GAM" = Gambia
"GEO" = Georgia
"FRG" = Germany
"GHA" = Ghana
"GRE" = Greece
"GUA" = Guatemala
"GUI" = Guinea
"GUY" = Guyana
"XPA" = Hamas (Palestine)*
"XLH" = Hezbollah (Lebanon)*
"HON" = Honduras
"XYH" = Houthi rebels (Yemen)*
"HUN" = Hungary
"ICE" = Iceland
"IND" = India
"INS" = Indonesia
"IRA" = Iran
"IRQ" = Iraq
"IRE" = Ireland
"ISR" = Israel
"ITA" = Italy
"JAM" = Jamaica
"JAP" = Japan
"JOR" = Jordan
"KAZ" = Kazakhstan
"KEN" = Kenya
"KIR" = Kiribati
"KSV" = Kosovo
"KUW" = Kuwait
"KYR" = Kyrgyzstan
"XUL" = LRA (Uganda)*
"XSL" = LTTE (Sri Lanka)*
"LAO" = Laos
"LAT" = Latvia
"LEB" = Lebanon
"LES" = Lesotho
"LIB" = Liberia
"LYA" = Libya
"LYW" = Libya GNC
"LYE" = Libya HoR
"LIT" = Lithuania
"LUX" = Luxembourg
"MAD" = Madagascar
"MWI" = Malawi
"MAL" = Malaysia
"MLV" = Maldives
"MLI" = Mali
"MTA" = Malta
"MAR" = Marshall Islands
"MRA" = Mauritania
"MAU" = Mauritius
"MEX" = Mexico
"MIC" = Micronesia
"MON" = Mongolia
"MTG" = Montenegro
"MOR" = Morocco
"MOZ" = Mozambique
"MYA" = Myanmar
"NAT" = NATO**
"XMN" = NLA (Macedonia)*
"XLB" = NTC (Libya)*
"NAM" = Namibia
"NEP" = Nepal
"NET" = Netherlands
"NZ"= New Zealand
"NIC" = Nicaragua
"NIR" = Niger
"NIG" = Nigeria
"KON" = North Korea
"MAC" = North Macedonia
"XAN" = Northern Alliance (Afghanistan)*
"NOR" = Norway
"OSC" = OSCE**
"OMA" = Oman
"XID" = PIJ (Israel/Palestine)*
"XTP" = PKK (Turkey)*
"XPC" = PRC (Israel/Palestine)*
"PAK" = Pakistan
"PAL" = Palau
"PA"= Palestine
"PAN" = Panama
"PAP" = Papua New Guinea
"PAR" = Paraguay
"PER" = Peru
"PHI" = Philippines
"POL" = Poland
"POR" = Portugal
"QAT" = Qatar
"XSR" = RUF (Sierra Leone)*
"RSS" = Regional Security System**
"ROM" = Romania
"RUS" = Russia
"RWA" = Rwanda
"SAM" = Samoa
"SAU" = Saudi Arabia
"SEN" = Senegal
"SER" = Serbia
"SEY" = Seychelles
"SIE" = Sierra Leone
"SIN" = Singapore
"SLK" = Slovakia
"SLO" = Slovenia
"SOL" = Solomon Islands
"SOM" = Somalia
"SA"= South Africa
"KOS" = South Korea
"SSD" = South Sudan
"SPA" = Spain
"SRI" = Sri Lanka
"SUD" = Sudan
"SUR" = Suriname
"SWE" = Sweden
"SWI" = Switzerland
"SYR" = Syria
"XSX" = Syria rebels*
"TAI" = Taiwan
"TAJ" = Tajikistan
"TAN" = Tanzania
"THA" = Thailand
"ET"= Timor-Leste
"TOG" = Togo
"TON" = Tonga
"TRI" = Trinidad and Tobago
"TUN" = Tunisia
"TUR" = Turkey
"TRK" = Turkmenistan
"TUV" = Tuvalu
"UAE" = UAE
"XSI" = UIC (Somalia)*
"UGA" = Uganda
"UKR" = Ukraine
"XUR" = Ukraine Rebels*
"UK" = United Kingdom
"UNO = United Nations**
"USA" = United States
"XMU" = United Wa State (Myanmar)*
"XXU" = Unknown rebel group*
"XXR" = Unknown recipient(s)
"URU" = Uruguay
"UZB" = Uzbekistan
"VAN" = Vanuatu
"VEN" = Venezuela
"VN"= Viet Nam
"SAH" = Western Sahara
"YEM" = Yemen
"ZAM" = Zambia
"ZIM" = Zimbabwe
"SWA" = eSwatini
```

### Equipment Category List (only use the number)
```    
"any" = All categories
"1" = Aircraft
"14" = Air defence systems
"2" = Artillery
"3" = Armoured vehicles
"4" = Engines
"5" = Sensors
"6" = Missiles
"12" = Naval weapons
"11" = Other
"13" = Satellites
"7" = Ships
```

## Examples

Pulling data and importing into a Pandas dataframe.
```
>>> import sipri
>>> import pandas
>>> import io
>>> from io import StringIO

>>> data = sipri.sipri_data()
>>> df = pd.read_csv(StringIO(r),keep_default_na=False,na_values=['None'])

>>> df.head()

<the first five rows of the pandas data frame will return>
```

Only looking for aircraft sold by the UK during the year 1995.
```
>>> import sipri

>>> data = sipri.sipri_data(low_year='1995',high_year='1995',seller='UK', armanent_category='1')
```


## Terms and Conditions

This python package is in no way affiliated with Stockholm International Peace Research Institute (SIPRI). SIPRI could change their API at anypoint causing this package to be obsolete. By using this package you still have to adhere to SIPRI's [terms and conditions](https://www.sipri.org/about/terms-and-conditions). 
