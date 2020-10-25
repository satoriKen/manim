from manim_sandbox.utils.imports import *


class CodeLine(Text):
    CONFIG = {
        't2c': {
            'RIGHT': ORANGE,
            'LEFT': ORANGE,
            'DOWN': ORANGE,
            'UP': ORANGE,
            'UR': ORANGE,
            'UL': ORANGE,
            'DR': ORANGE,
            'DL': ORANGE,
            'ORIGIN': ORANGE,
            'DEGREES': ORANGE,
            'BLACK': ORANGE,
            'Arc': ORANGE,
            'Circle': ORANGE,
            'AnnularSector': ORANGE,
            'ArcBetweenPoints': ORANGE,
            'CurvedArrow': ORANGE,
            'CurvedDoubleArrow': ORANGE,
            'FadeIn': average_color(RED, ORANGE),
            'move_to': BLUE_D,
            'shift': BLUE_D,
            'next_to': BLUE_D,
            'to_corner': BLUE_D,
            'to_edge': BLUE_D,
            'align_to': BLUE_D,
            'scale': BLUE_D,
            'rotate': BLUE_D,
            'flip': BLUE_D,
            'add': BLUE_D,
            'play': BLUE_D,
            'set_width': BLUE_D,
            'set_stroke': BLUE_D,
            '0': average_color(BLUE, PINK),
            '1': average_color(BLUE, PINK),
            '2': average_color(BLUE, PINK),
            '3': average_color(BLUE, PINK),
            '4': average_color(BLUE, PINK),
            '5': average_color(BLUE, PINK),
            '6': average_color(BLUE, PINK),
            '7': average_color(BLUE, PINK),
            '8': average_color(BLUE, PINK),
            '9': average_color(BLUE, PINK),
            'p1': average_color(BLUE, PINK),
            'p2': average_color(BLUE, PINK),
            'angle': average_color(BLUE, PINK),
            'self': PINK,
            'mob': RED_D,
            '~': WHITE,  # 随便搞个不常用的字符设成白色，以便在有时不能用空格占位时（比如涉及Transform）当空格用
        },
        'font': 'Consolas',
        'size': 0.3,
        'color': DARK_GRAY,
        'plot_depth': 2,
    }

    def __init__(self, text, **kwargs):
        # digest_config(self, kwargs)
        Text.__init__(self, text, **kwargs)


class CodeLines(VGroup):
    def __init__(self, *text, buff=0.2, **kwargs):
        VGroup.__init__(self)
        for each in text:
            self.add(CodeLine(each, **kwargs))
        self.arrange(DOWN, aligned_edge=LEFT, buff=buff)


class CodeBackground(BackgroundRectangle):
    CONFIG = {
        "fill_color": "#EBEBEB",
        "fill_opacity": 1,
        "stroke_width": 1,
        "stroke_opacity": 1,
        "stroke_color": DARK_GRAY,
        "buff": 0.5
    }


class ColorText(Text):
    CONFIG = {
        "size": 0.4,
        "font": "Consolas",
        "t2c": {
            '"': YELLOW_E,
            'np': BLACK,
            'array': BLUE_D,
            '~': WHITE
        },
        "color": DARK_GRAY,
    }

    def __init__(self, color, name=None, **kwargs):
        if name:
            Text.__init__(self, name, color=color, **kwargs)
        else:
            if isinstance(color, str):
                Text.__init__(self, '"' + color + '"', color=color, **kwargs)
            elif color[0] > 1 or color[1] > 1 or color[2] > 1:
                name = 'np.array([{},~{},~{}])'.format(
                    str(int(color[0])).rjust(3, "~"),
                    str(int(color[1])).rjust(3, "~"),
                    str(int(color[2])).rjust(3, "~")
                )
                Text.__init__(self, name, color=rgb_to_color(color / 255), **kwargs)
                self[10:name.index(",")].set_color(RED)
                self[name.index(",") + 2:name.index(",", name.index(",") + 1)].set_color(GREEN)
                self[name.index(",", name.index(",") + 1) + 2:-2].set_color(BLUE)
                self.set_color_by_t2c({"~": WHITE})
            else:
                name = 'np.array([{:.1f},~{:.1f},~{:.1f}])'.format(color[0], color[1], color[2])
                Text.__init__(self, name, **kwargs)
                self[10:name.index(",")].set_color(RED)
                self[name.index(",") + 2:name.index(",", name.index(",") + 1)].set_color(GREEN)
                self[name.index(",", name.index(",") + 1) + 2:-2].set_color(BLUE)
                self.set_color_by_t2c({"~": WHITE})


class DecimalNumberText(VMobject):
    CONFIG = {
        "num_decimal_places": 2,
        "include_sign": False,
        "group_with_commas": True,
        "digit_to_digit_buff": 0.05,
        "show_ellipsis": False,
        "unit": None,  # Aligned to bottom unless it starts with "^"
        "include_background_rectangle": False,
        "edge_to_fix": LEFT,
        "text_config": {
            "font": "Consolas",
            "size": 0.4,
            "color": GOLD,
        }
    }

    def __init__(self, number=0, **kwargs):
        super().__init__(**kwargs)
        self.number = number
        self.initial_config = kwargs

        if isinstance(number, complex):
            formatter = self.get_complex_formatter()
        else:
            formatter = self.get_formatter()
        num_string = formatter.format(number)

        rounded_num = np.round(number, self.num_decimal_places)
        if num_string.startswith("-") and rounded_num == 0:
            if self.include_sign:
                num_string = "+" + num_string[1:]
            else:
                num_string = num_string[1:]

        self.add(*[
            Text(char, **kwargs, **self.text_config)
            for char in num_string
        ])

        if self.show_ellipsis:
            self.add(Text("...", **self.text_config))

        if num_string.startswith("-"):
            minus = self.submobjects[0]
            minus.next_to(
                self.submobjects[1], LEFT,
                buff=self.digit_to_digit_buff
            )

        if self.unit is not None:
            self.unit_sign = Text(self.unit, color=self.color, **self.text_config)
            self.add(self.unit_sign)

        self.arrange(
            buff=self.digit_to_digit_buff,
            aligned_edge=DOWN
        )

        for i, c in enumerate(num_string):
            if c == "-" and len(num_string) > i + 1:
                self[i].align_to(self[i + 1], UP)
                self[i].shift(self[i + 1].get_height() * DOWN / 2)
            elif c == ",":
                self[i].shift(self[i].get_height() * DOWN / 2)
        if self.unit and self.unit.startswith("^"):
            self.unit_sign.align_to(self, UP)
        #
        if self.include_background_rectangle:
            self.add_background_rectangle()

    def get_formatter(self, **kwargs):
        config = dict([
            (attr, getattr(self, attr))
            for attr in [
                "include_sign",
                "group_with_commas",
                "num_decimal_places",
            ]
        ])
        config.update(kwargs)
        return "".join([
            "{",
            config.get("field_name", ""),
            ":",
            "+" if config["include_sign"] else "",
            "," if config["group_with_commas"] else "",
            ".", str(config["num_decimal_places"]), "f",
            "}",
        ])

    def get_complex_formatter(self, **kwargs):
        return "".join([
            self.get_formatter(field_name="0.real"),
            self.get_formatter(field_name="0.imag", include_sign=True),
            "i"
        ])

    def set_value(self, number, **config):
        full_config = dict(self.CONFIG)
        full_config.update(self.initial_config)
        full_config.update(config)
        new_decimal = DecimalNumberText(number, **full_config)
        new_decimal.scale(
            self[-1].get_height() / new_decimal[-1].get_height()
        )
        new_decimal.move_to(self, self.edge_to_fix)
        new_decimal.match_style(self)

        old_family = self.get_family()
        self.submobjects = new_decimal.submobjects
        for mob in old_family:
            mob.points[:] = 0
        self.number = number
        return self

    def get_value(self):
        return self.number

    def increment_value(self, delta_t=1):
        self.set_value(self.get_value() + delta_t)


class Scene_(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "use_plot_depth": True,
        },
        "fade_all": True,
    }

    def setup(self):
        self.caps_cnt = 1

    def next_caps(self):
        self.play(Transform(self.caps[0], self.caps[self.caps_cnt]))
        self.wait()
        self.caps_cnt += 1

    def tear_down(self):
        if self.fade_all:
            self.play(FadeOut(Group(*self.mobjects)))


class Emote(SVGMobject):
    CONFIG = {
        'file_name': r'mur.svg',
        'shake_color': average_color(YELLOW, ORANGE),
    }

    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        SVGMobject.__init__(self, file_name=self.file_name, **kwargs)
        self.list = [0, 1, 2, 3, 5, 6, 9]
        for i in self.list:
            try:
                self[i].set_fill(self.shake_color, 0)
            except:
                continue

        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]
        # self.add_updater(self.update_emote)

    def update_emote(self, mob):
        h, w, c = self.get_height(), self.get_width(), self.get_center()

        add_shake = not ((h == self.attribute_list[0]) and (w == self.attribute_list[1])
                         and (c[0] == self.attribute_list[2][0]) and (c[1] == self.attribute_list[2][1]))
        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]

        if add_shake:
            for i in self.list:
                self[i].set_opacity(1)
        else:
            for i in self.list:
                self[i].set_opacity(0)

    def shake_on(self):
        self.set_opacity(1)
        return self

    def shake_off(self):
        for i in self.list:
            self[i].set_fill(self.shake_color, 0)
        return self


class Emote_new(VGroup):
    CONFIG = {
        'file_name': r'mur.svg',
        'shake_color': average_color(YELLOW, ORANGE),
        'height': 2.5,
    }

    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.emote = SVGMobject(self.file_name, **kwargs).set_height(self.height)
        self.emote_02 = SVGMobject(self.file_name, **kwargs).set_height(self.height)
        self.center_dot = Dot().move_to(self.emote.get_center()).shift(
            (DOWN + RIGHT * 0.4) * self.height * 0.18).set_opacity(0)
        list = [0, 1, 2, 3, 5, 6, 9]
        for i in list:
            try:
                self.emote[i].set_fill(self.shake_color, 0);
                self.emote_02[i].set_fill(self.shake_color, 0)
            except:
                continue
        self.add(self.emote_02, self.center_dot, self.emote)
        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]
        self.emote_02.add_updater(self.update_emote)

    def update_emote(self, mob):
        h, w, c = self.get_height(), self.get_width(), self.get_center()

        add_shake = not ((h == self.attribute_list[0]) and (w == self.attribute_list[1])
                         and (c[0] == self.attribute_list[2][0]) and (c[1] == self.attribute_list[2][1]))
        self.attribute_list = [self.get_height(), self.get_width(), self.get_center()]

        if add_shake:
            mob.set_opacity(1)
        else:
            mob.set_opacity(0)

    def shake_on(self):
        self.emote_02.set_opacity(1)
        return self

    def shake_off(self):
        self.emote_02.set_opacity(0)
        return self


class Emote_bounce_around(Scene):
    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):

        emote = Emote_new(height=3.2, plot_depth=-1, color=BLACK).shift(UP * 1.234)  # .set_opacity(0.12)
        emote.emote_02.remove_updater(emote.update_emote)
        self.emote_velocity = (RIGHT * 2 + UP * 1.25) * 2.4e-2
        self.rotate_speed = 2.5 * DEGREES

        def update_emote(l, dt):
            l.shift(self.emote_velocity)
            l.rotate(self.rotate_speed, about_point=l.center_dot.get_center())
            self.emote_velocity += (RIGHT * 2 + UP * 1.25) * 2.8e-5 * np.sign(self.emote_velocity)

            if abs(l.get_center()[1]) > (FRAME_HEIGHT - l.get_height()) / 2:
                self.emote_velocity *= DR  # or we can use self.emote_velocity[1] *= -1
                self.rotate_speed *= -1
                l.shake_on()
            if abs(l.get_center()[0]) > (FRAME_WIDTH - l.get_width()) / 2:
                self.emote_velocity *= UL  # or we can use self.emote_velocity[0] *= -1
                self.rotate_speed *= -1
                l.shake_on()
            else:
                l.emote_02.set_opacity(l.emote_02.get_fill_opacity() - 0.02 if l.emote_02.get_fill_opacity() > 0 else 0)

        emote.add_updater(update_emote)
        self.add(emote)

        self.wait(24)


class CodeStyleTest(Scene):
    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }

    def construct(self):
        emote = Emote_new(color=BLACK, plot_depth=1).set_height(2.4).shift(LEFT * 4 + UP)

        tex_bg = Rectangle(stroke_width=1, stroke_color=GRAY, fill_color=LIGHT_GREY, fill_opacity=0.25, plot_depth=-1)
        tex_bg.set_height(6.2, stretch=True).set_width(5.4, stretch=True)
        loc = UP * 2.9 + RIGHT * 2.64
        tex_bg.to_corner(RIGHT * 1.25 + UP * 1.25)
        tex_add = CodeLine('self.add(mob)').move_to(loc)
        tex_shift_l = CodeLine('mob.shift(LEFT)').next_to(tex_add, DOWN).align_to(tex_add, LEFT)
        tex_flip_1 = CodeLine('mob.flip()').next_to(tex_shift_l, DOWN).align_to(tex_shift_l, LEFT)
        tex_flip_2 = CodeLine('mob.flip()').next_to(tex_flip_1, DOWN).align_to(tex_flip_1, LEFT)
        tex_shift_r2 = CodeLine('mob.shift(RIGHT * 2)').next_to(tex_flip_2, DOWN).align_to(tex_flip_2, LEFT)
        tex_scale_2 = CodeLine('mob.scale(2)').next_to(tex_shift_r2, DOWN).align_to(tex_shift_r2, LEFT)
        tex_annotation = CodeLine('# 所有对mob的变换均为瞬间完成的，\n\n'
                                  '# 但为了演示变换过程，\n\n'
                                  '# 实际执行的是将变换放入\n\n'
                                  '# self.play()后的对应动画过程', font='思源黑体 Bold', size=0.29) \
            .next_to(tex_scale_2, DOWN).align_to(tex_scale_2, LEFT).set_color(GREEN)

        loc_02 = DOWN * 1.2
        caption_add = CodeLine('使用self.add(mob)将物体（mob）加入场景', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_shift_1 = CodeLine('使用mob.shift(LEFT)将mob向左移动1个单位', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_flip_1 = CodeLine('使用mob.flip()将mob翻转', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_flip_2 = CodeLine('使用mob.flip()将mob再次翻转', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_shift_r2 = CodeLine('使用mob.shift(RIGHT*2)将mob向右移动2个单位', font='思源黑体 Bold', size=0.32).to_edge(loc_02)
        caption_scale_2 = CodeLine('使用mob.scale(2)将mob沿自身中心放大2倍', font='思源黑体 Bold', size=0.32).to_edge(loc_02)

        self.wait()
        self.play(FadeInFromDown(tex_bg))
        self.play(Write(tex_add), Write(caption_add), run_time=1.5)
        self.add(emote)
        self.wait()

        self.play(Write(tex_shift_l), ReplacementTransform(caption_add, caption_shift_1), run_time=1.5)
        self.play(emote.shift, LEFT, run_time=1.6)
        self.wait()

        self.play(Write(tex_flip_1), ReplacementTransform(caption_shift_1, caption_flip_1), run_time=1.5)
        self.play(emote.flip, run_time=1.25)
        self.wait(0.5)
        self.play(Write(tex_flip_2), ReplacementTransform(caption_flip_1, caption_flip_2), run_time=1.5)
        self.play(emote.flip, run_time=1.25)
        self.wait()

        self.play(Write(tex_shift_r2), ReplacementTransform(caption_flip_2, caption_shift_r2), run_time=1.5)
        self.play(emote.shift, RIGHT * 2, run_time=1.6)
        self.wait()

        self.play(Write(tex_scale_2), ReplacementTransform(caption_shift_r2, caption_scale_2), run_time=1.5)
        self.play(emote.scale, 2, run_time=1.6)

        self.wait(0.4)
        self.play(Write(tex_annotation), FadeOut(caption_scale_2), run_time=4)

        self.wait(5)
