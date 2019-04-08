
def fix_encoding(data):
    out= ''.join(format(ord(x), 'b') for x in data)
    return out 

def input_info(data):
    print("Input Lenght: \t{}".format(len(data)))
    b_eout= fix_encoding(data)
    print("Binary Encoding: \t{}".format(len(b_eout)))

def test(inputd, output, decoded):
    b_eout= fix_encoding(inputd)
    print("\n============Results============")
    print("Input Lenght: \t\t{}".format(len(inputd)))
    print("Binary Encoding: \t{}".format(len(b_eout)))
    print("Output Encoding: \t{}".format(len(output)))
    print("Compression Ratio:\t{0:.2f}".format(len(output)/len(b_eout)))
    print("Lossless:\t\t{}".format(inputd==decoded))
    print("="*31)