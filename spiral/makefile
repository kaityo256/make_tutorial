DAT=$(shell ls *.dat)
PNG=$(DAT:%.dat=%.png)

all: $(PNG)


%.png: %.dat
	python convert.py $<


gif: $(PNG)
	convert -delay 5 -loop 0 -resize 50% spiral*.png spiral.gif

clean:
	rm -f spiral.gif spiral*.dat spiral*.png
