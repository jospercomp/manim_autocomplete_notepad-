#Manim Community Examples
from manimlib.imports import *
import numpy as np

class AnimatedBoundaryExample(Scene):
    def construct(self):
        text = Text("So shiny!")
        boundary = AnimatedBoundary(text, colors=[RED, GREEN, BLUE],
                                    cycle_rate=3)
        self.add(text, boundary)
        self.wait(2)
###################################
class UsefulAnnotations(Scene):
    def construct(self):
        m0 = SmallDot()
        #m1 = AnnotationDot()
        #m2 = LabeledDot("ii")
        #m3 = LabeledDot(MathTex(r"\alpha").set_color(ORANGE))
        m4 = CurvedArrow(ORIGIN, 2*LEFT)
        m5 = CurvedDoubleArrow(ORIGIN, 2*RIGHT)

        #self.add(m0, m1, m2, m3, m4, m5)
        self.add(m0, m4, m5)
        for i, mobj in enumerate(self.mobjects):
            mobj.shift(DOWN * (i-3))
        self.wait(3)
#################################         
class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)
################################# 
class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)
#################################         
class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        # place the circle two units left from the origin
        circle.move_to(LEFT * 2)
        # place the square to the left of the circle
        square.next_to(circle, LEFT)
        # align the left border of the triangle to the left border of the circle
        triangle.align_to(circle, LEFT)

        self.add(circle, square, triangle)
        self.wait(1)
################################# 
class MobjectStyling(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.add(circle, square, triangle)
        self.wait(1)
#################################         
class MobjectZOrder(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.add(triangle, square, circle)
        self.wait(1)
################################# 
class SomeAnimations(Scene):
    def construct(self):
        square = Square()
        self.add(square)

        # some animations display mobjects, ...
        self.play(FadeIn(square))

        # ... some move or rotate mobjects around...
        self.play(Rotate(square, PI/4))

        # some animations remove mobjects from the screen
        self.play(FadeOut(square))

        self.wait(1)
#################################         
class ApplyMethodExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        # animate the change of color
        self.play(ApplyMethod(square.set_fill, WHITE))
        self.wait(1)

        # animate the change of position
        self.play(ApplyMethod(square.shift, UP))
        self.wait(1)
################################# 
class RunTime(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.play(ApplyMethod(square.shift, UP), run_time=3)
        self.wait(1)
class MoveAlongPathExample(Scene):
    def construct(self):
        d1 = Dot().set_color(ORANGE)
        l1 = Line(LEFT, RIGHT)
        l2 = VMobject()
        self.add(d1, l1, l2)
        l2.add_updater(lambda x: x.become(Line(LEFT, d1.get_center()).set_color(ORANGE)))
        self.play(MoveAlongPath(d1, l1), rate_func=linear)
#################################
class ImageFromArray(Scene):
    def construct(self):
        image = ImageMobject(np.uint8([[0, 100, 30, 200],
                                       [255, 0, 5, 33]]))
        image.height = 7
        self.add(image)
        self.wait(3)
####################################        
class HelloWorld(Scene):
    def construct(self):
        text = Text('Hello world').scale(3)
        self.add(text)
        self.wait(3)        
####################################
class TextAlignment(Scene):
    def construct(self):
        title = Text("K-means clustering and Logistic Regression", color=WHITE)
        title.scale_in_place(0.75)
        self.add(title.to_edge(UP))

        t1 = Text("1. Measuring").set_color(WHITE)
        t1.next_to(ORIGIN, direction=RIGHT, aligned_edge=UP)

        t2 = Text("2. Clustering").set_color(WHITE)
        t2.next_to(t1, direction=DOWN, aligned_edge=LEFT)

        t3 = Text("3. Regression").set_color(WHITE)
        t3.next_to(t2, direction=DOWN, aligned_edge=LEFT)

        t4 = Text("4. Prediction").set_color(WHITE)
        t4.next_to(t3, direction=DOWN, aligned_edge=LEFT)

        x = VGroup(t1, t2, t3, t4).scale_in_place(0.7)
        x.set_opacity(0.5)
        x.submobjects[1].set_opacity(1)
        self.add(x)
        self.wait(3)
###########################################  
class PlotParametricFunction(Scene):
    def func(self, t):
        return np.array((np.sin(2 * t), np.sin(3 * t), 0))

    def construct(self):
        func = ParametricFunction(self.func, t_max = TAU, fill_opacity=0).set_color(RED)
        self.add(func.scale(3))
        self.wait(3)        
############################################  
class ThreeDParametricSpring(ThreeDScene):
    def construct(self):
        curve1 = ParametricFunction(
            lambda u: np.array([
                1.2 * np.cos(u),
                1.2 * np.sin(u),
                u * 0.05
            ]), color=RED, t_min=-3 * TAU, t_max=5 * TAU,
        ).set_shade_in_3d(True)
        axes = ThreeDAxes()
        self.add(axes, curve1)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.wait()
###################################
class ShowPassingFlashScene(Scene):
    def construct(self):
        p = RegularPolygon(5)
        self.add(p)
        self.play(ShowPassingFlash(p.copy().set_color(YELLOW)))    
###################################################################################
class RotationUpdater(Scene):
    def construct(self):
        def updater_forth(mobj, dt):
            mobj.rotate_about_origin(dt)
        def updater_back(mobj, dt):
            mobj.rotate_about_origin(-dt)
        line_reference = Line(ORIGIN, LEFT).set_color(WHITE)
        line_moving = Line(ORIGIN, LEFT).set_color(YELLOW)
        line_moving.add_updater(updater_forth)
        self.add(line_reference, line_moving)
        self.wait(2)
        line_moving.remove_updater(updater_forth)
        line_moving.add_updater(updater_back)
        self.wait(2)
        line_moving.remove_updater(updater_back)
        self.wait(0.5)
#####################################
class Example(Scene):
    def construct(self):
        s1 = Square()
        s2 = Square()
        s3 = Square()
        s4 = Square()
        x = VGroup(s1, s2, s3, s4).set_x(0).arrange(buff=1.0)
        self.add(x)
        self.wait(3)
#########################
class DotInterpolation(Scene):
    def construct(self):
        dotL = Dot(color=DARK_GREY)
        dotL.shift(2 * RIGHT)
        dotR = Dot(color=WHITE)
        dotR.shift(2 * LEFT)

        dotMiddle = VMobject().interpolate(dotL, dotR, alpha=0.3)

        self.add(dotL, dotR, dotMiddle)
        self.wait(3)
###########################
class GeometricShapes(Scene):
    def construct(self):
        d = Dot()
        c = Circle()
        s = Square()
        t = Triangle()
        d.next_to(c, RIGHT)
        s.next_to(c, LEFT)
        t.next_to(c, DOWN)
        self.add(d, c, s, t)
        self.wait(3)
#####################################
class ShowIncreasingSubsetsScene(Scene):
    def construct(self):
        p = VGroup(Dot(), Square(), Triangle())
        self.add(p)
        self.play(ShowIncreasingSubsets(p))
        self.wait()
#####################################        
class SequencePlot(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            y_axis_label=r"Concentration [\%]",
            x_axis_label="Time [s]",
            **kwargs
        )

    def construct(self):
        data = [1, 2, 2, 4, 4, 1, 3]
        self.setup_axes()
        for time, dat in enumerate(data):
            dot = Dot().move_to(self.coords_to_point(time, dat))
            self.add(dot)
        self.wait()
#################################
class DeterminantOfAMatrix(Scene):
    def construct(self):
        matrix = Matrix([
            [2, 0],
            [-1, 1]
        ])
        # scaling down the `det` string
        det = get_det_text(matrix,
                    determinant=3,
                    initial_scale_factor=1)
        # must add the matrix
        self.add(matrix)
        self.add(det)
        self.wait(3)
###################################        
class BraceExample(Scene):
    def construct(self):
        circle = Circle()
        brace = Brace(circle, direction=RIGHT)
        self.play(ShowCreation(circle))
        self.play(ShowCreation(brace))
        self.wait(2)
###################################
from manim import *
class BraceExample2(Scene):
    def construct(self):
        s = Square()
        self.add(s)
        for i in np.linspace(0.1,1.0,4):
            br = Brace(s, sharpness=i)
            t = Text(f"sharpness= {i}").next_to(br, RIGHT)
            self.add(t)
            self.add(br)
        VGroup(*self.mobjects).arrange(DOWN, buff=0.2)
        self.wait(3)
##################################
class MyScene(Scene):
    def construct(self):
        self.play(Write(Text("Hello World!")))
##################################
class ShowWrite(Scene):
    def construct(self):
        self.play(Write(Text("Hello").scale(3)))
##################################
class CircleExample(Scene):
    def construct(self):
        circle_1 = Circle(radius=1.0)
        circle_2 = Circle(radius=1.5, color=GREEN)
        circle_3 = Circle(radius=1.0, color=BLUE_B, fill_opacity=1)
        circle_group = Group(circle_1, circle_2, circle_3).arrange(buff=1)
        self.add(circle_group)
        self.wait(2)
####################################################
class PointAtAngleExample(Scene):
    def construct(self):
        circle = Circle(radius=2.0)
        p1 = circle.point_at_angle(PI/2)
        p2 = circle.point_at_angle(270*DEGREES)
        s1 = Square(side_length=0.25).move_to(p1)
        s2 = Square(side_length=0.25).move_to(p2)
        self.add(circle, s1, s2)
        self.wait(2)
#####################################################
class DotExample(Scene):
    def construct(self):
        dot1 = Dot(point=LEFT, radius=0.08)
        dot2 = Dot(point=ORIGIN)
        dot3 = Dot(point=RIGHT)
        self.add(dot1,dot2,dot3)
        self.wait(2)
#########################################################        
from manim import *
class PolygonExample(Scene):
    def construct(self):
        isosceles = Polygon([-5, 1.5, 0], [-2, 1.5, 0], [-3.5, -2, 0])
        position_list = [
            [4, 1, 0],  # middle right
            [4, -2.5, 0],  # bottom right
            [0, -2.5, 0],  # bottom left
            [0, 3, 0],  # top left
            [2, 1, 0],  # middle
            [4, 3, 0],  # top right
        ]
        square_and_triangles = Polygon(*position_list, color=PURPLE_B)
        self.add(isosceles, square_and_triangles)
        self.wait(3);
###########################################################
from manim import *
class PolygonRoundCorners(Scene):
    def construct(self):
        points = [[-4, -2, 0], [-2, 2, 0], [4, 2, 0], [2, -2, 0]]
        parallelogram = Polygon(*points, stroke_color=LIGHT_PINK)
        rounded_1 = Polygon(*points, stroke_color=LIGHT_PINK).round_corners(radius=0.5)
        rounded_2 = Polygon(*points, stroke_color=LIGHT_PINK).round_corners(radius=1.5)

        self.play(Transform(parallelogram, rounded_1))
        self.wait(0.5)
        self.play(Transform(parallelogram, rounded_2))
        self.wait(0.5)
###########################################################
from manim import *
class RectangleExample(Scene):
    def construct(self):
        rect1 = Rectangle(width=4.0, height=2.0)
        rect2 = Rectangle(width=1.0, height=4.0)
        rects = Group(rect1,rect2).arrange(buff=1)
        self.add(rects)
        self.wait(3)        
###########################################################
from manim import *
class RegularPolygonExample(Scene):
    def construct(self):
        poly_1 = RegularPolygon(n=6)
        poly_2 = RegularPolygon(n=6, start_angle=30*DEGREES, color=GREEN)
        poly_3 = RegularPolygon(n=10, color=RED)

        poly_group = Group(poly_1, poly_2, poly_3).scale(1.5).arrange(buff=1)
        self.add(poly_group)
        self.wait(3)
###########################################################
from manim import *
class RoundedRectangleExample(Scene):
    def construct(self):
        rect_1 = RoundedRectangle(corner_radius=0.5)
        rect_2 = RoundedRectangle(corner_radius=1.5, height=4.0, width=4.0)

        rect_group = Group(rect_1, rect_2).arrange(buff=1)
        self.add(rect_group)
        self.wait(3)
###########################################################
from manim import *
class SquareExample(Scene):
    def construct(self):
        square_1 = Square(side_length=2.0).shift(DOWN)
        square_2 = Square(side_length=1.0).next_to(square_1, direction=UP)
        square_3 = Square(side_length=0.5).next_to(square_2, direction=UP)
        self.add(square_1, square_2, square_3)
        self.wait(3)
###########################################################
from manim import *
class TangentLineExample(Scene):
    def construct(self):
        circle = Circle(radius=2)
        line_1 = TangentLine(circle, alpha=0.0, length=4, color=BLUE_D) # right
        line_2 = TangentLine(circle, alpha=0.4, length=4, color=GREEN) # top left
        self.add(circle, line_1, line_2)
        self.wait(3)
###########################################################        
from manim import *
class TriangleExample(Scene):
    def construct(self):
        triangle_1 = Triangle()
        triangle_2 = Triangle().scale(2).rotate(60*DEGREES)
        tri_group = Group(triangle_1, triangle_2).arrange(buff=1)
        self.add(tri_group)
        self.wait(3)
###########################################################        
from manim import *
class VectorExample(Scene):
    def construct(self):
        plane = NumberPlane()
        vector_1 = Vector([1,2])
        vector_2 = Vector([-5,-2])
        self.add(plane, vector_1, vector_2)
        self.wait(3)
###########################################################        
from manim import *
class NextToUpdater(Scene):
    def construct(self):
        def dot_position(mobject):
            mobject.set_value(dot.get_center()[0])
            mobject.next_to(dot)

        dot = Dot(RIGHT*3)
        label = DecimalNumber()
        label.add_updater(dot_position)
        self.add(dot, label)

        self.play(Rotating(dot, about_point=ORIGIN, angle=TAU, run_time=TAU, rate_func=linear))
############################################################
from manim import *
class DtUpdater(Scene):
    def construct(self):
        line = Square()
        #Let the line rotate 90° per second
        line.add_updater(lambda mobject, dt: mobject.rotate(dt*90*DEGREES))
        self.add(line)
        self.wait(2)
#############################################################
from manim import *
class ArrangeSumobjectsExample(Scene):
    def construct(self):
        s= VGroup(*[Dot().shift(i*0.1*RIGHT*np.random.uniform(-1,1)+UP*np.random.uniform(-1,1)) for i in range(0,15)])
        s.shift(UP).set_color(BLUE)
        s2= s.copy().set_color(RED)
        s2.arrange_submobjects()
        s2.shift(DOWN)
        self.add(s,s2)
        self.wait(3)
##############################################################        
from manim import *
class BecomeScene(Scene):
    def construct(self):
        circ = Circle(fill_color=RED, fill_opacity=0.8)
        square = Square(fill_color=BLUE, fill_opacity=0.2)
        self.add(circ)
        self.wait(0.5)
        circ.become(square)
        self.wait(0.5)
##############################################################      
from manim import *
class FlipExample(Scene):
    def construct(self):
        s= Line(LEFT, RIGHT+UP).shift(4*LEFT)
        self.add(s)
        s2= s.copy().flip()
        self.add(s2)
        self.wait(3)
##############################################################      
from manim import *
class SuffleSumobjectsExample(Scene):
    def construct(self):
        s= VGroup(*[Dot().shift(i*0.1*RIGHT) for i in range(-20,20)])
        s2= s.copy()
        s2.shuffle_submobjects()
        s2.shift(DOWN)
        self.play(Write(s), Write(s2))
##############################################################       
from manim import *
class ValueTrackerExample2(Scene):
    def construct(self):
        pointer_tracker = ValueTracker(0)
        label = Dot(radius=3).add_updater(lambda x : x.set_x(pointer_tracker.get_value()))
        self.add(label)
        self.add(pointer_tracker)
        pointer_tracker.add_updater(lambda mobject, dt: mobject.increment_value(dt))
        self.wait(2)      
##############################################################                        
from manim import *
class ArcShapeIris(Scene):
    def construct(self):
        colors = [DARK_BLUE, DARK_BROWN, BLUE_E, BLUE_D, BLUE_A, TEAL_B, GREEN_B, YELLOW_E]
        radius = [1 + rad * 0.1 for rad in range(len(colors))]

        circles_group = VGroup()

        # zip(radius, color) makes the iterator [(radius[i], color[i]) for i in range(radius)]
        circles_group.add(*[Circle(radius=rad, stroke_width=10, color=col)
                            for rad, col in zip(radius, colors)])
        self.add(circles_group)
        self.wait(3)
##################################################################
from manim import *
class FunctionPlotWithLabelledYAxis(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            y_min=0,
            y_max=100,
            y_axis_config={"tick_frequency": 10},
            y_labeled_nums=np.arange(0, 100, 10),
            **kwargs
        )
    def construct(self):
        self.setup_axes()
        dot = Dot().move_to(self.coords_to_point(PI / 2, 20))
        func_graph = self.get_graph(lambda x: 20 * np.sin(x))
        self.add(dot,func_graph)
        self.wait(3)
#################################################################
from manim import *
amp = 5
mu = 3
sig = 1
def gaussian(x):
    return amp * np.exp((-1 / 2 * ((x - mu) / sig) ** 2))
class GaussianFunctionPlot(GraphScene):
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(gaussian, x_min=-1, x_max=10)
        graph.set_stroke(width=5)
        self.add(graph)
        self.wait(3)
#################################################################
from manim import *
class ShowDrawBorderThenFill(Scene):
    def construct(self):
        self.play(DrawBorderThenFill(Square(fill_opacity=1, fill_color=ORANGE)))
######################################################################
from manim import *
class ShowUncreate(Scene):
    def construct(self):
        self.play(Uncreate(Square()))
######################################################################
from manim import *
class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(
            ApplyPointwiseFunction(
                lambda point: complex_to_R3(np.exp(R3_to_complex(point))), square
            )
        )
        self.wait()
######################################################################
from manim import *
class BasicUsage(Scene):
    def construct(self):
        func = lambda pos: ((pos[0]*UR+pos[1]*LEFT) - pos)/3
        self.add(StreamLines(func))
        self.wait(3)
##########################################################################