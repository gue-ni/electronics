# @file Makefile
# @author Jakob G. Maier <e11809618@student.tuwien.ac.at>

CC 	   = gcc
CFLAGS = -Wall -g
LFLAGS = -li2c

PROGS  = test i2c

.PHONY: all clean

all: $(PROGS)

$(PROGS): %: %.o 
	$(CC) -o $@ $^ $(LFLAGS)

%.o: %.c 
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -rf *.o $(PROGS)

