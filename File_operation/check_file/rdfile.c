/***gcc -o libpycall.so -shared -fPIC rdfile.c*/
#include<stdio.h>
#define F_PATH "/home/lau/下载/2000W/200W-400W.csv"
char c;
int rdfile(char *fpath){
    FILE*fp=NULL;//需要注意
    fp=fopen(fpath,"r");
    if(NULL==fp)
    return -1;//要返回错误代码
//    while(fscanf(fp,"%c",&c)!=EOF) printf("%c",c); //从文本中读入并在控制台打印出来
    fclose(fp);
    fp=NULL;//需要指向空，否则会指向原打开文件地址
    return 0;
}
