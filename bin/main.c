#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

// read file and save its content to a string
char * read_file_to_string(char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        // TODO ADD A PROPER ERROR HANDLING system
        return NULL;
    }
    fseek(file, 0, SEEK_END);
    long length = ftell(file);
    fseek(file, 0, SEEK_SET);
    char *buffer = malloc(length + 1);
    if (buffer) {
        fread(buffer, 1, length, file);
    }
    fclose(file);
    buffer[length] = '\0';
    return buffer;
}

int compare_strings(char *s1, char *s2) {
        // safely compare two strings
        if (s1 == NULL || s2 == NULL) {
                return 0;
        }
        while (*s1 && *s2) {
                if (*s1 != *s2) {
                        return 0;
                }
                s1++;
                s2++;
        }
        return *s1 ==  *s2;
}


int main(int argc, char *argv[]) {
        if (argc != 2) {
                printf("Usage: %s <filename>\n", argv[0]);
                return 1;
        }
        char *filename = argv[1];
        char *content = read_file_to_string(filename);
        if (content == NULL) {
                printf("Error: Could not read file %s\n", filename);
                return 1;
        }

        if(compare_strings(content,"1 + 1\n"))
                printf("li a0, 1\n li a7, 1\n ecall\n");
        free(content);

        return 0;
}
