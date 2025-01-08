bits 32
global start        

extern exit, scanf, printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    mesaj db "%d/%d=%d",0
    format db "%d",0
    a dd 0 
    b dw 0
    

segment code use32 class=code
    start:
    
        push dword a
        push format
        call [scanf]
        add esp, 4*1
        
        push dword b
        push format
        call [scanf]
        add esp, 4*1
        
        mov ax, [a]
        mov dx, [a+2]
        
        mov bx, [b]
        idiv bx; catul e in ax
        
        cwde ; catul e in eax
        push eax
        
        
        push dword [a]
        mov ax, bx
        cwde
        push eax
        
        
        push mesaj
        call [printf]
        add esp, 4*2
    
    
    


        push    dword 0
        call    [exit]
