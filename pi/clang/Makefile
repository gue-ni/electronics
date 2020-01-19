# @file Makefile
# @author Jakob G. Maier <e11809618@student.tuwien.ac.at>

CC 	   = gcc
CFLAGS = -std=c99 -pedantic -Wall -D_DEFAULT_SOURCE -D_BSD_SOURCE -D_SVID_SOURCE -D_POSIX_C_SOURCE=200809L -g
LFLAGS = -li2c

PROGS  = i2c_io

.PHONY: all clean

all: $(PROGS)

$(PROGS): %: %.o 
	$(CC) -o $@ $^ $(LFLAGS)

%.o: %.c 
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -rf *.o $(PROGS)

