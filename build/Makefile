CC = gcc
CFLAGS = -I../include -Wall -Werror -Wextra -pedantic -std=c99
SRC_DIR = ../src/
OBJ_DIR = ../build/obj/
BIN_DIR = ../bin/
OBJ_LIST = $(OBJ_DIR)main.o 

PROJ_NAME = c_riscv_comp


# make main.o
$(OBJ_DIR)main.o: $(SRC_DIR)main.c
	$(CC) $(CFLAGS) -c $(SRC_DIR)main.c -o $(OBJ_DIR)main.o

# make all
all: $(OBJ_LIST)
	$(CC) $(CFLAGS) $(OBJ_LIST) -o $(BIN_DIR)$(PROJ_NAME)
