#Manim Community Examples
from manimlib.imports import *
import numpy as np
###################################
#VGroup No		
# class TracedPathExample(Scene):
    # def construct(self):
        # circ = Circle(color=RED).shift(4*LEFT)
        # dot = Dot(color=RED).move_to(circ.get_start())
        # rolling_circle = VGroup(circ, dot)
        # trace = TracedPath(circ.get_start)
        # rolling_circle.add_updater(lambda m: m.rotate(-0.3))
        # self.add(trace, rolling_circle)
        # self.play(rolling_circle.animate.shift(8*RIGHT), run_time=4, rate_func=linear)
#################################        
# class HelloLaTeX(Scene):
    # def construct(self):
        # tex = Tex(r'\LaTeX').scale(3)
        # self.add(tex)
#################################        
# class HelloTex(Scene):
    # def construct(self):
        # tex = Tex(r'$\xrightarrow{x^2y^3}$ \LaTeX').scale(3)
        # self.add(tex)
#################################         
# class MovingBraces(Scene):
    # def construct(self):
        # text=MathTex(
            # "\\frac{d}{dx}f(x)g(x)=",       #0
            # "f(x)\\frac{d}{dx}g(x)",        #1
            # "+",                            #2
            # "g(x)\\frac{d}{dx}f(x)"         #3
        # )
        # self.play(Write(text))
        # brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
        # brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
        # t1 = brace1.get_text("$g'f$")
        # t2 = brace2.get_text("$f'g$")
        # self.play(
            # GrowFromCenter(brace1),
            # FadeIn(t1),
            # )
        # self.wait()
        # self.play(
            # ReplacementTransform(brace1,brace2),
            # ReplacementTransform(t1,t2)
            # )
        # self.wait()        
#################################
# class AMSLaTeX(Scene):
    # def construct(self):
        # tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX').scale(3)
        # self.add(tex)
#################################        
# class LaTeXAttributes(Scene):
    # def construct(self):
        # tex = Tex(r'Hello \LaTeX', color=BLUE).scale(3)
        # self.add(tex)
################################# 
# class AddPackageLatex(Scene):
    # def construct(self):
        # myTemplate = TexTemplate()
        # myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        # tex = Tex(r'$\mathscr{H} \rightarrow \mathbb{H}$}', tex_template=myTemplate).scale(3)
        # self.add(tex)
#################################        
# class LaTeXSubstrings(Scene):
    # def construct(self):
        # tex = Tex('Hello', r'$\bigstar$', r'\LaTeX').scale(3)
        # tex.set_color_by_tex('igsta', RED)
        # self.add(tex)
#################################                
# class LaTeXMathFonts(Scene):
    # def construct(self):
        # tex = Tex(r'$x^2 + y^2 = z^2$', tex_template=TexFontTemplates.french_cursive).scale(3)
        # self.add(tex) 
################################# 
# class LaTeXTemplateLibrary(Scene):
    # def construct(self):
        # tex = Tex('Hello ?? \\LaTeX', tex_template=TexTemplateLibrary.ctex).scale(3)
        # self.add(tex)
###################################
# class LaTeXAlignEnvironment(Scene):
    # def construct(self):
        # tex = MathTex(r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6').scale(2)
        # self.add(tex)  
###################################
# class BasicMarkupExample(Scene):
    # def construct(self):
        # text1 = MarkupText("<b>foo</b> <i>bar</i> <b><i>foobar</i></b>")
        # text2 = MarkupText("<s>foo</s> <u>bar</u> <big>big</big> <small>small</small>")
        # text3 = MarkupText("H<sub>2</sub>O and H<sub>3</sub>O<sup>+</sup>")
        # text4 = MarkupText("type <tt>help</tt> for help")
        # text5 = MarkupText(
            # '<span underline="double">foo</span> <span underline="error">bar</span>'
        # )
        # group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
        # self.add(group)
###################################
  # class ColorExample(Scene):
    # def construct(self):
        # text1 = MarkupText(
            # f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED
        # )
        # text2 = MarkupText("nice gradient", gradient=(BLUE, GREEN))
        # text3 = MarkupText(
            # 'nice <gradient from="RED" to="YELLOW">intermediate</gradient> gradient',
            # gradient=(BLUE, GREEN),
        # )
        # text4 = MarkupText(
            # 'fl ligature <gradient from="RED" to="YELLOW">causing trouble</gradient> here'
        # )
        # text5 = MarkupText(
            # 'fl ligature <gradient from="RED" to="YELLOW" offset="1">defeated</gradient> with offset'
        # )
        # text6 = MarkupText(
            # 'fl ligature <gradient from="RED" to="YELLOW" offset="1">floating</gradient> inside'
        # )
        # text7 = MarkupText(
            # 'fl ligature <gradient from="RED" to="YELLOW" offset="1,1">floating</gradient> inside'
        # )
        # group = VGroup(text1, text2, text3, text4, text5, text6, text7).arrange(DOWN)
        # self.add(group) 
############################################################
# from manim import *
# #from manim.utils.color import Colors
# class ColorExample2(Scene):
    # def construct(self):
        # cols = Colors._member_names_
        # s = VGroup(*[Line(DOWN, UP, stroke_width=15).set_color(Colors[cols[i]].value) for i in range(0, len(cols))])
        # s.arrange_submobjects(buff=0.2)
        # self.add(s)
# ###################################
# class UnderlineExample(Scene):
    # def construct(self):
        # text1 = MarkupText(
            # '<span underline="double" underline_color="green">bla</span>'
        # )
        # text2 = MarkupText(
            # '<span underline="single" underline_color="green">xxx</span><gradient from="#ffff00" to="RED">aabb</gradient>y'
        # )
        # text3 = MarkupText(
            # '<span underline="single" underline_color="green">xxx</span><gradient from="#ffff00" to="RED" offset="-1">aabb</gradient>y'
        # )
        # text4 = MarkupText(
            # '<span underline="double" underline_color="green">xxx</span><gradient from="#ffff00" to="RED">aabb</gradient>y'
        # )
        # text5 = MarkupText(
            # '<span underline="double" underline_color="green">xxx</span><gradient from="#ffff00" to="RED" offset="-2">aabb</gradient>y'
        # )
        # group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
        # self.add(group) 
###################################
# class FontExample(Scene):
    # def construct(self):
        # text1 = MarkupText(
            # 'all in sans <span font_family="serif">except this</span>', font="sans"
        # )
        # text2 = MarkupText(
            # '<span font_family="serif">mixing</span> <span font_family="sans">fonts</span> <span font_family="monospace">is ugly</span>'
        # )
        # text3 = MarkupText("special char > or &gt;")
        # text4 = MarkupText("special char &lt; and &amp;")
        # group = VGroup(text1, text2, text3, text4).arrange(DOWN)
        # self.add(group)
###################################
# class NewlineExample(Scene):
    # def construct(self):
        # text = MarkupText('foooo<span foreground="red">oo\nbaa</span>aar')
        # self.add(text)
###################################        
# class NoLigaturesExample(Scene):
    # def construct(self):
        # text1 = MarkupText('fl<gradient from="RED" to="GREEN">oat</gradient>ing')
        # text2 = MarkupText('fl<gradient from="RED" to="GREEN">oat</gradient>ing', disable_ligatures=True)
        # group = VGroup(text1, text2).arrange(DOWN)
        # self.add(group)
###################################         
# class MultiLanguage(Scene):
    # def construct(self):
        # morning = MarkupText("???????", font="sans-serif")
        # chin = MarkupText(
            # '? ? ? ?  ? <span fgcolor="blue">? ? ?</span> ? ? ?!'
        # )  # works as in ``Text``.
        # mess = MarkupText("Multi-Language", style=BOLD)
        # russ = MarkupText("???????????? ?? ?? ? ", font="sans-serif")
        # hin = MarkupText("??????", font="sans-serif")
        # japanese = MarkupText("??????????", font="sans-serif")
        # group = VGroup(morning, chin, mess, russ, hin, japanese).arrange(DOWN)
        # self.add(group)
######################################        
# class ArcPolygonExample(Scene):
    # def construct(self):
        # arc_conf = {"stroke_width": 0}
        # poly_conf = {"stroke_width": 10, "stroke_color": BLUE,
              # "fill_opacity": 1, "color": PURPLE}
        # a = [-1, 0, 0]
        # b = [1, 0, 0]
        # c = [0, np.sqrt(3), 0]
        # arc0 = ArcBetweenPoints(a, b, radius=2, **arc_conf)
        # arc1 = ArcBetweenPoints(b, c, radius=2, **arc_conf)
        # arc2 = ArcBetweenPoints(c, a, radius=2, **arc_conf)
        # reuleaux_tri = ArcPolygonFromArcs(arc0, arc1, arc2, **poly_conf)
        # self.play(FadeIn(reuleaux_tri))
        # self.wait(2)
##################################
# class ArcPolygonExample2(Scene):
    # def construct(self):
        # arc_conf = {"stroke_width": 3, "stroke_color": BLUE,
            # "fill_opacity": 0.5, "color": GREEN}
        # poly_conf = {"color": None}
        # a = [-1, 0, 0]
        # b = [1, 0, 0]
        # c = [0, np.sqrt(3), 0]
        # arc0 = ArcBetweenPoints(a, b, radius=2, **arc_conf)
        # arc1 = ArcBetweenPoints(b, c, radius=2, **arc_conf)
        # arc2 = ArcBetweenPoints(c, a, radius=2, stroke_color=RED)
        # reuleaux_tri = ArcPolygonFromArcs(arc0, arc1, arc2, **poly_conf)
        # self.play(FadeIn(reuleaux_tri))
        # self.wait(2)
#################################
# class BezierSplineExample(Scene):
    # def construct(self):
        # p1 = np.array([-3, 1, 0])
        # p1b = p1 + [1, 0, 0]
        # d1 = Dot(point=p1).set_color(BLUE)
        # l1 = Line(p1, p1b)
        # p2 = np.array([3, -1, 0])
        # p2b = p2 - [1, 0, 0]
        # d2 = Dot(point=p2).set_color(RED)
        # l2 = Line(p2, p2b)
        # bezier = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)
        # self.add(l1, d1, l2, d2, bezier)    
####################################
# class HeightExample(Scene):
    # def construct(self):
        # decimal = DecimalNumber().to_edge(UP)
        # rect = Rectangle(color=BLUE)
        # rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        # decimal.add_updater(lambda d: d.set_value(rect.height))

        # self.add(rect_copy, rect, decimal)
        # self.play(rect.animate.set(height=5))
        # self.wait() 
####################################
# class WidthExample(Scene):
    # def construct(self):
        # decimal = DecimalNumber().to_edge(UP)
        # rect = Rectangle(color=BLUE)
        # rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        # decimal.add_updater(lambda d: d.set_value(rect.width))

        # self.add(rect_copy, rect, decimal)
        # self.play(rect.animate.set(width=7))
        # self.wait()
####################################
# class SeveralArcPolygons(Scene):
    # def construct(self):
        # a = [0, 0, 0]
        # b = [2, 0, 0]
        # c = [0, 2, 0]
        # ap1 = ArcPolygon(a, b, c, radius=2)
        # ap2 = ArcPolygon(a, b, c, angle=45*DEGREES)
        # ap3 = ArcPolygon(a, b, c, arc_config={'radius': 1.7, 'color': RED})
        # ap4 = ArcPolygon(a, b, c, color=RED, fill_opacity=1,
                                    # arc_config=[{'radius': 1.7, 'color': RED},
                                    # {'angle': 20*DEGREES, 'color': BLUE},
                                    # {'radius': 1}])
        # ap_group = VGroup(ap1, ap2, ap3, ap4).arrange()
        # self.play(*[ShowCreation(ap) for ap in [ap1, ap2, ap3, ap4]])
        # self.wait()        
###############################
# class AnimateExample(Scene):
    # def construct(self):
        # s = Square()
        # self.play(ShowCreation(s))
        # self.play(s.animate.shift(RIGHT))
        # self.play(s.animate.scale(2))
        # self.play(s.animate.rotate(PI / 2))
        # self.play(Uncreate(s)) 
##############################
# class BraceBPExample(Scene):
    # def construct(self):
        # p1 = [0,0,0]
        # p2 = [1,2,0]
        # brace = BraceBetweenPoints(p1,p2)
        # self.play(ShowCreation(NumberPlane()))
        # self.play(ShowCreation(brace))
        # self.wait(2)
################################        
# class CodeFromString(Scene):
    # def construct(self):
        # code = '''from manim import Scene, Square

# class FadeInSquare(Scene):
    # def construct(self):
        # s = Square()
        # self.play(FadeIn(s))
        # self.play(s.animate.scale(2))
        # self.wait()
# '''
        # rendered_code = Code(code=code, tab_width=4, background="window",
                            # language="Python", font="Monospace")
        # self.add(rendered_code)
#############################################        
# class ChangeOfDirection(Scene):
    # def construct(self):
        # ccw = RegularPolygon(5)
        # ccw.shift(LEFT).rotate
        # cw = RegularPolygon(5)
        # cw.shift(RIGHT).reverse_direction()

        # self.play(ShowCreation(ccw), ShowCreation(cw),
        # run_time=4) 
######################################
# class CutoutExample(Scene):
    # def construct(self):
        # s1 = Square().scale(2.5)
        # s2 = Triangle().shift(DOWN + RIGHT).scale(0.5)
        # s3 = Square().shift(UP + RIGHT).scale(0.5)
        # s4 = RegularPolygon(5).shift(DOWN + LEFT).scale(0.5)
        # s5 = RegularPolygon(6).shift(UP + LEFT).scale(0.5)
        # c = Cutout(s1, s2, s3, s4, s5, fill_opacity=1, color=BLUE, stroke_color=RED)
        # self.play(Write(c), run_time=4)
        # self.wait()
######################################
# class ChangingCameraWidthAndRestore(MovingCameraScene):
    # def construct(self):
        # text = Text("Hello World").set_color(BLUE)
        # self.add(text)
        # self.camera.frame.save_state()
        # self.play(self.camera.frame.animate.set(width=text.width * 1.2))
        # self.wait(0.3)
        # self.play(Restore(self.camera.frame))
######################################
# class MovingCameraCenter(MovingCameraScene):
    # def construct(self):
        # s = Square(color=RED, fill_opacity=0.5).move_to(2 * LEFT)
        # t = Triangle(color=GREEN, fill_opacity=0.5).move_to(2 * RIGHT)
        # self.wait(0.3)
        # self.add(s, t)
        # self.play(self.camera.frame.animate.move_to(s))
        # self.wait(0.3)
        # self.play(self.camera.frame.animate.move_to(t)) 
####################################        
# class MovingAndZoomingCamera(MovingCameraScene):
    # def construct(self):
        # s = Square(color=BLUE, fill_opacity=0.5).move_to(2 * LEFT)
        # t = Triangle(color=YELLOW, fill_opacity=0.5).move_to(2 * RIGHT)
        # self.add(s, t)
        # self.play(self.camera.frame.animate.move_to(s).set(width=s.width*2))
        # self.wait(0.3)
        # self.play(self.camera.frame.animate.move_to(t).set(width=t.width*2))
        # self.play(self.camera.frame.animate.move_to(ORIGIN).set(width=14))
#############################################        
# class MovingCameraOnGraph(GraphScene, MovingCameraScene):
    # def setup(self):
        # GraphScene.setup(self)

    # def construct(self):
        # self.camera.frame.save_state()
        # self.setup_axes(animate=False)
        # graph = self.get_graph(lambda x: np.sin(x),
                               # color=WHITE,
                               # x_min=0,
                               # x_max=3 * PI
                               # )
        # dot_at_start_graph = Dot().move_to(graph.points[0])
        # dot_at_end_graph = Dot().move_to(graph.points[-1])
        # self.add(graph, dot_at_end_graph, dot_at_start_graph)
        # self.play(self.camera.frame.animate.scale(0.5).move_to(dot_at_start_graph))
        # self.play(self.camera.frame.animate.move_to(dot_at_end_graph))
        # self.play(Restore(self.camera.frame))
        # self.wait()
#################################        
# class RateFunctions1Example(Scene):
    # def construct(self):
        # line1 = Line(3*LEFT, 3*RIGHT).shift(UP).set_color(RED)
        # line2 = Line(3*LEFT, 3*RIGHT).set_color(GREEN)
        # line3 = Line(3*LEFT, 3*RIGHT).shift(DOWN).set_color(BLUE)

        # dot1 = Dot().move_to(line1.get_left())
        # dot2 = Dot().move_to(line2.get_left())
        # dot3 = Dot().move_to(line3.get_left())

        # label1 = Tex("Ease In").next_to(line1, RIGHT)
        # label2 = Tex("Ease out").next_to(line2, RIGHT)
        # label3 = Tex("Ease In Out").next_to(line3, RIGHT)

        # self.play(
            # FadeIn(VGroup(line1, line2, line3)),
            # FadeIn(VGroup(dot1, dot2, dot3)),
            # Write(VGroup(label1, label2, label3)),
        # )
        # self.play(
            # MoveAlongPath(dot1, line1, rate_func=rate_functions.ease_in_sine),
            # MoveAlongPath(dot2, line2, rate_func=rate_functions.ease_out_sine),
            # MoveAlongPath(dot3, line3, rate_func=rate_functions.ease_in_out_sine),
            # run_time=7
        # )
        # self.wait()
####################################        
# class MatrixExamples(Scene):
    # def construct(self):
        # m0 = Matrix([[2, 0], [-1, 1]])
        # m1 = Matrix([[1, 0], [0, 1]],
                    # left_bracket="\\big(",
                    # right_bracket="\\big)")
        # m2 = DecimalMatrix(
            # [[3.456, 2.122], [33.2244, 12.33]],
            # element_to_mobject_config={"num_decimal_places": 2},
            # left_bracket="\\{",
            # right_bracket="\\}")

        # self.add(m0.shift(LEFT - (3, 0, 0)))
        # self.add(m1)
        # self.add(m2.shift(RIGHT + (3, 0, 0)))
#########################################              
# class Formula(Scene):
    # def construct(self):
        # t = MathTex(r"\int_a^b f'(x) dx = f(b)- f(a)")
        # self.add(t)
#############################        
# class ExampleCylinder(ThreeDScene):
    # def construct(self):
        # axes = ThreeDAxes()
        # cylinder = Cylinder(radius=2, height=3)
        # self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        # self.add(axes, cylinder)
####################################        
#from manim import Circle, Scene, ShowCreation, Text, Uncreate, VGroup
# class CircleWithContent(VGroup):
    # def __init__(self, content):
        # super().__init__()
        # self.circle = Circle()
        # self.content = content
        # self.add(self.circle, content)
        # content.move_to(self.circle.get_center())

    # def clear_content(self):
        # self.remove(self.content)
        # self.content = None

    # @override_animate(clear_content)
    # def _clear_content_animation(self):
        # anim = Uncreate(self.content)
        # self.clear_content()
        # return anim

# class AnimationOverrideExample(Scene):
    # def construct(self):
        # t = Text("hello!")
        # my_mobject = CircleWithContent(t)
        # self.play(ShowCreation(my_mobject))
        # self.play(my_mobject.animate.clear_content())
        # self.wait()
##################################### 
# class ExampleArrow3D(ThreeDScene):
    # def construct(self):
        # axes = ThreeDAxes()
        # arrow = Arrow3D(start=np.array([0, 0, 0]), end=np.array([2, 2, 2]))
        # self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        # self.add(axes, arrow)
######################################        
# class MovingSquareWithUpdaters(Scene):
    # def construct(self):
        # decimal = DecimalNumber(
            # 0,
            # show_ellipsis=True,
            # num_decimal_places=3,
            # include_sign=True,
        # )
        # square = Square().to_edge(UP)

        # decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        # decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        # self.add(square, decimal)
        # self.play(
            # square.animate.to_edge(DOWN),
            # rate_func=there_and_back,
            # run_time=5,
        # )
        # self.wait()
################################################
# class ExampleCone(ThreeDScene):
    # def construct(self):
        # axes = ThreeDAxes()
        # cone = Cone(direction=X_AXIS+Y_AXIS+2*Z_AXIS)
        # self.set_camera_orientation(phi=5*PI/11, theta=PI/9)
        # self.add(axes, cone)
###################################
# class ExampleLine3D(ThreeDScene):
    # def construct(self):
        # axes = ThreeDAxes()
        # line = Line3D(start=np.array([0, 0, 0]), end=np.array([2, 2, 2]))
        # self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        # self.add(axes, line)
##################################
# class ExampleTorus(ThreeDScene):
    # def construct(self):
        # axes = ThreeDAxes()
        # torus = Torus()
        # self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        # self.add(axes, torus)
#################################
# class DashedLineExample(Scene):
    # def construct(self):
        # dashed_line = DashedLine(config.frame_width/2*LEFT, 4*RIGHT)
        # self.add(dashed_line)
#################################
# from manim import *
# class DashedLineExample2(Scene):
    # def construct(self):
        # # dash_length increased
        # dashed_1 = DashedLine(config.left_side, config.right_side, dash_length=2.0).shift(UP*2)
        # # normal
        # dashed_2 = DashedLine(config.left_side, config.right_side)
        # # positive_space_ratio decreased
        # dashed_3 = DashedLine(config.left_side, config.right_side, positive_space_ratio=0.1).shift(DOWN*2)
        # self.add(dashed_1, dashed_2, dashed_3)
##################################################        
# class RightArcAngleExample(Scene):
    # def construct(self):
        # line1 = Line( LEFT, RIGHT )
        # line2 = Line( DOWN, UP )
        # rightarcangles = [
            # Angle(line1, line2, dot=True),
            # Angle(line1, line2, radius=0.4, quadrant=(1,-1), dot=True, other_angle=True),
            # Angle(line1, line2, radius=0.5, quadrant=(-1,1), stroke_width=8, dot=True, dot_color=YELLOW, dot_radius=0.04, other_angle=True),
            # Angle(line1, line2, radius=0.7, quadrant=(-1,-1), color=RED, dot=True, dot_color=GREEN, dot_radius=0.08),
        # ]
        # line_list = VGroup( *[VGroup() for k in range(4)] )
        # for k in range(4):
            # linea = line1.copy()
            # lineb = line2.copy()
            # line_list[k].add( linea )
            # line_list[k].add( lineb )
            # line_list[k].add( rightarcangles[k] )
        # line_list.arrange_in_grid(buff=1.5)
        # self.add(
            # line_list
        # )
##################################################
# class AngleExample(Scene):
    # def construct(self):
        # line1 = Line( LEFT + (1/3) * UP, RIGHT + (1/3) * DOWN )
        # line2 = Line( DOWN + (1/3) * RIGHT, UP + (1/3) * LEFT )
        # angles = [
            # Angle(line1, line2),
            # Angle(line1, line2, radius=0.4, quadrant=(1,-1), other_angle=True),
            # Angle(line1, line2, radius=0.5, quadrant=(-1,1), stroke_width=8, other_angle=True),
            # Angle(line1, line2, radius=0.7, quadrant=(-1,-1), color=RED),
            # Angle(line1, line2, other_angle=True),
            # Angle(line1, line2, radius=0.4, quadrant=(1,-1)),
            # Angle(line1, line2, radius=0.5, quadrant=(-1,1), stroke_width=8),
            # Angle(line1, line2, radius=0.7, quadrant=(-1,-1), color=RED, other_angle=True),
        # ]
        # line_list = VGroup( *[VGroup() for k in range(8)] )
        # for k in range(8):
            # linea = line1.copy()
            # lineb = line2.copy()
            # line_list[k].add( linea )
            # line_list[k].add( lineb )
            # line_list[k].add( angles[k] )
        # line_list.arrange_in_grid(n_rows=2, n_cols=4, buff=1.5)
        # self.add(
            # line_list
        # )
##########################################        
# from manim.mobject.geometry import ArrowSquareTip        
# class ArrowExample(Scene):
    # def construct(self):
        # arrow_1 = Arrow(start=RIGHT, end=LEFT, color=GOLD)
        # arrow_2 = Arrow(start=RIGHT, end=LEFT, color=GOLD, tip_shape=ArrowSquareTip).shift(DOWN)
        # g1 = Group(arrow_1, arrow_2)

        # # the effect of buff
        # square = Square(color=MAROON_A)
        # arrow_3 = Arrow(start=LEFT, end=RIGHT)
        # arrow_4 = Arrow(start=LEFT, end=RIGHT, buff=0).next_to(arrow_1, UP)
        # g2 = Group(arrow_3, arrow_4, square)

        # # a shorter arrow has a shorter tip and smaller stroke width
        # arrow_5 = Arrow(start=ORIGIN, end=config.top).shift(LEFT * 4)
        # arrow_6 = Arrow(start=config.top + DOWN, end=config.top).shift(LEFT * 3)
        # g3 = Group(arrow_5, arrow_6)

        # self.add(Group(g1, g2, g3).arrange(buff=2))
        
#############################################
# from manim.mobject.geometry import ArrowTriangleTip, ArrowSquareTip, ArrowSquareFilledTip,\
                                # ArrowCircleTip, ArrowCircleFilledTip
# class ArrowTipsShowcase(Scene):
    # def construct(self):
        # a00 = Arrow(start=[-2, 3, 0], end=[2, 3, 0], color=YELLOW)
        # a11 = Arrow(start=[-2, 2, 0], end=[2, 2, 0], tip_shape=ArrowTriangleTip)
        # a12 = Arrow(start=[-2, 1, 0], end=[2, 1, 0])
        # a21 = Arrow(start=[-2, 0, 0], end=[2, 0, 0], tip_shape=ArrowSquareTip)
        # a22 = Arrow([-2, -1, 0], [2, -1, 0], tip_shape=ArrowSquareFilledTip)
        # a31 = Arrow([-2, -2, 0], [2, -2, 0], tip_shape=ArrowCircleTip)
        # a32 = Arrow([-2, -3, 0], [2, -3, 0], tip_shape=ArrowCircleFilledTip)
        # b11 = a11.copy().scale(0.5, scale_tips=True).next_to(a11, RIGHT)
        # b12 = a12.copy().scale(0.5, scale_tips=True).next_to(a12, RIGHT)
        # b21 = a21.copy().scale(0.5, scale_tips=True).next_to(a21, RIGHT)
        # self.add(a00, a11, a12, a21, a22, a31, a32, b11, b12, b21)
############################################
# class CircleSurround(Scene):
    # def construct(self):
        # triangle1 = Triangle()
        # circle1 = Circle().surround(triangle1)
        # group1 = Group(triangle1,circle1) # treat the two mobjects as one

        # line2 = Line()
        # circle2 = Circle().surround(line2, buffer_factor=2.0)
        # group2 = Group(line2,circle2)

        # # buffer_factor < 1, so the circle is smaller than the square
        # square3 = Square()
        # circle3 = Circle().surround(square3, buffer_factor=0.5)
        # group3 = Group(square3, circle3)

        # group = Group(group1, group2, group3).arrange(buff=1)
        # self.add(group)  
#####################################################
# from manim import *
# from manim.mobject.geometry import ArrowCircleFilledTip
# class DoubleArrowExample(Scene):
    # def construct(self):
        # circle = Circle(radius=2.0)
        # d_arrow = DoubleArrow(start=circle.get_left(), end=circle.get_right())
        # d_arrow_2 = DoubleArrow(tip_shape_end=ArrowCircleFilledTip, tip_shape_start=ArrowCircleFilledTip)
        # group = Group(Group(circle, d_arrow), d_arrow_2).arrange(UP, buff=1)
        # self.add(group)
#########################################################        
# from manim import *
# class SoundExample(Scene):
    # # Source of sound under Creative Commons 0 License. https://freesound.org/people/Druminfected/sounds/250551/
    # def construct(self):
        # dot = Dot().set_color(GREEN)
        # self.add_sound("click.wav")
        # self.add(dot)
        # self.wait()
        # self.add_sound("click.wav")
        # dot.set_color(BLUE)
        # self.wait()
        # self.add_sound("click.wav")
        # dot.set_color(RED)
        # self.wait()  
#########################################################
# from manim import *
# class MovingVertices(Scene):
    # def construct(self):
        # vertices = [1, 2, 3, 4]
        # edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        # g = Graph(vertices, edges)
        # self.play(Create(g))
        # self.wait()
        # self.play(g[1].animate.move_to([1, 1, 0]),
                  # g[2].animate.move_to([-1, 1, 0]),
                  # g[3].animate.move_to([1, -1, 0]),
                  # g[4].animate.move_to([-1, -1, 0]))
        # self.wait()
#############################
# from manim import *
# class GraphAutoPosition(Scene):
    # def construct(self):
        # vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        # edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 # (2, 8), (3, 4), (6, 1), (6, 2),
                 # (6, 3), (7, 2), (7, 4)]
        # autolayouts = ["spring", "circular", "kamada_kawai",
                       # "planar", "random", "shell",
                       # "spectral", "spiral"]
        # graphs = [Graph(vertices, edges, layout=lt).scale(0.5)
                  # for lt in autolayouts]
        # r1 = VGroup(*graphs[:3]).arrange()
        # r2 = VGroup(*graphs[3:6]).arrange()
        # r3 = VGroup(*graphs[6:]).arrange()
        # self.add(VGroup(r1, r2, r3).arrange(direction=DOWN))
####################################################
# from manim import *
# class GraphManualPosition(Scene):
    # def construct(self):
        # vertices = [1, 2, 3, 4]
        # edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
        # lt = {1: [0, 0, 0], 2: [1, 1, 0], 3: [1, -1, 0], 4: [-1, 0, 0]}
        # G = Graph(vertices, edges, layout=lt)
        # self.add(G) 
####################################################
# from manim import *

# class LabeledModifiedGraph(Scene):
    # def construct(self):
        # vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        # edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 # (2, 8), (3, 4), (6, 1), (6, 2),
                 # (6, 3), (7, 2), (7, 4)]
        # g = Graph(vertices, edges, layout="circular", layout_scale=3,
                  # labels=True, vertex_config={7: {"fill_color": RED}},
                  # edge_config={(1, 7): {"stroke_color": RED},
                               # (2, 7): {"stroke_color": RED},
                               # (4, 7): {"stroke_color": RED}})
        # self.add(g)
######################################################        
# from manim import *

# import networkx as nx

# class PartiteGraph(Scene):
    # def construct(self):
        # G = nx.Graph()
        # G.add_nodes_from([0, 1, 2, 3])
        # G.add_edges_from([(0, 2), (0,3), (1, 2)])
        # graph = Graph(list(G.nodes), list(G.edges), layout="partite", partitions=[[0, 1]])
        # self.play(Create(graph))
#######################################################
# from manim import *
# import networkx as nx
# class Tree(Scene):
    # def construct(self):
        # G = nx.Graph()

        # G.add_node("ROOT")

        # for i in range(5):
            # G.add_node("Child_%i" % i)
            # G.add_node("Grandchild_%i" % i)
            # G.add_node("Greatgrandchild_%i" % i)

            # G.add_edge("ROOT", "Child_%i" % i)
            # G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
            # G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)

        # self.play(Create(
            # Graph(list(G.nodes), list(G.edges), layout="tree", root_vertex="ROOT")))
########################################################
#from manim import *

# class ChangeGraphLayout(Scene):
    # def construct(self):
        # G = Graph([1, 2, 3, 4, 5], [(1, 2), (2, 3), (3, 4), (4, 5)],
                  # layout={1: [-2, 0, 0], 2: [-1, 0, 0], 3: [0, 0, 0],
                          # 4: [1, 0, 0], 5: [2, 0, 0]}
                  # )
        # self.play(Create(G))
        # self.play(G.animate.change_layout("circular"))
        # self.wait()
###########################################################
# from manim import *

# import networkx as nx

# nxgraph = nx.erdos_renyi_graph(14, 0.5)

# class ImportNetworkxGraph(Scene):
    # def construct(self):
        # G = Graph.from_networkx(nxgraph, layout="spring", layout_scale=3.5)
        # self.play(Create(G))
        # self.play(*[G[v].animate.move_to(5*RIGHT*np.cos(ind/7 * PI) +
                                         # 3*UP*np.sin(ind/7 * PI))
                    # for ind, v in enumerate(G.vertices)])
        # self.play(Uncreate(G))
###########################################################
# from manim import *
# class EllipseExample(Scene):
    # def construct(self):
        # ellipse_1 = Ellipse(width=2.0, height=4.0, color=BLUE_B)
        # ellipse_2 = Ellipse(width=4.0, height=1.0, color=BLUE_D)
        # ellipse_group = Group(ellipse_1,ellipse_2).arrange(buff=1)
        # self.add(ellipse_group)
###########################################################
# from manim import *
# class SeveralLabeledDots(Scene):
    # def construct(self):
        # sq = Square(fill_color=RED, fill_opacity=1)
        # self.add(sq)
        # dot1 = LabeledDot(Tex("42", color=RED))
        # dot2 = LabeledDot(MathTex("a", color=GREEN))
        # dot3 = LabeledDot(Text("ii", color=BLUE))
        # dot4 = LabeledDot("3")
        # dot1.next_to(sq, UL)
        # dot2.next_to(sq, UR)
        # dot3.next_to(sq, DL)
        # dot4.next_to(sq, DR)
        # self.add(dot1, dot2, dot3, dot4)
###########################################################
# from manim import *
# class RightAngleExample(Scene):
    # def construct(self):
        # line1 = Line( LEFT, RIGHT )
        # line2 = Line( DOWN, UP )
        # rightangles = [
            # RightAngle(line1, line2),
            # RightAngle(line1, line2, length=0.4, quadrant=(1,-1)),
            # RightAngle(line1, line2, length=0.5, quadrant=(-1,1), stroke_width=8),
            # RightAngle(line1, line2, length=0.7, quadrant=(-1,-1), color=RED),
        # ]
        # line_list = VGroup( *[VGroup() for k in range(4)] )
        # for k in range(4):
            # linea = line1.copy()
            # lineb = line2.copy()
            # line_list[k].add( linea )
            # line_list[k].add( lineb )
            # line_list[k].add( rightangles[k] )
        # line_list.arrange_in_grid(buff=1.5)
        # self.add(
            # line_list
        # )  
###########################################################
# from manim import *
# class AnimateChainExample(Scene):
    # def construct(self):
        # s = Square()
        # self.play(Create(s))
        # self.play(s.animate.shift(RIGHT).scale(2).rotate(PI / 2))
        # self.play(Uncreate(s))        
#############################################################
# from manim import *
# class AnimateWithArgsExample(Scene):
    # def construct(self):
        # s = Square()
        # c = Circle()

        # VGroup(s, c).arrange(RIGHT, buff=2)
        # self.add(s, c)

        # self.play(
            # s.animate(run_time=2).rotate(PI / 2),
            # c.animate(rate_func=there_and_back).shift(RIGHT)
        # )
#############################################################
# from manim import *
# class ArrangeInGrid(Scene):
    # def construct(self):
        # #Add some numbered boxes:
        # np.random.seed(3)
        # boxes = VGroup(*[
            # Rectangle(WHITE, np.random.random()+.5, np.random.random()+.5).add(Text(str(i+1)).scale(0.5))
            # for i in range(22)
        # ])
        # self.add(boxes)

        # boxes.arrange_in_grid(
            # buff=(0.25,0.5),
            # col_alignments="lccccr",
            # row_alignments="uccd",
            # col_widths=[2, *[None]*4, 2],
            # flow_order="dr"
        # )
#############################################################
# from manim import *
# class AngleMidPoint(Scene):
    # def construct(self):
        # line1 = Line(ORIGIN, 2*RIGHT)
        # line2 = Line(ORIGIN, 2*RIGHT).rotate_about_origin(80*DEGREES)
        # a = Angle(line1, line2, radius=1.5, other_angle=False)
        # d = Dot(a.get_midpoint()).set_color(RED)
        # self.add(line1, line2, a, d)
        # self.wait()
##############################################################      
# from manim import *
# class InvertSumobjectsExample(Scene):
    # def construct(self):
        # s= VGroup(*[Dot().shift(i*0.1*RIGHT) for i in range(-20,20)])
        # s2= s.copy()
        # s2.invert()
        # s2.shift(DOWN)
        # self.play(Write(s), Write(s2))
##############################################################      
# from manim import *
# class MatchPointsScene(Scene):
    # def construct(self):
        # circ = Circle(fill_color=RED, fill_opacity=0.8)
        # square = Square(fill_color=BLUE, fill_opacity=0.2)
        # self.add(circ)
        # self.wait(0.5)
        # self.play(circ.animate.match_points(square))
        # self.wait(0.5)
##############################################################      
# from manim import *
# class IncorrectLaTeXSubstringColoring(Scene):
    # def construct(self):
        # equation = MathTex(
            # r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots"
        # )
        # equation.set_color_by_tex("x", YELLOW)
        # self.add(equation)
##############################################################                
# from manim import *
# class CorrectLaTeXSubstringColoring(Scene):
    # def construct(self):
        # equation = MathTex(
            # r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            # substrings_to_isolate="x"
        # )
        # equation.set_color_by_tex("x", YELLOW)
        # self.add(equation)
##############################################################                        
# from manim import *
# class Dot3DExample(ThreeDScene):
    # def construct(self):
        # self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        # axes = ThreeDAxes()
        # dot_1 = Dot3D(color=RED).move_to(axes.coords_to_point(0, 0, 1))
        # dot_2 = Dot3D(radius=0.1, color=BLUE).move_to(axes.coords_to_point(2, 0, 0))
        # self.add(axes, dot_1, dot_2)
##############################################################                                
# from manim import *
# class ValueTrackerExample(Scene):
    # def construct(self):
        # number_line = NumberLine()
        # pointer = Vector(DOWN)
        # label = MathTex("x").add_updater(lambda m: m.next_to(pointer, UP))

        # pointer_tracker = ValueTracker(0)
        # pointer.add_updater(
            # lambda m: m.next_to(
                        # number_line.n2p(pointer_tracker.get_value()),
                        # UP
                    # )
        # )
        # self.add(number_line, pointer,label)
        # pointer_tracker += 1.5
        # self.wait(1)
        # pointer_tracker -= 4
        # self.wait(0.5)
        # self.play(pointer_tracker.animate.set_value(5)),
        # self.wait(0.5)
        # self.play(pointer_tracker.animate.set_value(3))
        # self.play(pointer_tracker.animate.increment_value(-2))
        # self.wait(0.5)
##############################################################                        
# from manim import *
# class ShapesWithVDict(Scene):
    # def construct(self):
        # square = Square().set_color(RED)
        # circle = Circle().set_color(YELLOW).next_to(square, UP)

        # # create dict from list of tuples each having key-mobject pair
        # pairs = [("s", square), ("c", circle)]
        # my_dict = VDict(pairs, show_keys=True)

        # # display it just like a VGroup
        # self.play(Create(my_dict))
        # self.wait()

        # text = Tex("Some text").set_color(GREEN).next_to(square, DOWN)

        # # add a key-value pair by wrapping it in a single-element list of tuple
        # # after attrs branch is merged, it will be easier like `.add(t=text)`
        # my_dict.add([("t", text)])
        # self.wait()

        # rect = Rectangle().next_to(text, DOWN)
        # # can also do key assignment like a python dict
        # my_dict["r"] = rect

        # # access submobjects like a python dict
        # my_dict["t"].set_color(PURPLE)
        # self.play(my_dict["t"].animate.scale(3))
        # self.wait()

        # # also supports python dict styled reassignment
        # my_dict["t"] = Tex("Some other text").set_color(BLUE)
        # self.wait()

        # # remove submobject by key
        # my_dict.remove("t")
        # self.wait()

        # self.play(Uncreate(my_dict["s"]))
        # self.wait()

        # self.play(FadeOut(my_dict["c"]))
        # self.wait()

        # self.play(FadeOutAndShift(my_dict["r"], DOWN))
        # self.wait()

        # # you can also make a VDict from an existing dict of mobjects
        # plain_dict = {
            # 1: Integer(1).shift(DOWN),
            # 2: Integer(2).shift(2 * DOWN),
            # 3: Integer(3).shift(3 * DOWN),
        # }

        # vdict_from_plain_dict = VDict(plain_dict)
        # vdict_from_plain_dict.shift(1.5 * (UP + LEFT))
        # self.play(Create(vdict_from_plain_dict))

        # # you can even use zip
        # vdict_using_zip = VDict(zip(["s", "c", "r"], [Square(), Circle(), Rectangle()]))
        # vdict_using_zip.shift(1.5 * RIGHT)
        # self.play(Create(vdict_using_zip))
        # self.wait()     
##################################################################
# from manim import *
# class AddToVGroup(Scene):
    # def construct(self):
        # circle_red = Circle(color=RED)
        # circle_green = Circle(color=GREEN)
        # circle_blue = Circle(color=BLUE)
        # circle_red.shift(LEFT)
        # circle_blue.shift(RIGHT)
        # gr = VGroup(circle_red, circle_green)
        # gr2 = VGroup(circle_blue) # Constructor uses add directly
        # self.add(gr,gr2)
        # self.wait()
        # gr += gr2 # Add group to another
        # self.play(
            # gr.animate.shift(DOWN),
        # )
        # gr -= gr2 # Remove group
        # self.play( # Animate groups separately
            # gr.animate.shift(LEFT),
            # gr2.animate.shift(UP),
        # )
        # self.play( #Animate groups without modification
            # (gr+gr2).animate.shift(RIGHT)
        # )
        # self.play( # Animate group without component
            # (gr-circle_red).animate.shift(RIGHT)
        # )  
#################################################################
# from manim import *
# class UseZoomedScene(ZoomedScene):
    # def construct(self):
        # dot = Dot().set_color(GREEN)
        # self.add(dot)
        # self.wait(1)
        # self.activate_zooming(animate=False)
        # self.wait(1)
        # self.play(dot.animate.shift(LEFT))
#################################################################
# from manim import *
# class ChangingZoomScale(ZoomedScene):
    # def __init__(self, **kwargs):
        # ZoomedScene.__init__(
            # self,
            # zoom_factor=0.3,
            # zoomed_display_height=1,
            # zoomed_display_width=3,
            # image_frame_stroke_width=20,
            # zoomed_camera_config={
                # "default_frame_stroke_width": 3,
            # },
            # **kwargs
        # )
    # def construct(self):
        # dot = Dot().set_color(GREEN)
        # sq = Circle(fill_opacity=1, radius=0.2).next_to(dot, RIGHT)
        # self.add(dot, sq)
        # self.wait(1)
        # self.activate_zooming(animate=False)
        # self.wait(1)
        # self.play(dot.animate.shift(LEFT * 0.3))

        # self.play(self.zoomed_camera.frame.animate.scale(4))
        # self.play(self.zoomed_camera.frame.animate.shift(0.5 * DOWN))  
######################################################################
# from manim import *
# class CreateScene(Scene):
    # def construct(self):
        # self.play(Create(Square()))  
######################################################################
# from manim import *
# class UnwriteReverseFalse(Scene):
    # def construct(self):
        # text = Tex("Alice and Bob").scale(3)
        # self.add(text)
        # self.play(Unwrite(text))
######################################################################
# from manim import *
# class UnwriteReverseTrue(Scene):
    # def construct(self):
        # text = Tex("Alice and Bob").scale(3)
        # self.add(text)
        # self.play(Unwrite(text,reverse=True))
######################################################################
# from manim import *
# class FadeTransformSubmobjects(Scene):
    # def construct(self):
        # src = VGroup(Square(), Circle().shift(LEFT + UP))
        # src.shift(3*LEFT + 2*UP)
        # src_copy = src.copy().shift(4*DOWN)

        # target = VGroup(Circle(), Triangle().shift(RIGHT + DOWN))
        # target.shift(3*RIGHT + 2*UP)
        # target_copy = target.copy().shift(4*DOWN)

        # self.play(FadeIn(src), FadeIn(src_copy))
        # self.play(
            # FadeTransform(src, target),
            # FadeTransformPieces(src_copy, target_copy)
        # )
        # self.play(*[FadeOut(mobj) for mobj in self.mobjects])
########################################################################
# from manim import *
# class FilledAngle(Scene):
    # def construct(self):
        # l1 = Line(ORIGIN, 2 * UP + RIGHT).set_color(GREEN)
        # l2 = (
            # Line(ORIGIN, 2 * UP + RIGHT)
            # .set_color(GREEN)
            # .rotate(-20 * DEGREES, about_point=ORIGIN)
        # )
        # norm = l1.get_length()
        # a1 = Angle(l1, l2, other_angle=True, radius=norm - 0.5).set_color(GREEN)
        # a2 = Angle(l1, l2, other_angle=True, radius=norm).set_color(GREEN)
        # q1 = a1.get_points() #  save all coordinates of points of angle a1
        # q2 = a2.reverse_direction().get_points()  #  save all coordinates of points of angle a1 (in reversed direction)
        # pnts = np.concatenate([q1, q2, q1[0].reshape(1, 3)])  # adds points and ensures that path starts and ends at same point
        # mfill = VMobject().set_color(ORANGE)
        # mfill.set_points_as_corners(pnts).set_fill(GREEN, opacity=1)
        # self.add(l1, l2)
        # self.add(mfill)
###############################################        
# from manim import *
# class UsingCircumscribe(Scene):
    # def construct(self):
        # lbl = Tex(r"Circum-\\scribe").scale(2)
        # self.add(lbl)
        # self.play(Circumscribe(lbl))
        # self.play(Circumscribe(lbl, Circle))
        # self.play(Circumscribe(lbl, fade_out=True))
        # self.play(Circumscribe(lbl, time_width=2))
        # self.play(Circumscribe(lbl, Circle, True))
###############################################        
# from manim import *
# class DifferentFadeTransforms(Scene):
    # def construct(self):
        # starts = [Rectangle(width=4, height=1) for _ in range(3)]
        # VGroup(*starts).arrange(DOWN, buff=1).shift(3*LEFT)
        # targets = [Circle(fill_opacity=1).scale(0.25) for _ in range(3)]
        # VGroup(*targets).arrange(DOWN, buff=1).shift(3*RIGHT)

        # self.play(*[FadeIn(s) for s in starts])
        # self.play(
            # FadeTransform(starts[0], targets[0], stretch=True),
            # FadeTransform(starts[1], targets[1], stretch=False, dim_to_match=0),
            # FadeTransform(starts[2], targets[2], stretch=False, dim_to_match=1)
        # )
        # self.play(*[FadeOut(mobj) for mobj in self.mobjects])
##################################################################        
# class ApplyingWaves(Scene):
    # def construct(self):
        # tex = Tex("WaveWaveWaveWaveWave").scale(2)
        # self.play(ApplyWave(tex))
        # self.play(ApplyWave(
            # tex,
            # direction=RIGHT,
            # time_width=0.5,
            # amplitude=0.3
        # ))
        # self.play(ApplyWave(
            # tex,
            # rate_func=linear,
            # ripples=4
        # ))
###############################################        
# class DarkThemeBanner(Scene):
    # def construct(self):
        # banner = ManimBanner()
        # self.play(banner.create())
        # self.play(banner.expand())
        # self.wait()
        # self.play(Unwrite(banner))
###############################################                
# from manim import *
# class LightThemeBanner(Scene):
    # def construct(self):
        # self.camera.background_color = "#ece6e2"
        # banner = ManimBanner(dark_theme=False)
        # self.play(banner.create())
        # self.play(banner.expand())
        # self.wait()
        # self.play(Unwrite(banner))
###############################################                
# from manim import *
# class ExpandDirections(Scene):
    # def construct(self):
        # banners = [ManimBanner().scale(0.5).shift(UP*x) for x in [-2, 0, 2]]
        # self.play(
            # banners[0].expand(direction="right"),
            # banners[1].expand(direction="center"),
            # banners[2].expand(direction="left"),
        # )
###############################################                
# from manim import *
# class SpawningAndFlowingArea(Scene):
    # def construct(self):
        # func = lambda pos: np.sin(pos[0])*UR+np.cos(pos[1])*LEFT+pos/5
        # stream_lines = StreamLines(
            # func,
            # x_min=-3, x_max=3, delta_x=0.2,
            # y_min=-2, y_max=2, delta_y=0.2,
            # padding=1
        # )

        # spawning_area = Rectangle(width=6, height=4)
        # flowing_area = Rectangle(width=8, height=6)
        # labels = [
            # Tex("Spawning Area"),
            # Tex("Flowing Area").shift(DOWN*2.5)
        # ]
        # for lbl in labels:
            # lbl.add_background_rectangle(opacity=0.6, buff=0.05)
        # self.add(stream_lines, spawning_area, flowing_area, *labels)
##########################################################################        
# from manim import *
# class StreamLineCreation(Scene):
    # def construct(self):
        # func = lambda pos: (pos[0]*UR+pos[1]*LEFT) - pos
        # stream_lines = StreamLines(
            # func,
            # color=YELLOW,
            # delta_x=1, delta_y=1, stroke_width=3,
            # virtual_time=1,          # use shorter lines
            # max_anchors_per_line=5,  #better performance with fewer anchors
        # )
        # self.play(stream_lines.create()) # uses virtual_time as run_time
        # self.wait()
##########################################################################
# from manim import *
# class EndAnimation(Scene):
    # def construct(self):
        # func = lambda pos: np.sin(pos[0]/2)*UR+np.cos(pos[1]/2)*LEFT
        # stream_lines = StreamLines(
            # func, stroke_width=3,
            # max_anchors_per_line=5,
            # virtual_time=1, color=BLUE
        # )
        # self.add(stream_lines)
        # stream_lines.start_animation(
            # warm_up=False,
            # flow_speed=1.5,
            # time_width=0.5
        # )
        # self.wait(1)
        # self.play(stream_lines.end_animation()) 
###########################################################################
# from manim import *
# class ContinuousMotion(Scene):
    # def construct(self):
        # func = lambda pos: np.sin(pos[0]/2)*UR+np.cos(pos[1]/2)*LEFT
        # stream_lines = StreamLines(
            # func, stroke_width=3,
            # max_anchors_per_line=30
        # )
        # self.add(stream_lines)
        # stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        # self.wait(stream_lines.virtual_time / stream_lines.flow_speed)