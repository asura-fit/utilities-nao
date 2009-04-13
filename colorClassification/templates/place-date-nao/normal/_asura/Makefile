#
# colorClassificationTable(TMAP) Generating System
#
# NAJIMA Hiroki. ASURA 2004
#

THRESH = thresh
COLOR = asuraColors.txt
OUTPUTFILE = normal.tm2
CONVERTER = "/cygdrive/c/Program Files/IrfanView/i_view32"

DIRS := ../Misc ../Ball ../Marker ../Goal ../Nao ../Field ../NearYellowGoal
IMAGE_DIRS := $(wildcard $(addsuffix /*, $(DIRS)))
LABELPSD = $(wildcard $(addsuffix /*/label.psd, $(DIRS)))
#LABELS = $(wildcard $(addsuffix /*/label.ppm, $(DIRS)))
LABELS = $(patsubst %.psd, %.ppm, $(LABELPSD))
YUVIMAGES = $(wildcard $(addsuffix /*/imageyuv.ppm, $(DIRS)))

.PHONY = all clean all-clean result maketile usecache

all: _colors.txt $(LABELS) $(OUTPUTFILE) result

_colors.txt : $(COLOR) _train.txt _test.txt
	@echo "Make Colors"
	@cat $(COLOR) _train.txt _test.txt > _colors.txt

cache.dat : $(YUVIMAGES) $(LABELS) _colors.txt
	@echo "Generating thresh.tm2 without cache..."
	@echo "Enum labelfiles..."
	@echo $(LABELS)
	@echo "done."
	@rm -f cache.dat
	$(THRESH) _colors.txt -c
	@echo "done."

maketile:
	@echo "Generating Tiles..."
	@for dir in $(IMAGE_DIRS); do \
		(cd $$dir; \
		echo $$dir; \
		count=`find . -name \digicame\*.ppm | wc -l`; \
		if [ 0 -ne $$count -a ! -e imageyuv.ppm ]; then \
			tile 3 digicame*.ppm; \
		fi; \
		 \
		); \
	done
	@echo "done."

_test.txt: $(YUVIMAGES) FORCE
	@echo "Generate _test.txt"
	@perl ./maketest.pl $(YUVIMAGES) > _test.txt

_train.txt: $(LABELS) ignorelist.txt FORCE
	@echo "Generate _train.txt"
	@perl ./maketrain.pl $(LABELS) > _train.txt

%.ppm : %.psd
	@echo "Generating $(@D) label.ppm from label.psd"
	@(cd $(@D); $(CONVERTER) $(<F) /convert=$(@F))

thresh.tm2 : cache.dat $(COLOR)
	@echo "Generating thresh.tm2 with cache..."
	$(THRESH) _colors.txt -t
	@echo "done."

result :
	@if [ ! -e cache.dat ] ; then \
		$(MAKE) cache.dat; \
	fi;
	$(MAKE) _colors.txt
	$(THRESH) _colors.txt -r

usecache :
	@if [ ! -e cache.dat ] ; then \
		$(MAKE) cache.dat; \
	fi;
	$(THRESH) _colors.txt

print: 
	@echo YUVIMAGES
	@echo $(YUVIMAGES)
	@echo
	@echo LABELS
	@echo $(LABELS)

$(OUTPUTFILE) : thresh.tm2
	@cp thresh.tm2 $(OUTPUTFILE)

all-clean: clean
	@echo "Removing All Generated Files..."
	@rm -f cache.dat
	@rm -f thresh.tm2 $(OUTPUTFILE)
	@rm -f results/*.ppm
	@rm -f _test.txt _train.txt _colors.txt
	@echo "done."

clean: 
	@rm -f out.ppm color.ppm thresh.log weight*.ppm

rmcache:
	rm cache.dat

FORCE:
