bits 32
global start


extern exit, scanf,printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll


segment data use32 class=data

    zece dd 0
    saispe dd 0
    
    format_zece db "%d",0
    format_saispe db "%x",0
    
    mesaj db "%d",0

segment code use32 class=code

    start:
    
        push dword zece
        push dword format_zece
        call [scanf]
        add esp ,4*2
        
        push dword saispe
        push dword format_saispe
        call [scanf]
        add esp ,4*2

        
        mov eax , [zece]
        add eax, dword [saispe]
        
        mov ecx, 8*4
        mov ebx,0
        
        repeta:
        
            shr eax, 1
            adc ebx,0
       
        loop repeta
        
        

        
        
        push ebx
        push mesaj
        call [printf]
        add esp, 4*2
        
    
        push    dword 0
        call    [exit]