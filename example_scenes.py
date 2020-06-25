#!/usr/bin/env python

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()


class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "This is a some text",
            tex_to_color_map={r"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()


class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()

# See old_projects folder for many, many more


class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10.3,
        "y_min": -1.5,
        "y_max": 1.5,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_labeled_nums": range(-10,12,2),
    }

    def construct(self):

        self.setup_axes(animate=True)

        func_graph = self.get_graph(self.func_to_graph, self.function_color)  # function_color specified in CONFIG
        graph_lab = self.get_graph_label(func_graph, label="\\cos(x)")

        func_graph2 = self.get_graph(self.func_to_graph2)
        graph_lab2 = self.get_graph_label(func_graph2, label="\\sin(x)", x_val=-10, direction=UP/2)

        vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color=YELLOW)

        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU, func_graph)
        two_pi.next_to(label_coord, RIGHT+UP)

        self.play(
            ShowCreation(func_graph),
            ShowCreation(graph_lab))
        self.play(
            ShowCreation(func_graph2),
            ShowCreation(graph_lab2))
        self.play(
            ShowCreation(vert_line),
            ShowCreation(two_pi))

    def func_to_graph(self, x):
        return np.cos(x)

    def func_to_graph2(self, x):
        return np.sin(x)


class ExampleApproximation(GraphScene):
    CONFIG = {
        "function" : lambda x : np.cos(x),
        "function_color" : BLUE,
        "taylor" : [lambda x: 1, lambda x: 1-x**2/2, lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4), lambda x: 1-x**2/2+x**4/math.factorial(4)-x**6/math.factorial(6),
        lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8), lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8) - x**10/math.factorial(10)],
        "center_point" : 0,
        "approximation_color" : GREEN,
        "x_min" : -10,
        "x_max" : 10,
        "y_min" : -1,
        "y_max" : 1,
        "graph_origin" : ORIGIN ,
        "x_labeled_nums" :range(-10,12,2),

    }

    def construct(self):

        self.setup_axes(animate=True)

        func_graph = self.get_graph(
            self.function,
            self.function_color,
        )

        approx_graphs = [
            self.get_graph(
                f,
                self.approximation_color
            )
            for f in self.taylor
        ]

        term_num = [
            TexMobject("n = " + str(n), aligned_edge=TOP)
            for n in range(0, 8)]


        # Since we are going to do successive transformations from a list, it helps to have a blank placeholder on the screen.
        # term and approx_graph are VectorizedPoint instances, which are mobjects that don’t display anything on screen.
        # This way we can put the placeholders on the screen without anything appearing,
        # and then transform those mobjects into either the graph or the TexMobjects.
        approx_graph = VectorizedPoint(
            self.input_to_graph_point(self.center_point, func_graph)
        )

        term = VectorizedPoint(3*DOWN)

        self.play(
            ShowCreation(func_graph),
        )

        for n, graph in enumerate(approx_graphs):
            self.play(
                Transform(approx_graph, graph, run_time=2),
                Transform(term, term_num[n])
            )
            self.wait()


class NumberPlane(VMobject):
    CONFIG = {
        "color": BLUE_D,
        "secondary_color": BLUE_E,
        "axes_color": WHITE,
        "secondary_stroke_width": 1,
        # TODO: Allow coordinate center of NumberPlane to not be at (0, 0)
        "x_radius": None,
        "y_radius": None,
        "x_unit_size": 1,
        "y_unit_size": 1,
        "center_point": ORIGIN,
        "x_line_frequency": 1,
        "y_line_frequency": 1,
        "secondary_line_ratio": 1,
        "written_coordinate_height": 0.2,
        "propagate_style_to_family": False,
        "make_smooth_after_applying_functions": True,
    }


class DrawAnAxis(Scene):
    CONFIG = {"plane_kwargs": {
        "x_line_frequency": 2,
        "y_line_frequency": 2
    }
    }

    def construct(self):
        my_plane = NumberPlane(**self.plane_kwargs)
        # my_plane.add(my_plane.get_axis_labels())
        self.add(my_plane)


class SimpleField(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED
        },
    }

    def construct(self):

        plane = NumberPlane(**self.plane_kwargs)
        # plane.add(plane.get_axis_labels())
        self.add(plane)

        points = [x*RIGHT+y*UP
            for x in np.arange(-5,5,1)
            for y in np.arange(-5,5,1)
            ]

        vec_field = []
        for point in points:
            field = 0.5*RIGHT + 0.5*UP
            result = Vector(field).shift(point)
            vec_field.append(result)

        draw_field = VGroup(*vec_field)

        self.play(ShowCreation(draw_field))


class MoveBraces(Scene):
    def construct(self):
        text=TexMobject(
            "\\frac{d}{dx}f(x)g(x)=",       #0
            "f(x)\\frac{d}{dx}g(x)",        #1
            "+",                            #2
            "g(x)\\frac{d}{dx}f(x)"         #3
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff = SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff = SMALL_BUFF)
        t1 = brace1.get_text("$g'f$")
        t2 = brace2.get_text("$f'g$")
        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
            )
        self.wait()
        self.play(
        	ReplacementTransform(brace1,brace2),
        	ReplacementTransform(t1,t2)
        	)
        self.wait()


class NumberPlane(Axes):
    CONFIG = {
        "axis_config": {
            "stroke_color": WHITE,
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
        },
        "y_axis_config": {
            "label_direction": DR,
        },
        "background_line_style": {
            "stroke_color": BLUE_D,
            "stroke_width": 2,
            "stroke_opacity": 1,
        },
        # Defaults to a faded version of line_config
        "faded_line_style": None,
        "x_line_frequency": 1,
        "y_line_frequency": 1,
        "faded_line_ratio": 1,
        "make_smooth_after_applying_functions": True,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_background_lines()

    def init_background_lines(self):
        if self.faded_line_style is None:
            style = dict(self.background_line_style)
            # For anything numerical, like stroke_width
            # and stroke_opacity, chop it in half
            for key in style:
                if isinstance(style[key], numbers.Number):
                    style[key] *= 0.5
            self.faded_line_style = style

        self.background_lines, self.faded_lines = self.get_lines()
        self.background_lines.set_style(
            **self.background_line_style,
        )
        self.faded_lines.set_style(
            **self.faded_line_style,
        )
        self.add_to_back(
            self.faded_lines,
            self.background_lines,
        )

    def get_lines(self):
        x_axis = self.get_x_axis()
        y_axis = self.get_y_axis()
        x_freq = self.x_line_frequency
        y_freq = self.y_line_frequency

        x_lines1, x_lines2 = self.get_lines_parallel_to_axis(
            x_axis, y_axis, x_freq,
            self.faded_line_ratio,
        )
        y_lines1, y_lines2 = self.get_lines_parallel_to_axis(
            y_axis, x_axis, y_freq,
            self.faded_line_ratio,
        )
        lines1 = VGroup(*x_lines1, *y_lines1)
        lines2 = VGroup(*x_lines2, *y_lines2)
        return lines1, lines2

    def get_lines_parallel_to_axis(self, axis1, axis2, freq, ratio):
        line = Line(axis1.get_start(), axis1.get_end())
        dense_freq = (1 + ratio)
        step = (1 / dense_freq) * freq

        lines1 = VGroup()
        lines2 = VGroup()
        ranges = (
            np.arange(0, axis2.x_max, step),
            np.arange(0, axis2.x_min, -step),
        )
        for inputs in ranges:
            for k, x in enumerate(inputs):
                new_line = line.copy()
                new_line.move_to(axis2.number_to_point(x))
                if k % (1 + ratio) == 0:
                    lines1.add(new_line)
                else:
                    lines2.add(new_line)
        return lines1, lines2

    def get_center_point(self):
        return self.coords_to_point(0, 0)

    def get_x_unit_size(self):
        return self.get_x_axis().get_unit_size()

    def get_y_unit_size(self):
        return self.get_x_axis().get_unit_size()

    def get_axes(self):
        return self.axes

    def get_vector(self, coords, **kwargs):
        kwargs["buff"] = 0
        return Arrow(
            self.coords_to_point(0, 0),
            self.coords_to_point(*coords),
            **kwargs
        )

    def prepare_for_nonlinear_transform(self, num_inserted_curves=50):
        for mob in self.family_members_with_points():
            num_curves = mob.get_num_curves()
            if num_inserted_curves > num_curves:
                mob.insert_n_curves(
                    num_inserted_curves - num_curves
                )
        return self


class RefresherOnPolarCoordinates(MovingCameraScene):
    CONFIG = {
        "x_color": GREEN,
        "y_color": RED,
        "r_color": YELLOW,
        "theta_color": LIGHT_PINK,
    }

    def construct(self):
        self.show_xy_coordinates()

    def show_xy_coordinates(self):
        plane = NumberPlane()
        plane.add_coordinates()

        x = 3 * np.cos(PI / 6)
        y = 3 * np.sin(PI / 6)

        point = plane.c2p(x, y)
        xp = plane.c2p(x, 0)
        origin = plane.c2p(0, 0)

        x_color = self.x_color
        y_color = self.y_color

        x_line = Line(origin, xp, color=x_color)
        y_line = Line(xp, point, color=y_color)
        n_line = ArcBetweenPoints(point, origin, angle=-TAU/4)

        dot = Dot(point)

        coord_label = self.get_coord_label(0, 0, x_color, y_color)
        x_coord = coord_label.x_coord
        y_coord = coord_label.y_coord
        coord_label.next_to(dot, UR, SMALL_BUFF)
        coord_label.add_updater(
            lambda m: m.next_to(dot, UR, SMALL_BUFF)
        )

        x_brace = Brace(x_coord, UP)
        y_brace = Brace(y_coord, UP)
        x_brace.add(x_brace.get_tex("x").set_color(x_color))
        y_brace.add(y_brace.get_tex("y").set_color(y_color))
        x_brace.add_updater(lambda m: m.next_to(x_coord, UP, SMALL_BUFF))
        y_brace.add_updater(lambda m: m.next_to(y_coord, UP, SMALL_BUFF))

        self.add(plane)
        self.add(dot, coord_label)
        self.add(x_brace, y_brace)

        self.play(
            ShowCreation(x_line),
            ChangeDecimalToValue(x_coord, x),
            UpdateFromFunc(
                dot,
                lambda d: d.move_to(x_line.get_end()),
            ),
            run_time=2,
        )
        self.play(
            ShowCreation(y_line),
            ChangeDecimalToValue(y_coord, y),
            UpdateFromFunc(
                dot,
                lambda d: d.move_to(y_line.get_end()),
            ),
            run_time=2,
        )
        self.play(
            ShowCreation(n_line),
            # ChangeDecimalToValue(x_coord, x),
            # ChangeDecimalToValue(y_coord, y),
            UpdateFromFunc(
                dot,
                lambda d: d.move_to(n_line.get_end()),
            ),
            run_time=3,
        )
        self.wait()

    def get_coord_label(self,
                        x=0,
                        y=0,
                        x_color=WHITE,
                        y_color=WHITE,
                        include_background_rectangle=True,
                        **decimal_kwargs):
        coords = VGroup()
        for n in x, y:
            if isinstance(n, numbers.Number):
                coord = DecimalNumber(n, **decimal_kwargs)
            elif isinstance(n, str):
                coord = TexMobject(n)
            else:
                raise Exception("Invalid type")
            coords.add(coord)

        x_coord, y_coord = coords
        x_coord.set_color(x_color)
        y_coord.set_color(y_color)

        coord_label = VGroup(
            TexMobject("("), x_coord,
            TexMobject(","), y_coord,
            TexMobject(")")
        )
        coord_label.arrange(RIGHT, buff=SMALL_BUFF)
        coord_label[2].align_to(coord_label[0], DOWN)

        coord_label.x_coord = x_coord
        coord_label.y_coord = y_coord
        if include_background_rectangle:
            coord_label.add_background_rectangle()
        return coord_label


INTERVAL_RADIUS = 5
NUM_INTERVAL_TICKS = 16
class ZoomInOnInterval(Scene):

    def construct(self):
        number_line = NumberLine(density = 10*DEFAULT_POINT_DENSITY_1D)
        number_line.add_numbers()
        interval = self.zero_to_one_interval().split()

        new_line = deepcopy(number_line)
        # new_line.set_color("black", lambda x_y_z1 : x_y_z1[0] < 0 or x_y_z1[0] > 1 or x_y_z1[1] < -0.2)
        # height = new_line.get_height()
        new_line.scale(2*INTERVAL_RADIUS)
        new_line.shift(INTERVAL_RADIUS*LEFT)
        # new_line.stretch_to_fit_height(height)

        self.add(number_line)
        self.wait()
        self.play(Transform(number_line, new_line))
        self.clear()
        squish = lambda p : (p[0], 0, 0)
        self.play(
            ApplyMethod(new_line.apply_function, squish),
            ApplyMethod(
                interval[0].apply_function, squish,
                rate_func = lambda t : 1-t
            ),
            *[FadeIn(interval[x]) for x in [1, 2]]
        )
        self.clear()
        self.add(*interval)
        self.wait()


    def zero_to_one_interval(self):
        interval = NumberLine(
            radius = INTERVAL_RADIUS,
            interval_size = 2.0*INTERVAL_RADIUS/NUM_INTERVAL_TICKS
        )
        # interval.elongate_tick_at(-INTERVAL_RADIUS, 4)
        # interval.elongate_tick_at(INTERVAL_RADIUS, 4)
        zero = TexMobject("0").shift(INTERVAL_RADIUS*LEFT+DOWN)
        one = TexMobject("1").shift(INTERVAL_RADIUS*RIGHT+DOWN)
        mob = Mobject()
        mob.add(interval)
        mob.add(zero)
        mob.add(one)
        return mob

