from typing import Optional
import tcod.event
from actions import Action, EscapeAction, MovementAction

class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym
        match key:    # added numpad diagonals as acceptable input
            case tcod.event.K_KP_9:
                action = MovementAction(dx=1,dy=-1)
            case tcod.event.K_KP_7:
                action = MovementAction(dx=-1,dy=-1)
            case tcod.event.K_KP_1:
                action = MovementAction(dx=-1,dy=1)
            case tcod.event.K_KP_3:
                action = MovementAction(dx=1,dy=1) 
            case tcod.event.K_UP | tcod.event.K_KP_8:
                action = MovementAction(dx=0, dy=-1)
            case tcod.event.K_DOWN | tcod.event.K_KP_2:
                action = MovementAction(dx=0, dy=1)
            case tcod.event.K_LEFT | tcod.event.K_KP_4:
                action = MovementAction(dx=-1, dy=0)
            case tcod.event.K_RIGHT | tcod.event.K_KP_6:
                action = MovementAction(dx=1, dy=0)
            case tcod.event.K_ESCAPE:
                action = EscapeAction()

        return action
