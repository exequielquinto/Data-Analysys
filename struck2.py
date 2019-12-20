#import struct
from struck3 import dec_to_float32, float32_to_msb, float32_to_lsb


def binary(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num))

x=binary(5000)
x1=x[0:16]
x2=x[16:32]
print x
print x1
print x2

y=hex(int(x,2))
y1=hex(int(x1,2))
y2=hex(int(x2,2))
print y
print y1
print y2

z=int(x,2)
z1=int(x1,2)
z2=int(x2,2)
print z
print z1
print z2

print hex(z1)
print hex(z2)

print float32_to_msb(2500)
print float32_to_lsb(2500)

print dec_to_float32(17820, 16384)

print hex(int(16))