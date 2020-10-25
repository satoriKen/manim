from manim_sandbox.utils.imports import *
from .test_present_style import *


class Scene_1(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "use_plot_depth": True,
        }
    }

    def construct(self):
        # 坐标系
        plane = NumberPlane(axis_config={"stroke_color": BLACK}, plot_depth=-5) \
            .add_coordinates(y_vals=[1, 2, 3, -1, -2], number_config={"color": BLACK})
        # .add_coordinates(y_vals=[1, 2, 3, -1, -2])

        # 字幕
        captions = [
            "使用shift方法可以根据传入的vector移动物体",
            "先将图片添加到画面中",
            "调用shift(LEFT*5)向左移动五个单位",
            "同理可以沿任意方向移动任意单位",
            "shift中可以传入多个vector参数，会先将其全部相加，再进行移动",
        ]
        captions_mob = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.32).to_edge(DOWN * 1.2) \
                    .add_background_rectangle(color=WHITE, buff=0.1, opacity=0.85)
                for cap in captions
            ]
        )

        # 代码块及代码
        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        loc = UP * 2.9 + RIGHT * 2.64
        method = CodeLine("shift(*vector)", size=0.5).next_to(tex_bg.get_top(), DOWN)
        line = Line(LEFT, RIGHT, stroke_width=1, stroke_color=GRAY).set_width(5.4).next_to(method, DOWN)
        codes = [
            "self.add(mob)",
            "mob.shift(LEFT*5)",
            "mob.shift(UP*2+RIGHT*3)",
            "mob.shift(DOWN*2, RIGHT*2)"
        ]
        codes_mob = VGroup(
            *[
                CodeLine(code) for code in codes
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob.next_to(line, DOWN, buff=0.5)

        # 移动向量箭头
        arrow1 = Arrow(ORIGIN, LEFT * 5, color=ORANGE, buff=0, plot_depth=-1)
        arrow2 = Arrow(LEFT * 5, LEFT * 2 + UP * 2, color=ORANGE, buff=0, plot_depth=-1)
        arrow3_0 = Arrow(LEFT * 2 + UP * 2, LEFT * 2, color=GREEN, buff=0, plot_depth=-1)
        arrow3_1 = Arrow(LEFT * 2, ORIGIN, color=GREEN, buff=0, plot_depth=-1)
        arrow3 = Arrow(LEFT * 2 + UP * 2, ORIGIN, color=ORANGE, buff=0, plot_depth=-1)

        # 物体
        mob1 = ImageMobject("logo.png").set_width(1).shift(UP * 0.2)
        mob2 = ImageMobject("head.png").set_width(1).shift(UP * 0.2)

        # self.add(plane, tex_bg, method, line, codes_mob, arrow1, arrow2, arrow3_0, arrow3_1, arrow3, mob1, mob2)

        self.add(plane)
        self.play(FadeInFromDown(tex_bg))
        self.play(
            Write(captions_mob[0]),
            Write(method)
        )
        self.play(Write(line))
        self.wait(4)
        self.play(
            Transform(captions_mob[0], captions_mob[1])
        )
        self.play(Write(codes_mob[0]), FadeIn(mob1))
        self.wait(4)

        self.play(Transform(captions_mob[0], captions_mob[2]))
        self.play(Write(codes_mob[1]))

        self.play(Write(arrow1))
        self.remove(mob1)
        self.add(mob2)
        self.play(mob2.shift, LEFT * 5)
        self.remove(mob2)
        mob1.shift(LEFT * 5)
        self.add(mob1)
        self.wait(2)
        self.play(FadeOut(arrow1))
        self.wait(2)

        self.play(Transform(captions_mob[0], captions_mob[3]))
        self.play(Write(codes_mob[2]))

        self.play(Write(arrow2))
        self.remove(mob1)
        self.add(mob2)
        self.play(mob2.shift, UP * 2 + RIGHT * 3)
        self.remove(mob2)
        mob1.shift(UP * 2 + RIGHT * 3)
        self.add(mob1)
        self.wait(2)
        self.play(FadeOut(arrow2))
        self.wait(2)

        self.play(Transform(captions_mob[0], captions_mob[4]))
        self.play(Write(codes_mob[3]))

        self.play(Write(arrow3_0))
        self.play(Write(arrow3_1))
        self.wait()
        self.play(Write(arrow3), FadeOut(arrow3_0), FadeOut(arrow3_1))
        self.remove(mob1)
        self.add(mob2)
        self.play(mob2.shift, DOWN * 2 + RIGHT * 2)
        self.remove(mob2)
        mob1.shift(DOWN * 2, RIGHT * 2)
        self.add(mob1)
        self.wait(2)
        self.play(FadeOut(arrow3))
        self.wait(2)
        self.play(FadeOut(Group(captions_mob[0], tex_bg, line, method, codes_mob, mob1)))
        self.wait(2)


class Scene_2(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "use_plot_depth": True,
        }
    }

    def construct(self):
        # 坐标系
        plane = NumberPlane(axis_config={"stroke_color": BLACK}, plot_depth=-5) \
            .add_coordinates(y_vals=[1, 2, 3, -1, -2], number_config={"color": BLACK})

        # 字幕
        captions = [
            "还可以使用move_to方法来使物体移动到目标位置",
            "先将logo添加进画面",
            "传入一个参数，表示移动的目标位置（可以是坐标或者物品）",
            "可选参数aligned_edge，表示与目标位置对齐的方式，默认中对齐",
            "这里将logo与np.array(LEFT*3)左对齐、右对齐",
            "还可以传入coor_mask参数(三维ndarray)，来决定在哪个维度上进行移动",
            "比如，move_to(UP*2)，但是将y轴的移动屏蔽掉，就是这样的效果"
        ]
        captions_mob = VGroup(
            *[
                CodeLine(cap, font='Source Han Sans CN Bold', size=0.32).to_edge(DOWN * 1.2) \
                    .add_background_rectangle(color=WHITE, buff=0.1, opacity=0.85)
                for cap in captions
            ]
        )

        # 代码块及代码
        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        loc = UP * 2.9 + RIGHT * 2.64
        method = CodeLine("""move_to(point_or_mobject, 
aligned_edge=ORIGIN,
coor_mask=np.array([1, 1, 1]))""", size=0.3).next_to(tex_bg.get_top(), DOWN)
        line = Line(LEFT, RIGHT, stroke_width=1, stroke_color=GRAY).set_width(5.4).next_to(method, DOWN)
        codes = [
            "self.add(logo)",
            "logo.move_to(LEFT*5+UP*2)",
            """logo.move_to(LEFT*3,
    aligned_edge=LEFT)""",
            """logo.move_to(LEFT*3,
    aligned_edge=RIGHT)""",
            """logo.move_to(UP*2,
    coor_mask=np.array([1, 0, 1]))"""
        ]
        codes_mob = VGroup(
            *[
                CodeLine(code, size=0.28) for code in codes
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob.next_to(line, DOWN, buff=0.5)

        # 移动向量箭头
        dot1 = Dot(LEFT * 5 + UP * 2, radius=0.12, color=ORANGE, plot_depth=-1)
        dot2 = Dot(LEFT * 3, radius=0.12, color=ORANGE, plot_depth=-1)
        dot3 = Dot(UP * 2, radius=0.12, color=ORANGE, plot_depth=-1)
        arrow1 = Arrow(LEFT * 3.75, UP * 2, color=GREEN, plot_depth=-1, buff=0)
        arrow2 = Arrow(LEFT * 3.75, ORIGIN, color=GOLD, plot_depth=-1, buff=0)

        # 物体
        logo = Logo(size=1.5, black_bg=False)

        # self.add(plane, tex_bg, method, line, codes_mob, arrow1, arrow2, dot1, dot2, dot3, logo)

        self.add(plane)
        self.play(FadeInFromDown(tex_bg))
        self.play(
            Write(captions_mob[0]),
            Write(method)
        )
        self.play(Write(line))
        self.wait(4)
        self.play(
            Transform(captions_mob[0], captions_mob[1])
        )
        self.play(Write(codes_mob[0]), FadeIn(logo))
        self.wait(4)

        self.play(Transform(captions_mob[0], captions_mob[2]))
        self.play(Write(codes_mob[1]))

        self.play(Write(dot1))
        self.play(logo.move_to, LEFT * 5 + UP * 2)
        self.wait(2)
        self.play(FadeOut(dot1))
        self.wait(2)

        self.play(Transform(captions_mob[0], captions_mob[3]))
        self.wait(3)
        self.play(Transform(captions_mob[0], captions_mob[4]))
        self.play(Write(codes_mob[2]))

        self.play(Write(dot2))
        self.play(logo.move_to, LEFT * 3, LEFT)
        self.wait(2)
        self.play(Write(codes_mob[3]))
        self.play(logo.move_to, LEFT * 3, RIGHT)
        self.wait(2)
        self.play(FadeOut(dot2))
        self.wait(2)

        self.play(Transform(captions_mob[0], captions_mob[5]))
        self.wait(3)
        self.play(Transform(captions_mob[0], captions_mob[6]))
        self.play(Write(codes_mob[4]))

        self.play(Write(dot3))
        self.play(Write(arrow1))
        self.wait()
        self.play(TransformFromCopy(arrow1, arrow2))
        self.play(logo.move_to, ORIGIN)
        self.wait(2)
        self.play(FadeOut(dot3), FadeOut(arrow1), FadeOut(arrow2))
        self.wait(2)
        self.play(FadeOut(Group(captions_mob[0], tex_bg, line, method, codes_mob, logo)))
        self.wait(2)
