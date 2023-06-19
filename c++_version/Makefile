# Makefile

# Compiler
CC := g++

# Compiler flags
CFLAGS := -c
LDFLAGS := -lsfml-graphics -lsfml-system -lsfml-window

# Source file
SRC := main.cc

# Object file
OBJ := $(SRC:.cc=.o)

# Executable name
EXEC := sfml-app

# Default target
all: $(EXEC)

# Compile source file
$(OBJ): $(SRC)
	$(CC) $(CFLAGS) $< -o $@

# Link object file to create executable
$(EXEC): $(OBJ)
	$(CC) $< -o $@ $(LDFLAGS)

# Clean object and executable files
clean:
	rm -f $(OBJ) $(EXEC)

# Declare the `clean` target as phony
.PHONY: clean
