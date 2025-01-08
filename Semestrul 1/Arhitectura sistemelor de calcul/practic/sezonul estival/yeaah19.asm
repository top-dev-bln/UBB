bits 32
global start


extern exit, scanf,printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll


segment data use32 class=data

    format db "%d",0
    pozitiv db "DA",0
    negativ db "NU",0
    
    cuvant dd 0
    octet dd 0


segment code use32 class=code

    start:
    
        push dword octet
        push dword format
        call [scanf]
        add esp ,4*2
        
        push dword cuvant
        push dword format
        call [scanf]
        add esp ,4*2
        
      
        mov dl,[octet]
        mov eax,[cuvant]
        
        mov ebx,0
        mov ecx,9
        
        repeta:
            cmp al,dl
            jne invalid
            je gasit
            
            
     
            continue:
            shr eax,1
        loop repeta
        
        

        
        jmp skip
        invalid:
            mov ebx,0
            jmp continue
              
        skip
       
        
        
        push negativ
        call [printf]
        add esp, 4*2
        
        push    dword 0
        call    [exit]
        
        
        gasit:
            push pozitiv
            call [printf]
            add esp, 4*2
            
            push    dword 0
            call    [exit]
        
        