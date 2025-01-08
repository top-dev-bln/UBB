bits 32
global start


extern exit, scanf,printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll


segment data use32 class=data

    
    form db "%d",0
    fmic db"%d < %d",0
    fegal db"%d = %d",0
    fmare db"%d > %d",0

    
    a dd 0
    b dd 0


segment code use32 class=code

    start:
    
        push dword a
        push dword form
        call [scanf]
        add esp ,4*2
        
        push dword b
        push dword form
        call [scanf]
        add esp ,4*2
        
        mov eax, [a]
        mov ebx, [b]
        cmp eax,ebx
        
        ja mare
        jb mic
        
        
        egal:
        push ebx
        push eax
        push dword fegal
        call [printf]
        add esp, 4*2
        
        push    dword 0
        call    [exit]
        
        mic:
        push ebx
        push eax
        push dword fmic
        call [printf]
        add esp, 4*2
        
        push    dword 0
        call    [exit]        
        
        mare:
        push ebx
        push eax
        push dword fmare
        call [printf]
        add esp, 4*2
        
  
        push    dword 0
        call    [exit]
        
        