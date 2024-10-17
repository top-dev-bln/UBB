bits 32
global start        

extern exit
import exit msvcrt.dll


segment data use32 class=data ;(g+5)-a*d
a db 3
d db 2
g dw 70


segment code use32 class=code
    start:  ;(g+5)-a*d
    
    MOV EAX,0
    
    ADD WORD [g], 5   ;[g] = g+5
    MOV AL,[a]        ;AL = a
    MUL byte [d]      ;AX = a*d
    
    
    ;;pentru ca vreau sa il vad in debugger o sa fac interschimbare
    MOV DX,AX
    MOV AX,[g]

    SUB AX,DX
    
    
        
        
    

        push    dword 0
        call    [exit]

        