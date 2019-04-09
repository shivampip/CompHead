import os
import ioman

def fix_encoding(data):
    out= ''.join(format(ord(x), 'b') for x in data)
    return out 

def fix_uniencoding(data):
    out= ''.join('{:08b}'.format(b) for b in data.encode('utf8'))
    return out


def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)

def test(text=None, in_file=None, enc_data= None, dec_data= None, out_file= None):
    if(text is None):
        text= ioman.read_file(in_file)
    b_eout= fix_uniencoding(text)
    print("\n============Results============")
    print("Input Lenght: \t\t{}".format(len(text)))
    print("Binary Encoding: \t{}".format(len(b_eout)))
    print("Output Encoding: \t{}".format(len(enc_data)))
    if(in_file is not None):
        print("Input File Size:\t{}".format(file_size('files/{}'.format(in_file))))
    if(out_file is not None):
        print("Output File Size:\t{}".format(file_size('files/{}'.format(out_file))))
    print("Compression Ratio:\t{0:.2f}".format((len(enc_data)/len(b_eout))))
    print("Lossless:\t\t{}".format(text==dec_data))
    print("="*31)
