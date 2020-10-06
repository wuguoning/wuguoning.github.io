set table "meanvalue.pgf-plot.table"; set format "%.5f"
set samples 500.0; plot [x=-1:2] 2*x**2 + x**2*sin(1/x)
