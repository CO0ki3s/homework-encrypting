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

## Šifrovanie a dešifrovanie - cryenurl.py

Šifrovací kľúč **self.key** nachádzajúci sa v **__ init __** je možné ľubovoľne zmeniť za vlastný, unikátny string. 

Šifrovanie, ak sa *argname="crypt"* prebieha takto:
1. **Secret key** sa spája s uid z funkcie a vytvára kľúč
2. Pomocou funcie XOR prebehne šifrovanie uid s kľúčom
3. Funkcia bytearray() nám vráti pole bitov už vyXORovanej premennej
4. Funkciou standart_b64encode() sa premenná zakóduje do formátu Base64
5. Premennú nakoniec dekódujeme späť do formátu UTF-8
6. return funcie nám vracia už spojenú URL so zašifrovaným ID

Zašifrovaná URL ktorá je spomenutá na začiatku vyzerá takto:
https://www.example.com/user/?profilEditUserId=dlZaXVtUQFQ=

Dešifrovanie, ak sa *argname="decrypt"* prebieha takto:
1. **Secret key** sa spája s uid z funkcie a vytvára kľúč
2. Funkcia bytearray() nám vráti pole bitov zašifrovaného uid
3. Funkciou standart_b64decode() sa premenná dekóduje z formátu Base64
4. Premennú dekódujeme späť do formátu UTF-8
5. Pomocou funcie XOR prebehne dešifrovanie uid pomocou kľúča
6. return funcie nám vracia už spojenú URL so rozšifrovaným ID

Pomocou tejto funkcie *crypt_decrypt* sme šifrovali a dešifrovali uid -> **59562135 -> dlZaXVtUQFQ= -> 59562135**

## Testovanie - test_cryenurl.py

Pomocou tohto algoritmu testujeme či naša funkcia pracuje správne.

URL ktoré budeme testovať sa nachádzajú v súbore **urls.txt**

Po načítaní url pomocou funkcie *for* ju vkladame do funkcie pre šifrovanie a dešifrovanie s **argname = "crypt"**. Pri vkladaní url do funkcie crypt_decrypt je url rozdelené funkciou *split()*.

Do konzole sa nám vrátia hodnoty:
1. Nezašifrovanej URL - DECRYPTED url
2. Zašifrovanej URL - ENCRYPTED url

Po zašifrovaní kotrolujeme či dešifrovanie prebehlo v poriadku. Do funkcie pre dešifrovanie a dešifrovanie vkladáme novú URL spolu s **argname = "decrypt"**.

Ak je splnená podmienka kde *uid* pred šifrovaním sa rovná *uid* po zašifrovaní a následnom rozšifrovaní, vracia sa hodnota "OK" do konzole. Ak táto podmienka neplatí do konzole sa vráti hodnota "BAD".

Do konzole sa nám vrátia hodnoty:
1. Samotného uid aký malo tvar pred šifrovaním, po šifrovaní a následne po dešifrovaní -> **59562135 -> dlZaXVtUQFQ= -> 59562135**
2. Výsledok kontroly podmienkov - **OK** alebo **BAD**

**Celý výpis konzoly jednej kotroly vyzerá takto:**

*---------------------------------------*

*DECRYPTED url: https://www.example.com/user/?serviceId=84sdf66sf4][;s5*

*ENCRYPTED url: https://www.example.com/user/?serviceId=e1scDw9TRRIUUT8+TwdQ*

*84sdf66sf4][;s5 -> e1scDw9TRRIUUT8+TwdQ -> 84sdf66sf4][;s5*

*OK*

*---------------------------------------*

## main.py

Po spustení main.py môžete vložiť do konzole ľubovoľnú URL vo vyššie spomenutom tvare.

https://www.example.com/user/?profilEditUserId=59562135

A program vám obratom vytvorí URL so zašifrovaným uid.

https://www.example.com/user/?profilEditUserId=dlZaXVtUQFQ=

**Celý výpis konzoly vyzerá takto:**

*Add URL: https://www.example.com/user/?serviceId=645sd4f6s5d4f*

*645sd4f6s5d4f -> dVtaGA1RFVcBUAZREg==*

*ENCRYPTED url: https://www.example.com/user/?serviceId=dVtaGA1RFVcBUAZREg==*
