
SRCS = $(wildcard *_build.py)
OBJDIR = ctest
_OBJ = cp36-win_amd64.pyd

PROGS = $(patsubst %_build.py,$(OBJDIR)/_%.$(_OBJ),$(SRCS))

main: ctest
	python $@.py

ctest: $(PROGS)
	@echo Building ... 
	@rm -rf Release

$(OBJDIR)/_%.$(_OBJ): %_build.py
	python $< 

clean:
	rm -rf ctest/* Release
