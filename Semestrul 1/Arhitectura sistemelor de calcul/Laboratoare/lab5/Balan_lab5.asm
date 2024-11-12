bits 32

global start

extern exit
import exit msvcrt.dll

segment data use32 class=data


; Se dau 2 siruri de octeti S1 si S2 de aceeasi lungime. Sa se construiasca sirul D astfel incat fiecare element din D sa reprezinte maximul dintre elementele de pe pozitiile corespunzatoare din S1 si S2.
;Exemplu:
;S1: 1, 3, 6, 2, 3, 7
;S2: 6, 3, 8, 1, 2, 5
;D: 6, 3, 8, 2, 3, 7


    S1 db 1, 3, 6, 2, 3, 7
    S2 db 6, 3, 8, 1, 2, 5
    l equ $-S2 
    d times l db 0
    

segment code use32 class=code
    start:
    
    mov ecx,l
    mov esi,0
    mov eax,0
    mov ebx,0
    
    jecxz sfarsit
    
 
    
    repeta:
    
    mov al, [S1+esi]    
    mov bl, [S2+esi]
    
    cmp al, bl
    
    
    
    
    jg maimare
    mov [d+esi], bl
    
    jmp skip
    
    maimare:
    mov [d+esi], al
    
    
    
    skip:
    inc esi
    
    loop repeta 
    
    
    
    
    sfarsit:
    push    dword 0
    call    [exit]
