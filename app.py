from app import App
from app_components import clear_background
from power import BatteryLevel

class Battery(App):
  def __init__(self):
    pass

  def update(self, delta):
    pass

  def draw(self, ctx):
    ctx.save()
    ctx.text_align = ctx.CENTER
    ctx.text_baseline = ctx.MIDDLE
    clear_background(ctx)
    label = f"{(BatteryLevel()/106.25)*100:.2f}%"
    ctx.move_to(0, 0).gray(1).text(label)
    ctx.restore()

__app_export__ = Battery
