#!/usr/bin/env python

from manimlib.imports import *


class Fraction(Scene):

    def construct(self):
        formula_tex = TextMobject("Fraction: $\\displaystyle\\frac{d}{dx}$")
        self.add(formula_tex)
