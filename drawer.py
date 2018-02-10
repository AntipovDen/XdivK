from pyx import canvas, path, deco, style, color, text
from math import sin, cos, pi, sqrt

if True:
    c = canvas.canvas()
    #axis
    c.stroke(path.line(0, 0, 12, 0), [deco.earrow(size=0.5)])
    c.stroke(path.line(0, 0, 0, 6), [deco.earrow(size=0.5)])
    #dashed lines
    c.stroke(path.line(0, 5, 10, 5), [style.linestyle.dashed, style.linewidth.thin])
    c.stroke(path.line(10, 0, 10, 5), [style.linestyle.dashed, style.linewidth.thin])
    # c.stroke(path.line(0, 0, 20, 10), [style.linestyle.dashed])

    c.stroke(path.line(0, 3.75, 7.5, 3.75), [style.linestyle.dashed, style.linewidth.thin])
    c.stroke(path.line(7.5, 0, 7.5, 3.75), [style.linestyle.dashed, style.linewidth.thin])


    #plot
    c.stroke(path.line(0, 0, 7.5, 3.75), [style.linewidth.THICK])
    c.stroke(path.line(7.5, 3.75, 10, 3.75), [style.linewidth.THICK])
    c.stroke(path.circle(10, 5, 0.18))
    c.fill(path.circle(10, 5, 0.18), [color.rgb.black])
    c.stroke(path.circle(10, 3.75, 0.18))
    c.fill(path.circle(10, 3.75, 0.18), [color.rgb.white])

    #text
    c.text(-0.2, 6, r"Plateau$(x)$", [text.halign.boxright, text.valign.top, text.size.Huge])
    c.text(13, -0.2, r"OneMax$(x)$", [text.halign.boxcenter, text.valign.top, text.size.Huge])

    c.text(0, 5, r"$n$", [text.halign.boxright, text.valign.top, text.size.Huge])
    c.text(0, 3.75, r"$n - k$", [text.halign.boxright, text.valign.middle, text.size.Huge])

    c.text(0, 0, r"$0$", [text.halign.boxright, text.valign.top, text.size.Huge])

    c.text(7.5, -0.2, r"$n - k$", [text.halign.boxcenter, text.valign.top, text.size.Huge])
    c.text(10, -0.2, r"$n$", [text.halign.boxcenter, text.valign.top, text.size.Huge])


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

c = canvas.canvas()

# levels circles
# for r in 3, 8, 11:
#     circle = path.circle(11, 0, r)
#     intersect = (circle.intersect(path.line(0, 2.6, 11, 2.6))[0][0], circle.intersect(path.line(0, -2.2, 11, -2.1))[0][0])
#     arc = circle.split(intersect)[1]
#     c.stroke(arc, [style.linestyle.dashed, style.linewidth.thin])

#states
c.stroke(path.circle(0, 0, 0.4))
c.stroke(path.circle(3, 0, 0.4))
c.stroke(path.circle(8, 0, 0.4))
c.stroke(path.circle(11, 0, 0.4))
c.fill(path.circle(0, 0, 0.4), [color.rgb.white])
c.fill(path.circle(3, 0, 0.4), [color.rgb.white])
c.fill(path.circle(8, 0, 0.4), [color.rgb.white])
c.fill(path.circle(11, 0, 0.4), [color.rgb.black])
c.text(0, 0, r"0", [text.halign.boxcenter, text.valign.middle, text.size.huge])
c.text(3, 0, r"1", [text.halign.boxcenter, text.valign.middle, text.size.huge])
c.text(8, 0, r"$k - 1$", [text.size.small, text.halign.boxcenter, text.valign.middle])

#dots
c.fill(path.circle(6, 0, 0.1), [color.rgb.black])
c.fill(path.circle(5, 0, 0.1), [color.rgb.black])
c.fill(path.circle(5.5, 0, 0.1), [color.rgb.black])


#transitions
c.stroke(path.line(sqrt(0.15), 0.1, 3 - sqrt(0.15), 0.1), [deco.earrow()])
c.text(1.5, 0.1, r"$p_0^1$", [text.halign.boxcenter, text.valign.bottom])
c.stroke(path.line(3 - sqrt(0.15), -0.1, sqrt(0.15), -0.1), [deco.earrow()])
c.text(1.5, -0.1, r"$p_1^0$", [text.halign.boxcenter, text.valign.top])
c.stroke(path.curve(3 + sqrt(0.15), 0.1, 5, 0.4, 6, 0.4, 8 - sqrt(0.15), 0.1), [deco.arrow()])
c.text(5.5, 0.4, r"$p_1^{k - 1}$", [text.halign.boxcenter, text.valign.bottom])
c.stroke(path.curve(8 - sqrt(0.15), -0.1, 6, -0.4, 5, -0.4, 3 + sqrt(0.15), -0.1), [deco.arrow()])
c.text(5.5, -0.4, r"$p_{k - 1}^1$", [text.halign.boxcenter, text.valign.top])
c.stroke(path.line(8.4, 0, 10.6, 0), [deco.earrow()])
c.text(9.5, 0, r"$p_{k - 1}^k$", [text.halign.boxcenter, text.valign.bottom])
c.stroke(path.curve(0, 0.4, 3, 2.7, 8, 2.7, 11, 0.4), [deco.arrow()])
c.text(5.5, 2.2, r"$p_0^k$", [text.halign.boxcenter, text.valign.bottom])
c.stroke(path.curve(sqrt(0.07), 0.3, 3, 2, 5, 2, 8 - sqrt(0.07), 0.3), [deco.arrow()])
c.text(4.5, 1.6, r"$p_0^{k - 1}$", [text.halign.boxcenter, text.valign.bottom])
c.stroke(path.curve(8 - sqrt(0.12), 0.2, 5, 1.9, 3, 1.9, sqrt(0.12), 0.2), [deco.arrow()])
c.text(4.5, 1.4, r"$p_{k - 1}^0$", [text.halign.boxcenter, text.valign.top])
c.stroke(path.curve(3 + sqrt(0.07), -0.3, 6, -2, 9, -2, 11 - sqrt(0.07), -0.3), [deco.arrow()])
c.text(7, -1.7, r"$p_1^k$", [text.halign.boxcenter, text.valign.top])
c.stroke(path.curve(-sqrt(0.07), -0.3, -0.3, -1, 0.3, -1, sqrt(0.07), -0.3), [deco.earrow])
c.text(0, -1, r"$p_0^0$", [text.halign.boxcenter, text.valign.top])
c.stroke(path.curve(3 - sqrt(0.07), -0.3, 3-0.3, -1, 3.3, -1, 3 + sqrt(0.07), -0.3), [deco.earrow])
c.text(3, -1, r"$p_1^1$", [text.halign.boxcenter, text.valign.top])
c.stroke(path.curve(8 - sqrt(0.07), -0.3, 8-0.3, -1, 8.3, -1, 8 + sqrt(0.07), -0.3), [deco.earrow])
c.text(8, -1, r"$p_{k - 1}^{k - 1}$", [text.halign.boxcenter, text.valign.top])



c.writePDFfile("levels_chain.pdf")