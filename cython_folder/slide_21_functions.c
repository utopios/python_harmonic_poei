#include <stdio.h>
#include <dirent.h>
void getDirectory(const char* folder) { DIR *d;
struct dirent *dir;
d = opendir(folder);
if (d) {
while ((dir = readdir(d)) != NULL) {
printf("%s\n", dir->d_name); }
closedir(d); }
}