add x1, x1, x12
sub x4, x2, x3
beq x1, x4, 2
sub x1, x2, x12
sll x1, x2, x4
bne x2, x3, 3
xor x7, x1, x4
and x8, x7, x3
srl x1, x1, x4
blt x1, x4, 4
bge x1, x4, 2
add x9, x4, x3
bltu x2, x3, 5
bgeu x4, x1, 2
add x10, x1, x2