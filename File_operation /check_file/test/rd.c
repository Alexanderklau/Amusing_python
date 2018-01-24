/***gcc -o libpycall.so -shared -fPIC rd.c*/
#include<stdio.h>
#include<pthread.h>

#include<sys/types.h>
#include<sys/syscall.h>
#include<unistd.h>

#include<stdlib.h>
#include<assert.h>

const int buf_size=1024;
const int buf_size2=1024*2;

/*获取线程的id必须使用syscall，不能直接使用pthread_t
*pthread_t 的结构体实际是：
*typedef struct {
*   void * p;                   // Pointer to actual object 
*   unsigned int x;            // Extra information - reuse count etc 
*} ptw32_handle_t;
*/
pid_t gettid()
{
    return syscall(__NR_gettid);
}

/*文件读取线程，实现对一个或多个文件的读写*/
void * func(void * args){
    FILE* fp=(FILE*)args;
    int count=0;
    int read_count=0;
    char * buf;
    int size;
    pid_t tid=gettid();
    int sleep_time;

    if(tid%2==0){
        size=buf_size;
        sleep_time=50;
    }
    else{
        size=buf_size2;
        sleep_time=100;
    }

    buf=(char *)malloc(size);
    printf("the tid is %d, malloc size is %d\n", tid, size);
    while(!feof(fp)){
        count+=fread(buf, 1, size, fp);
        read_count++;
        usleep(sleep_time);
    }
    printf("thread [%d] read count is %d, read size is %d\n", tid, read_count, count);
    pthread_exit("thread exit");
}

int rd(char *rd_path)
{
    FILE* fd=fopen(rd_path,"r");
    if(NULL==fd)
    return -1;
    // printf("bitch!");
    pthread_t ntid[4];
    int err;
    int i=0;
	
	/*多个线程同时对一个文件执行读操作，最后每个线程*/
    for(i=0; i<5; i++){
        err=pthread_create(&ntid[i], NULL, func, fd);
        if(err!=0){
            printf("can't create a new thread");
        }
    }
	
    for(i=0; i<5; i++)
        pthread_join(ntid[i], NULL);
    return 0;
}
