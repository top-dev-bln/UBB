
###### Regiştrii generali EU
- EAX - accumulator register (registrul acumulator) folosit ca unul dintre operanzi
- EBX - base register (registru general)
- ECX - counter register (registru contor pt instr care au nevoie de indicaţii numerice.
- EDX - data register 
**\_\_\_\_\_\_Lucru cu stiva\_\_\_\_\_\_\_\_\_**
- ESP - stack pointer
- EBP - base pointer
**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**
- EDI - desination index
- ESI - source index

###### Tip de date = dimensiunea de reprezentare (byte, word, dword, qword)

| byte    | word     | dword    | qword    |
| ------- | -------- | -------- | -------- |
| 8 biti  | 16 biti  | 32 biti  | 64 biti  |
| 1 octet | 2 octeti | 4 octeti | 8 octeti |

##### Operatii

op1 = m cifre
op2 = n cifre
__________
suma = max(m,n)+1(octet)
op1\*op2 = m+n cifre

###### Consecintele 
b+b  -> b
w+w ->w
dw + dw -> dw
__________
b\*b -> w
w\*w -> dw         32    32
dw\*dw -> qw - \[EDX]:\[EAX]   (doua jumatati)

Intrebare: De ce lucreaza trei registrii cu stiva?

Un program executabil este format dintr-o serie de activari si dezactivari de functii si proceduri, care se afla intr-o stiva ( stiva de executie )