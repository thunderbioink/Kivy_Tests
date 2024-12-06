from kivy.app import App
from kivy.graphics import Rectangle, Line
from kivy.uix.widget import Widget
# Drawing app mode test 


class MyWidget(Widget):
	def on_touch_down(self, touch):
		touch.ud['line'] = Line(points=(touch.x, touch.y))
		self.canvas.add(touch.ud['line'])

	def on_touch_move(self, touch):
		touch.ud['line'].points += [touch.x, touch.y]



class FoodsReadyApp(App):
	def build(self):
		return MyWidget()
if __name__ == '__main__':
	FoodsReadyApp().run()


