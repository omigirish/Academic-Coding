Data Segment
no db 35h
data ends

code segment
assume cs:code,ds:data
start:  mov bl,35h
mov al,bl
AND al,0fh
and bl,0f0h
mov cl,04
rol bl,cl
int 3
code ends
end start
