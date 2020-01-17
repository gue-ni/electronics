#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <i2c/smbus.h>
#include <sys/ioctl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <linux/i2c-dev.h>

#define I2C "/dev/i2c-1"
#define ADRESS (0x05)
#define BUFSIZE (4)

void error_exit(char *msg)
{
    fprintf(stderr, "%s\n", msg);
    exit(EXIT_FAILURE);
}

int main(int argc, char **argv)
{

    int fd;
    uint8_t buffer[BUFSIZE];
    buffer[0] = 0x41;
    buffer[1] = 0x42;

    if((fd = open(I2C, O_RDWR)) < 0){
        error_exit("failed to open");
    }

    if(ioctl(fd, I2C_SLAVE, ADRESS) < 0){
        error_exit("ioctl failed");
    }

    if (write(fd, buffer, BUFSIZE) != BUFSIZE){
        error_exit("write failed");
    }

    if(read(fd, buffer, BUFSIZE) != BUFSIZE){
        printf("Read: %s\n", buffer);
    }




    return EXIT_SUCCESS;
}
