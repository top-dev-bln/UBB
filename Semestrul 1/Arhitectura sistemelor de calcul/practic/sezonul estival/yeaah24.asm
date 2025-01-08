bits 32
global start


extern exit, scanf,printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll


segment data use32 class=data

    
    form db "%d",0
    binary_output db "Binary: %s", 10, 0
    string times 32 db '0'
    stop resb 1

    
    a dd 0
    b dd 0
    k dd 17


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
        sub eax, [b]
        
        mov ebx, [k]
        mul ebx
        ; eax = (a-b)*k  fiindca avem numere mici nu trecem pe edx
        
        mov ecx, 32
        
        lea edi, [string+31]
        
        
        convert:
            shr eax, 1
            jc set
            
            jmp next

            set:
                mov byte [edi], '1'
                
            next:
                dec edi
        loop convert
        
        
        
        push dword string
        push binary_output
        call [printf]
        add esp, 4*2
           
      
        
  
        push    dword 0
        call    [exit]
        
        