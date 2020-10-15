set terminal postscript portrait enhanced color dashed lw 1 "DejaVuSans" 12
set output "fun2.ps"
f(x) = 2*x*x*x + x*x*x*sin(1/(x*x))

set xlabel "x"
set ylabel "y"
set mxtics
set xrange [-0.1:0.1]
set yrange [-0.0015:0.0015]
set samples 1000
set size ratio 0.8
unset key

#plot
plot f(x) notitle
