#include <stdio.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>

int rd(char *filename)
{
    int fd;
    int size_read;
    char buffer[800000];
    fd = open(filename, O_RDONLY);
    size_read = read(fd, buffer, sizeof(buffer));
    while (size_read > 0) /*循环读取数据*/
    {
        if (size_read < sizeof(buffer))
        {
            buffer[size_read] = '\0';
        }
//        printf("%s\n", buffer);
        size_read = read(fd, buffer, sizeof(buffer) - 1);
    }
    if (size_read == -1) /*如果出错*/
    {
        perror("Error reading");
        return -1;
    }
    close(fd);
    return 0;
}
