#!/usr/bin/env python3
# Random number reader.
#
# Reads numbers from a file filled with random numbers.

class MyRNG:
    # NOTE: IF updating these directories,
    # ##### then also update them in __del__() and __intit__()
    random_dir = "/media/me/Data/Random/"
    random_file = "file1.bin"
    random_index = "index"
    f_random = 0
    f_index = 0
    index = 0
    prev_width = 0
    bbs = 0 # Best byte size
    def __init__(self):
        from functions import cast_number
        # NOTE: IF updating these directories,
        # ##### then also update them in __del__()
        #random_dir = "/media/me/Data/Random/"
        #random_file = "file1.bin"
        #random_index = "index"
        self.f_random = open(self.random_dir+self.random_file, "rb")
        with open(self.random_dir+self.random_index, "rt") as f:
            self.index = cast_number(f.read())
        if self.index:
            self.f_random.seek(self.index)
        else:
            print("Index not found.")
    def __del__(self):
        try:
            new_index = self.f_random.tell()
            #print(f"New index? {new_index}")
            with open(self.random_dir+self.random_index, "wt") as f:
                f.write(str(new_index))
            self.f_random.close()
        except ValueError or NameError:
            print("Unable to update index automatically")
            from functions import cast_number
            # If we don't know exact index,
            # then just add a prime so it will be different
            # next time.
            # index might already be deleted.
            random_dir = "/media/me/Data/Random/"
            random_file = "file1.bin"
            random_index = "index"
            with open(random_dir+random_index, "rt") as f:
                f.seek(0) # back to start of file, just in case
                index = f.read()
            if index:
                print(f"Index is {index}, type:{type(index)}")
                index = cast_number(index)
            else:
                print(f"Resetting index. It didn't work. index={index}, "
                + f"type:{type(index)}")
                index = 0
            # erase old index file.
            with open(random_dir+random_index, "wt") as f:
                f.write(str(int(index)+1031))
    def rand_bytes(self, num):
        from functions import bytes_to_int
        rand = self.f_random.read(num)
        return bytes_to_int(rand)
    def rand_range(self, width):
        from functions import lookup_best_byte_size
        from functions import bytes_to_int
        size = 0
        if width == self.prev_width:
            size =self.bbs
        else:
            size = lookup_best_byte_size(width)
            self.bbs = size
        self.prev_width = width
        rand = self.rand_bytes(size)
        return rand%width
