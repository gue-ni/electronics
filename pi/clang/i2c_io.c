/**
 * @author Jakob G. Maier
 * @details
 * 
 * Documentation: 
 * https://www.kernel.org/doc/Documentation/i2c/dev-interface 
 */
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <sys/stat.h>

#include <linux/i2c-dev.h>
#include <i2c/smbus.h>

#define I2C "/dev/i2c-1"
#define ADRESS (0x05)
#define BUFSIZE (2)

struct data_buf {
    uint8_t buf[BUFSIZE];
};

void error_exit(char *msg)
{
    fprintf(stderr, "%s\n", msg);
    exit(EXIT_FAILURE);
}

int main(int argc, char **argv)
{
    int fd;

    struct data_buf *data = malloc(sizeof(struct data_buf));

    data->buf[0] = 0x41;
    data->buf[1] = 0x42;
    
    if((fd = open(I2C, O_RDWR)) < 0){
        error_exit("failed to open");
    }

    if(ioctl(fd, I2C_SLAVE, ADRESS) < 0){
        error_exit("ioctl failed");
    }

    if (write(fd, data, BUFSIZE) != BUFSIZE){
        error_exit("write failed");
    }

    if(read(fd, data, BUFSIZE) != BUFSIZE){
        error_exit("read failed");
    }

    printf("Read: %s from slave %d\n", data->buf, ADRESS);

    free(data);

    return EXIT_SUCCESS;
}
