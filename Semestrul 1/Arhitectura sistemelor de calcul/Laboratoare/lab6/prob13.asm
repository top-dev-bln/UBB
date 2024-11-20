bits 32
global start

extern exit
import exit msvcrt.dll

;12311011h,1116adch,4120ca1h, 234681h, 0a90b87ch, 29b65cad9h , 12345607h, 1A2B3C15h, 13A33412h
segment data use32 class=data
sir dd  12345607h, 1A2B3C15h, 13A33412h
len equ ($-sir)/4
D   db 0,0,0
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