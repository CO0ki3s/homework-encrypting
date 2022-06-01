# URL ID encrypt and decrypt

Pomocou funkcie crypt_decrypt v triede ProtectUidToUrl v časti cryenurl.py šifrujeme ID ktoré sa nachádza v URL.

Predpokladame že budeme pracovať s URL v tvare:
https://www.example.com/user/?profilEditUserId=59562135

S tejto URL sa šifruje a dešifruje časť nachádzajúca sa za "=" 

Funkcia crypt_decrypt sa zapisuje v tomto tvare:
## crypt_decrypt(url, argname, uid)

**url** -> do tejto premennej vkladáme časť URL ktorá je bez ID ktoré budeme šifrovať alebo dešifrovať bez znaku "="

**argname** -> táto premenná nám rozhodne či sa bude šifrovať alebo dešifrovať pomocou anglický ekvivalentov slov *"crypt"* pre šifrovanie a *"decrypt"* pre dešifrovanie

**uid** -> je časť URL ktorá je za "="

## Šifrovanie a dešifrovanie

Šifrovanie, ak sa *argname="crypt"* prebieha takto:
1. **Secret key** sa spája s uid z funkcie a vytvára kľúč
2. Pomocou funcie XOR prebehne šifrovanie uid s kľúčom
3. Funkcia bytearray() nám vráti pole bitov už vyXORovanej premennej
4. Funkciou standart_b64encode() sa premenná zakóduje do formátu Base64
5. Premennú nakoniec dekódujeme späť do formátu UTF-8
6. return funcie nám vracia už spojenú URL so zašifrovaným ID

Zašifrovaná URL ktorá je spomenutá na začiatku vyzerá takto:
https://www.example.com/user/?profilEditUserId=dlZaXVtUQFQ=
