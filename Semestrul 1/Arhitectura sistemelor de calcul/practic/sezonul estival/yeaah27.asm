bits 32
global start        

extern exit,scanf,printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data

    format db "%c",0
    formator db "%d",0
    caracter db 0
    sir db "de la moara pan la gara , am fumat inc-o tigara",0
    len equ $-sir

segment code use32 class=code
    start:
        push dword caracter
        push format
        call [scanf]
        add esp, 4*2
        
        
        
        mov edi, sir
        mov al,[caracter]
        mov ecx,len
        mov ebx,0
        cld
        
        repet:
            scasb 
            jne cont
            inc ebx
            
            cont:
        loop repet
        
        push ebx
        push formator
        call [printf]
        add esp, 4*2
        


        push    dword 0
        call    [exit]
