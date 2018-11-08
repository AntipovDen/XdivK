from pyx import canvas, path, deco, style, color, text, trafo
from math import sin, cos, pi, sqrt

def draw_plot():
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


def draw_level_chain():
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


def draw_drop(x, y, r, c):
    c.fill(path.circle(x, y - 3 * r, r), [color.cmyk.RoyalBlue])
    c.stroke(path.circle(x, y - 3 * r, r))

    triangle = path.line(x, y, x + sqrt(8) * r / 3, y - 8 * r / 3) << path.line(x + sqrt(8) * r / 3, y - 8 * r / 3, x - sqrt(8) * r / 3, y - 8 * r / 3)
    triangle.append(path.closepath())
    c.fill(triangle, [color.cmyk.RoyalBlue])
    c.stroke(path.line(x - sqrt(8) * r / 3, y - 8 * r / 3, x, y) << path.line(x, y, x + sqrt(8) * r / 3, y - 8 * r / 3))

    c.fill(path.circle(x - 0.5 * r, (y - 3 * r) / 2, 0.2 * r), [color.rgb.white, trafo.scale(sx=1, sy=2)])

def arrow(x0, y0, x1, y1):
    alpha = 0.3
    beta = 0.5
    x2 = x1 + (x1 - x0) * alpha
    y2 = y1 + (y1 - y0) * alpha
    x3 = x2 + (y1 - y0) * beta
    y3 = y2 + (x0 - x1) * beta
    x4 = x2 - (y1 - y0) * beta
    y4 = y2 - (x0 - x1) * beta
    arrow = path.line(x0, y0, x3, y3) << path.line(x3, y3, x1, y1) << path.line(x1, y1, x4, y4)
    arrow.append(path.closepath())
    return arrow

def pipe(x0, y0, x1, y1, x2, y2, x3, y3, c, x):
    c.stroke(path.curve(x0, y0, x1, y1, x2, y2, x3, y3), [color.rgb.black, style.linewidth(width=0.6 * x / 24)])
    c.stroke(path.curve(x0, y0, x1, y1, x2, y2, x3, y3), [color.cmyk.RoyalBlue, style.linewidth(width=0.5 * x / 24)])


def state(x0, y0, r, c):
    x1 = x0 - r/sqrt(2)
    y1 = y0 + r/sqrt(2)
    x2 = x0 - 3 * r / 4 / sqrt(2)
    y2 = y1 + r/8
    x3 = x0 - r / 4 / sqrt(2)
    y3 = y1 - r/8
    x4 = x0 + r / 4 / sqrt(2)
    y4 = y1 + r/8
    x5 = x0 + 3 * r / 4 / sqrt(2)
    y5 = y1 - r/8
    x6 = x0 + r/sqrt(2)
    y6 = y1
    delta = r / 40

    c.fill(path.circle(x0, y0, r), [color.cmyk.RoyalBlue])
    c.fill(path.rect(x1 + delta, y0 + delta, r * sqrt(2) - 2 * delta, r), [color.rgb.white])

    inside = path.curve(x1, y1, x2, y2, x3, y3, x0, y1) << \
             path.curve(x0, y1, x4, y4, x5, y5, x6, y6) << \
             path.line(x6, y6, x6, y0) << \
             path.line(x6, y0, x1, y0)
    inside.append(path.closepath())
    c.fill(inside, [color.cmyk.RoyalBlue])
    c.stroke(path.circle(x0, y0, r), [style.linewidth(r/25)])


def draw_leaky_chain():
    c = canvas.canvas()

    x = 6
    r = x/6

    pipe(sqrt(0.75) * r, r / 2, x / 3, r, 2 * x / 3, r, 19/24 * x, 0.65 * r, c, x)
    c.fill(arrow(x - sqrt(0.75) * r, r / 2, 19 / 24 * x, 0.65 * r), [color.rgb.black])

    pipe(x - sqrt(0.75) * r, - r / 2, 2 * x / 3, -r, x / 3, -r, 5 / 24 * x, -0.65 * r, c, x)
    c.fill(arrow(sqrt(0.75) * r, -r / 2, 5 / 24 * x, -0.65 * r), [color.rgb.black])

    pipe(x + sqrt(0.75) * r, r / 2, 1.5 * x, r, x * 1.5, -r, x + 5 / 4 * r, -2.3 / 4 * r, c, x)
    c.fill(arrow(x + sqrt(0.75) * r, -r / 2, x + 5 / 4 * r, -2.3 / 4 * r))

    pipe(-sqrt(0.75) * r, -r / 2, -0.5 * x, -r, -x * 0.5, r, -5 / 4 * r, 2.3 / 4 * r, c, x)
    c.fill(arrow(-sqrt(0.75) * r, r / 2, -5 / 4 * r, 2.3 / 4 * r))

    state(0, 0, r, c)
    state(x, 0, r, c)


    c.text(-x * 0.2, r, r"\Pr[0 \to 0]", [text.halign.boxright, text.mathmode, text.size.large])
    c.text(x * 1.2, r, r"\Pr[1 \to 1]", [text.halign.boxleft, text.mathmode, text.size.large])
    c.text(x * 0.5, 5/4 * r, r"\Pr[0 \to 1]", [text.valign.bottom, text.halign.boxcenter, text.mathmode, text.size.large])
    c.text(x * 0.5, -5 / 4 * r, r"\Pr[1 \to 0]", [text.valign.top, text.halign.boxcenter, text.mathmode, text.size.large])

    c.text(0, 0, r"0", [color.rgb.white, text.halign.boxcenter, text.valign.middle, text.mathmode, text.size.Huge])
    c.text(x, 0, r"1", [color.rgb.white, text.halign.boxcenter, text.valign.middle, text.mathmode, text.size.Huge])

    draw_drop(0, -5/4 * r, r/4, c)
    draw_drop(x, -7/4 * r, r/4, c)

    water = path.curve(-5/4 * r, -x/2, -5/4 * r + 17/72 * x, -x / 2 - x/48, -5/4 * r + 34/72 * x, -x/2 + x / 48, x/2, -x/2) << \
            path.curve(x/2, -x/2, x/2 + 17/72 * x, -x/2 - x /48, x/2 + 34/72 * x, -x/2 + x/48, x + 5/4 * r, -x/2) << \
            path.line(x + 5/4 * r, -x/2, x + 5/4 * r, -7/12 * x) << path.line(x + 5/4 * r, -7/12 * x, -5/4 * r, -7/12 * x)
    water.append(path.closepath())
    c.fill(water, [color.cmyk.RoyalBlue])
    c.stroke(path.line(-5/4 * r, -11 / 24 * x, -5/4 * r, -7/12 * x) << path.line(-5/4 * r, -7/12 * x, x + 5/4 * r, -7/12 * x) << path.line(x + 5/4 * r, -7/12 * x, x + 5/4 * r, -11/24 * x), [style.linewidth.THICK])



    c.writePDFfile("leaky_chain.pdf")



draw_leaky_chain()