from app import App
from app_components import clear_background
from power import BatteryLevel
from events.input import Buttons, BUTTON_TYPES

class Battery(App):
  def __init__(self):
    self.button_states = Buttons(self)

  def update(self, delta):if self.button_states.get(BUTTON_TYPES["CANCEL"]):
    # The button_states do not update while you are in the background.
    # Calling clear() ensures the next time you open the app, it stays open.
    # Without it the app would close again immediately.
    self.button_states.clear()
    self.minimise()

  def draw(self, ctx):
    ctx.save()
    ctx.text_align = ctx.CENTER
    ctx.text_baseline = ctx.MIDDLE
    clear_background(ctx)
    label = f"{(BatteryLevel()/106.25):.2f}%"
    ctx.move_to(0, 0).gray(1).text(label)
    ctx.restore()

__app_export__ = Battery