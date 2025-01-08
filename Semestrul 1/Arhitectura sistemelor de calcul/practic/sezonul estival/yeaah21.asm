bits 32
global start


extern exit, scanf,printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll


segment data use32 class=data

    format db "%x",0
    form db "%d",0

    
    a dd 0
    b dd 0
    c dd 0


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
        
        mov eax, [a] ; ax - wordul
        mov ebx, [b] ; bx - wordul
        
        sub eax, [b] ; ax = a-b
        add ebx, [a] ; bx = a+b
        
        mov [c], bx
        mov [c+2], ax
        
        
        
        push dword [c]
        push dword format
        call [printf]
        add esp, 4*2
        
  
        push    dword 0
        call    [exit]
        
        