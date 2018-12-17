OUTDIR := notebooks
ZIPFILE := notebooks.zip

zip:
	mkdir $(OUTDIR)
	ln *.ipynb $(OUTDIR)
	zip -r $(ZIPFILE) $(OUTDIR)

clean:
	rm -rf $(OUTDIR) $(ZIPFILE)
