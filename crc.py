# program for error detecting code using crc - ccitt (16 bits)

def xor(val1, val2):
  result = ''
  for i in range(len(val1)):
    if val1[i] == val2[i]:
      result += '0'
    else:
      result += '1'
  return result[1:]

def binary_division(modified_dataword, divisor, dataword):
  track = len(divisor)
  currval = modified_dataword[:len(divisor)]
  while track < len(modified_dataword):
    if currval[0] == '0':
      currval = xor(currval, '0'*len(divisor)) + modified_dataword[track]
    else:
      currval = xor(currval, divisor) + modified_dataword[track]
    track += 1
  if currval[0] == '0':
    currval = xor(currval, '0'*len(divisor)) 
  else:
    currval = xor(currval, divisor)
  return currval

def main():
  dataword = input('enter dataword: ')

  divisor = '10011000000100001'
  print('divisor: ', divisor)
  
  modified_dataword = dataword + (len(divisor)-1)*'0'
  print('modified dataword: ', modified_dataword)
  
  codeword = dataword + binary_division(modified_dataword, divisor, dataword)
  print('codeword: ', codeword)

  check_cw = binary_division(codeword, divisor, dataword)
  print('checking the codeword , syndrome:', check_cw)

main()
