# from author @Micoael_Primo
from manim_sandbox.videos.manimTutorial.utils import *


class Scene_0(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }

    def construct(self):
        captions = [
            "下面我们来看next_to方法",
            "顾名思义,next_to表示紧挨着一个物体",
            "比如我们想让一个方块挨着一个圆圈就可以这样写",
            "所以可以用a.next_to(b)来快速安排位置"

        ]
        commands = [
            "c = Circle(radius=0.5)",
            "sq = Square(side_length=0.5)",
            "c.next_to(sq)",

        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Medium', size=0.32).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
        c = Circle(radius=0.5).shift(LEFT * 2)
        sq = Square(side_length=0.5, fill_color=BLUE, fill_opacity=1.0).shift(LEFT * 2)

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = UP * 2.9 + RIGHT * 3.1
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)

        coms = VGroup(
            *[
                CodeLine(com, font='Consolas', size=0.28).move_to(loc)
                for com in commands
            ]
        )

        self.play(FadeInFromDown(tex_bg))
        self.play(Write(caps[0]))
        self.wait()
        self.play(ReplacementTransform(caps[0], caps[1]))
        self.wait(2)

        self.play(ReplacementTransform(caps[1], caps[2]))
        self.wait()

        self.play(Write(coms[0]))
        self.play(ShowCreation(c))
        self.play(Write(coms[1].next_to(coms[0], DOWN, aligned_edge=LEFT)))
        self.play(ShowCreation(sq))
        self.play(Write(coms[2].next_to(coms[1], DOWN, aligned_edge=LEFT)))
        self.play(c.next_to, sq)

        self.play(ReplacementTransform(caps[2], caps[3]))
        self.wait()


class Scene_1(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }

    def construct(self):
        captions = [
            "除此之外,我们可以指定next_to的方向。",
            "分别是UP,DOWN,LEFT,RIGHT",
            "表示相邻的位置",
            "那么就可以用a.next_to(b,方向)排顺序"

        ]
        commands = [
            "c.next_to(sq,UP)",
            "c.next_to(sq,DOWN)",
            "c.next_to(sq,LEFT)",
            "c.next_to(sq,RIGHT)"

        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Medium', size=0.32).to_edge(DOWN * 1.2)
                for cap in captions
            ]
        )
        c = Circle(radius=0.5).shift(LEFT * 2)
        sq = Square(side_length=0.5, fill_color=BLUE, fill_opacity=1.0).shift(LEFT * 2)

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = UP * 2.9 + RIGHT * 3.1
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)

        oria = CodeLine("c = Circle(radius=0.5)", font='Consolas', size=0.28).move_to(loc)
        orib = CodeLine("sq = Square(side_length=0.5)", font='Consolas', size=0.28).move_to(loc)
        oric = CodeLine("c.next_to(sq)", font='Consolas', size=0.28).move_to(loc)
        self.add(oria)
        self.add(orib.next_to(oria, DOWN, aligned_edge=LEFT))
        self.add(oric.next_to(orib, DOWN, aligned_edge=LEFT))

        coms = VGroup(
            *[
                CodeLine(com, font='Consolas', size=0.28).next_to(oric, DOWN, aligned_edge=LEFT)
                for com in commands
            ]
        )

        self.add(tex_bg)
        self.add(c, sq)
        c.next_to(sq)

        self.play(Write(caps[0]))
        self.play(ReplacementTransform(caps[0], caps[1]))

        def change(what, where):
            self.play(ReplacementTransform(what[where - 1], what[where]))

        self.play(Write(coms[0].next_to(oric, DOWN, aligned_edge=LEFT)))
        self.play(c.shift, UP + LEFT)
        change(coms, 1)
        self.play(c.shift, 2 * DOWN)
        change(coms, 2)
        self.play(c.shift, UP + LEFT)
        change(coms, 3)
        self.play(c.shift, 2 * RIGHT)
        change(caps, 2)
        self.wait(2)
        change(caps, 3)
        self.wait(2)


class Scene_2(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }

    def construct(self):
        captions = [
            "有时候我们还可能实现类似于上/下/左/右对齐的功能",
            "这时候可以加入aligned_edge=方向",
            "这有5种取值方式:UP，DOWN，LEFT，RIGHT，ORIGIN",
            "如果要加入对齐,可以这样写：a.next_to(b,方向,aligned_edge=取值)"

        ]
        commands = [
            "c.next_to(sq,RIGHT,aligned_edge=UP)",
            "c.next_to(sq,RIGHT,aligned_edge=DOWN)",
            "c.next_to(sq,DOWN,aligned_edge=LEFT)",
            "c.next_to(sq,DOWN,aligned_edge=RIGHT)",
            "c.next_to(sq,DOWN,aligned_edge=ORIGIN)"

        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Medium', size=0.33).shift(DOWN * 3.4)
                for cap in captions
            ]
        )
        c = Circle(radius=0.5).shift(LEFT * 2)
        sq = Square(side_length=0.5, fill_color=BLUE, fill_opacity=1.0).shift(LEFT * 2)

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = UP * 2.9 + RIGHT * 3
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)

        oria = CodeLine("c = Circle(radius=0.5)", font='Consolas', size=0.21).move_to(loc)
        orib = CodeLine("sq = Square(side_length=0.5)", font='Consolas', size=0.21).move_to(loc)
        oric = CodeLine("c.next_to(sq)", font='Consolas', size=0.21).move_to(loc)
        self.add(oria)
        self.add(orib.next_to(oria, DOWN, aligned_edge=LEFT))
        self.add(oric.next_to(orib, DOWN, aligned_edge=LEFT))

        coms = VGroup(
            *[
                CodeLine(com, font='Consolas', size=0.21).next_to(oric, DOWN, aligned_edge=LEFT)
                for com in commands
            ]
        )

        self.add(tex_bg)
        self.add(c, sq)
        c.next_to(sq)

        def change(what, where):
            self.play(ReplacementTransform(what[where - 1], what[where]))
            self.wait()

        up = c.copy().next_to(sq, RIGHT, aligned_edge=UP)
        down = c.copy().next_to(sq, RIGHT, aligned_edge=DOWN)
        left = c.copy().next_to(sq, DOWN, aligned_edge=LEFT)
        right = c.copy().next_to(sq, DOWN, aligned_edge=RIGHT)
        origin = c.copy().next_to(sq, DOWN, aligned_edge=ORIGIN)

        self.play(Write(caps[0]))
        self.wait()
        change(caps, 1)
        self.wait()

        change(caps, 2)
        self.wait()

        self.play(Write(coms[0]))
        self.play(ReplacementTransform(c, up))
        change(coms, 1)
        self.play(ReplacementTransform(up, down))
        change(coms, 2)
        self.play(ReplacementTransform(down, left))
        change(coms, 3)
        self.play(ReplacementTransform(left, right))
        change(coms, 4)
        self.play(ReplacementTransform(right, origin))

        change(caps, 3)
        self.wait()


class Scene_3(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }

    def construct(self):
        captions = [
            "如果觉得默认的距离不够好的话",
            "可以加入一些缓冲区buff.",
            "可以写作一个关键词buff=缓冲大小",
            "像这样：a.next_to(b,方向,buff=取值)"

        ]
        commands = [
            "c.next_to(sq,RIGHT,aligned_edge=UP)",
            "c.next_to(sq,RIGHT,aligned_edge=DOWN)",
            "c.next_to(sq,DOWN,aligned_edge=LEFT)",
            "c.next_to(sq,DOWN,aligned_edge=RIGHT)",
            "c.next_to(sq,DOWN,aligned_edge=ORIGIN)"

        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Medium', size=0.33).shift(DOWN * 3.4)
                for cap in captions
            ]
        )
        c = Circle(radius=0.5).shift(LEFT * 2)
        sq = Square(side_length=0.5, fill_color=BLUE, fill_opacity=1.0).shift(LEFT * 2)

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = 2.9 * UP + RIGHT * 3
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        oria = CodeLine("c = Circle(radius=0.5)", font='Consolas', size=0.28).move_to(loc)
        orib = CodeLine("sq = Square(side_length=0.5)", font='Consolas', size=0.28).move_to(loc)
        oric = CodeLine("c.next_to(sq)", font='Consolas', size=0.28).move_to(loc)
        self.add(oria)
        self.add(orib.next_to(oria, DOWN, aligned_edge=LEFT))
        self.add(oric.next_to(orib, DOWN, aligned_edge=LEFT))
        coms = VGroup(
            *[
                CodeLine(com, font='Consolas', size=0.21).next_to(oric, DOWN, aligned_edge=LEFT)
                for com in commands
            ]
        )

        self.add(tex_bg)
        self.add(c, sq)
        c.next_to(sq, DOWN)

        def change(what, where):
            self.play(ReplacementTransform(what[where - 1], what[where]))
            self.wait()

        self.play(Write(caps[0]))
        change(caps, 1)
        a = DoubleArrow((sq.get_center()), (c.get_center()), color=BLUE)
        tx = CodeLine("c.next_to(sq,DOWN,buff=2.5)", font='Consolas', size=0.28).next_to(oric, DOWN, aligned_edge=LEFT)

        def upr(obj):
            obj.become(CodeLine(
                "c.next_to(sq,DOWN,buff=" + str(round(sq.get_center()[1] - c.get_center()[1] - 1 + 0.25, 2)) + ")",
                font='Consolas', size=0.28).next_to(oric, DOWN, aligned_edge=LEFT))
            if sq.get_center()[1] - c.get_center()[1] - 1 + 0.25 > 0:
                a.become(DoubleArrow((sq.get_center()), (c.get_center() + 0.2 * UP), color=BLUE))
            else:
                a.become(DoubleArrow((sq.get_center()), (c.get_center() + 0.2 * DOWN), color=BLUE))
            tx.become(Text("buff=" + str(round(sq.get_center()[1] - c.get_center()[1] - 1 + 0.25, 2)), size=0.28,
                           font="Consolas", color=BLACK).move_to(a))

        cod = CodeLine("buff=" + str(round(sq.get_center()[1] - c.get_center()[1] - 1 + 0.25, 2)), font='Consolas',
                       size=0.25).move_to(loc)
        cod.add_updater(upr)
        self.play(Write(cod), Write(a), Write(tx))
        self.play(c.shift, 3 * DOWN, runselftime=3)
        self.play(c.shift, 3 * UP, runselftime=3)
        cod.remove_updater(upr)
        self.wait()
        change(caps, 2)


class Scene_4(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        }
    }

    def construct(self):
        captions = [
            "其实我们还可以对VGroup进行对齐操作",
            "我们先来加入两个组a和b.",
            "一组有5个文本.另一组有3个文本.如下所示",
            "比如让B[0]和A[1]对齐",
            "传入的A[1]是一个VGroup的一项，B和它左对齐",
            "或者让B[0]和A[2]对齐",
            "传入的A[2]也是一个VGroup的一项，B和它左对齐",
            "如果让B[1]和A[2]对齐怎么办？",
            "我们需要用到属性——submobject_to_align和index_of_submobject_to_align",
            "传入的submobject_to_align是自己要对齐的位置。这里就是让B[1]和目标A[2]对齐",
            "或者还有一种等价的写法。像这样：",
            "我们可以看出，我们这里传入了一个VMobject的列表A",
            "这就相当于A的第index_of_submobject_to_align项和submobject_to_align对齐。",

        ]
        commands = [
            """A = VGroup(...)""",
            """B = VGroup(...)""",
            "B.next_to(A[2],DOWN,aligned_edge=LEFT)",
            "B.next_to(A[1],DOWN,aligned_edge=LEFT)",
            """B.next_to(A[2],DOWN,
    submobject_to_align=B[1],
    aligned_edge=LEFT)""",
            """B.next_to(A,DOWN,
    index_of_submobject_to_align=2,
    submobject_to_align=B[1],
    aligned_edge=LEFT)"""

        ]
        caps = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Medium', size=0.5).shift(DOWN * 3.4)
                for cap in captions
            ]
        )
        vg1 = VGroup(
            TextMobject("$A_0$", color=BLACK).shift(LEFT * 2),
            TextMobject("$A_1$", color=BLACK).shift(LEFT),
            TextMobject("$A_2$", color=BLACK),
            TextMobject("$A_3$", color=BLACK).shift(RIGHT),
            TextMobject("$A_4$", color=BLACK).shift(RIGHT * 2),
        ).shift(2 * LEFT).shift(UP)

        vg2 = VGroup(
            TextMobject("$B_0$", color=BLACK).shift(LEFT),
            TextMobject("$B_1$", color=BLACK),
            TextMobject("$B_2$", color=BLACK).shift(RIGHT)
        ).shift(3 * LEFT).shift(UP * 2)

        eg = vg2.copy().next_to(vg1[1], DOWN, aligned_edge=LEFT)
        eg3 = vg2.copy().next_to(vg1[2], DOWN, aligned_edge=LEFT)
        eg2 = vg2.copy().next_to(vg1[2], DOWN, submobject_to_align=vg2[1], aligned_edge=LEFT)

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = UP * 2.9 + RIGHT * 3.6
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)

        coms = VGroup(
            *[
                CodeLine(com, font='Consolas', size=0.33).move_to(loc)
                for com in commands
            ]
        )

        self.add(tex_bg)

        def change(what, where):
            self.play(ReplacementTransform(what[where - 1], what[where]))
            self.wait()

        self.play(Write(caps[0]))
        self.wait()
        change(caps, 1)
        self.wait()
        change(caps, 2)
        self.play(Write(coms[0].shift(-0.2 * UP + 1.2 * LEFT)))
        self.play(Write(vg1))
        self.play(Write(coms[1].next_to(coms[0], DOWN, aligned_edge=LEFT)))
        self.play(Write(vg2))
        change(caps, 3)
        self.wait(1)
        change(caps, 4)
        self.play(Write(coms[3].next_to(coms[1], DOWN, aligned_edge=LEFT)))
        self.play(ReplacementTransform(vg2, eg))
        self.wait()
        change(caps, 5)
        change(caps, 6)
        self.play(FocusOn(coms[3]))
        self.play(ReplacementTransform(coms[3], coms[2].move_to(coms[3].get_center())))

        self.play(ReplacementTransform(eg, eg3))
        self.wait(1)

        change(caps, 7)
        self.wait(2)
        change(caps, 8)
        self.wait(2)
        self.play(FocusOn(coms[2]))
        self.play(FadeOut(coms[2]), FadeIn(coms[4].next_to(coms[1], DOWN, aligned_edge=LEFT)))

        self.play(ReplacementTransform(eg3, eg2))
        change(caps, 9)

        self.wait(3)
        change(caps, 10)
        self.play(FocusOn(coms[4]))
        self.play(FadeOut(coms[4]), FadeIn(coms[5].next_to(coms[1], DOWN, aligned_edge=LEFT)))
        self.wait(3)
        change(caps, 11)
        self.wait(3)
        change(caps, 12)
        self.wait(3)
