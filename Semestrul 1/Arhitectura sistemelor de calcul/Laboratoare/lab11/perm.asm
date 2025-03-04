bits 32
global permutari        

extern printf
import printf msvcrt.dll


segment code use32 class=code
        permutari:
        mov ecx,[esp+8]
        jecxz gata
        
        
    
        loop_mare:
            push ecx
            push dword [esp+8]
            push dword [esp+20]
            call [printf]
            add esp , 8
            
            
            mov eax, [esp+8]
            mov edx,0
            
            mov ebx,10
            div ebx
            
            ;in edx am restul ; in eax am catul
            push eax
            
            
            mov ecx,[esp+16]
            jecxz gata
            mov eax ,edx
            mov ebx,10
            putere:
                
                mul ebx
                

     
            loop putere
             
            
            pop ebx
            
            add ebx, eax
            mov dword [esp+8], ebx
            
            
            

            pop ecx
        loop loop_mare
        
            push dword [esp+4]
            push dword [esp+16]
            call [printf]
            add esp , 8
        
        gata: 
        ret
