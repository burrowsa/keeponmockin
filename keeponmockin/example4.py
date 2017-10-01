def generate_file(filename):
    with open(filename, 'w') as f:
        f.write(u"hello world\n")
        f.writelines([u"hello moon\n",
                      u"hello space\n"])
        f.write(u"hello universe\n")
