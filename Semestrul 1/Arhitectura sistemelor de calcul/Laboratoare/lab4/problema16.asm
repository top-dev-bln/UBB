bits 32 

global start        


extern exit   
import exit msvcrt.dll   

a db 01010111b
b dw 1001101110111110b
c dd 0
; cu datele acestea in EAX va fii 9B 7E F5 FF


segment data use32 class=data
segment code use32 class=code
    start:
    ;bitii 0-7 ai lui C au valoarea 1
    mov eax , [c]
    or al, 0xFF ; c = 00000000000000000000000011111111
                ;                                   AL

    ;bitii 8-11 ai lui C coincid cu bitii 4-7 ai lui A
    xor ebx, ebx
    mov bl, [a] 
    and bl, 11110000b ; bl = xxxx(din a) 0000
    mov bh,0
    mov cl ,4
    shl bx, cl; bx = 0000 xxxx 0000 0000 

    
    or ax, bx; eax = 000000000000 0000-0000XXXX 11111111
    
    
    ;bitii 12-19 coincid cu bitii 2-9 ai lui B
    mov ebx,0
    mov bx , [b]
    mov cl,2  ; da delete la bitii 0 1 
    shr bx, cl
    ;acum in bl avem bitii 2-9 lui b
    mov bh, bl; bh = 2-9 din b
    mov bl,0 
    ; ebx = 00000000 00000000 xxxxxxxx 00000000
    mov cl, 4
    shl ebx,cl ; ebx 00000000 0000xxxx xxxx0000 00000000
    
    or EAX, ebx;  000000000000(b:6-9)   (b:2-5)(a:4-7) 11111111
    
    mov ebx ,0
    mov bh,[a]
    and bh, 00001111b
    mov cl , 12
    shl ebx, cl
    ; EBX = 00000000 xxxx 000..00000
    
    or EAX, EBX; EAX = 00 7E F5 FF
    
    ;bitii 24-31 coincid cu octetului high din cuvantul B
    mov ebx,0
    mov bx, [b]
    mov bl,0
    shl ebx, 16
    
    or EAX, EBX 
    
    
    

        push    dword 0  
        call    [exit]   