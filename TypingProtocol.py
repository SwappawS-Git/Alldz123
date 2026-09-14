from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str: ...
        
def render(Draw_obj: Drawable) -> None:
    print(Draw_obj.draw())
class Circle:
    def draw(self) -> str:
        return "O"
class Romb:
    def draw(self) -> str:
        return "<>"

render(Circle())
render(Romb())