bits 32
global start        

extern exit, scanf, printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data

    
    citindo  dd 0
    formator db "%d",0
    


segment code use32 class=code
    start:
    
        mov ebx,0xFFFFFFFF
        
        repeta:
            push dword citindo
            push formator
            call [scanf]
            add esp, 4*2
            
            mov edx,0
            cmp [citindo],edx
            je gata_joaca
            
            cmp [citindo], ebx
            ja continue
            mov ebx, [citindo]
            
            
            
            
            continue:
        jmp repeta
        
        gata_joaca:
        
        
        
        push ebx
        push formator
        call [printf]
        add esp, 4*2
        


        push    dword 0
        call    [exit]
