Data Segment
data ends
code segment
start:  mov ax,0fffeh
mov dx,000fh
mov bx,0fffh
div bx
int 3
code ends
end start
