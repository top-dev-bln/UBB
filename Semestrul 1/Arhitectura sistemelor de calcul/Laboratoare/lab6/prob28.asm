;Dandu-se un sir de octeti si un subsir al sau, sa se elimine din primul sir toate aparitiile subsirului.

bits 32
global start

extern exit
import exit msvcrt.dll


segment data use32 class=data
sir db  12h,11h,41h, 23h, 0ah, 29h , 12h, 1Ah, 13h
sub_sir db 12h, 1Ah, 13h
sir_temp db  0,0,0,0,0,0,0,0,0
segment code use32 class=code
    start:
    mov esi, sir
    mov edi, D
    mov ecx, len
    mov bl, 7
    cld
    
    

    repeta:
        lodsd ;;; eax = numar din sir
        mov bh, al ;  pun octetul in bh in caz ca e bun
        mov ah ,0 ; dau clear la ah pentru ca acolo vine modulo 
        div bl ; il impart cu 7
        cmp ah,0 ; verific daca al % 7 == 0 
        
        jne nonmultiplu ; daca nu , ii dam skip
        mov al, bh ;; octetul din bh salvat il pun inapoi pe al ca sa ii dau load in sirul d
        stosb
        
       nonmultiplu:
    loop repeta
        
        


    push    dword 0
    call    [exit]