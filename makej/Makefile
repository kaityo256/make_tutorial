INPUTS=$(shell ls input*.dat)
OUTPUTS=$(INPUTS:input%=output%)


all: $(OUTPUTS)

output%: input%
	python convert.py < $< > $@

clean:
	rm -f $(OUTPUTS)
