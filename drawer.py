from pyx import canvas, path, deco, style, color, text
from math import sin, cos, pi


c = canvas.canvas()
#axis
c.stroke(path.line(0, 0, 23, 0), [deco.earrow(size=0.5)])
c.stroke(path.line(0, 0, 0, 11), [deco.earrow(size=0.5)])
#dashed lines
c.stroke(path.line(0, 10, 20, 10), [style.linestyle.dashed])
c.stroke(path.line(20, 0, 20, 10), [style.linestyle.dashed])
c.stroke(path.line(0, 0, 20, 10), [style.linestyle.dashed])

c.stroke(path.line(0, 7.5, 15, 7.5), [style.linestyle.dashed])
c.stroke(path.line(15, 0, 15, 7.5), [style.linestyle.dashed])


#plot
c.stroke(path.line(0, 0, 15, 7.5), [style.linewidth.THICK])
c.stroke(path.line(15, 7.5, 20, 7.5), [style.linewidth.THICK])
c.stroke(path.circle(20, 10, 0.1), [style.linewidth.THICK])
c.stroke(path.circle(20, 7.5, 0.18))
c.fill(path.circle(20, 7.5, 0.18), [color.rgb.white])

#text
c.text(-0.2, 11, r"Plateau$(x)$", [text.halign.boxright, text.valign.top, text.size.Huge])
c.text(23, -0.2, r"OneMax$(x)$", [text.halign.boxcenter, text.valign.top, text.size.Huge])

c.text(0, 10, r"$n$", [text.halign.boxright, text.valign.top, text.size.Huge])
c.text(0, 7.5, r"$n - k$", [text.halign.boxright, text.valign.middle, text.size.Huge])

c.text(0, 0, r"$0$", [text.halign.boxright, text.valign.top, text.size.Huge])

c.text(15, -0.2, r"$n - k$", [text.halign.boxcenter, text.valign.top, text.size.Huge])
c.text(20, -0.2, r"$n$", [text.halign.boxcenter, text.valign.top, text.size.Huge])


c.writePDFfile("plateau.pdf")

c = canvas.canvas()

c.stroke(path.circle(0, 0, 0.18))
c.fill(path.circle(0, 0, 0.18), [color.rgb.black])
c.text(0.18, 0, r"Opt", [text.halign.boxleft, text.valign.middle, text.size.Huge])

n_level = 20
for i in range(n_level):
    if i not in range(8, 13):
        c.stroke(path.circle(2 * sin(i * pi * 2 / n_level), 2 * cos(i * pi * 2 / n_level), 0.18))
c.text(0, -2, r"Level $(k - 1)$", [text.halign.boxcenter, text.valign.bottom, text.size.LARGE])

n_level = 40
for i in range(n_level):
    if i not in range(18, 23):
        c.stroke(path.circle(4 * sin(i * pi * 2 / n_level), 4 * cos(i * pi * 2 / n_level), 0.18))
c.text(0, -4, r"Level $(k - 2)$", [text.halign.boxcenter, text.valign.bottom, text.size.LARGE])

c.stroke(path.circle(0, 0, 5), [style.linestyle.dotted, style.linewidth.thick])

n_level = 60
for i in range(n_level):
    if i not in range(29, 32):
        c.stroke(path.circle(6 * sin(i * pi * 2 / n_level), 6 * cos(i * pi * 2 / n_level), 0.18))
c.text(0, -6, r"Level $0$", [text.halign.boxcenter, text.valign.bottom, text.size.LARGE])
c.writePDFfile("individuals_chain.pdf")