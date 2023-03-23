from typing import List, Optional

from pydantic import BaseModel

from .models import LanderAction, LanderData, LanderRotation, LanderStatus

LANDING_MAX_SPEED = 40
LANDING_MAX_ANGLE = 15

class Brain(BaseModel):
    player_name: str
    status: LanderStatus = LanderStatus.DEAD
    cycle: int = 0
    previous: Optional[LanderData] = None

    def handleLander(self, players : List[LanderData]) -> LanderAction:
        for player in players:
             if player.name == self.player_name:
                  break
        else:
             raise Exception("player not found in payload")
        if player.status != self.status:
            if self.previous:
                print("prev", self.previous)
            print(self.cycle, player)
            # NEW CYCLE !
            self.status = player.status
            self.cycle = 0

        thrust = False
        rotate = LanderRotation.NONE

        if abs(player.vx) > 35:
            if player.vx > 0:
                if player.angle < -20:
                    thrust = True
                else:
                    rotate = LanderRotation.COUNTERCLOCKWISE
            else:                
                if player.angle > 20:
                    thrust = True
                else:
                    rotate = LanderRotation.CLOCKWISE
        else:
            if player.angle > 10:
                    rotate = LanderRotation.COUNTERCLOCKWISE
            elif player.angle < -10:
                    rotate = LanderRotation.CLOCKWISE
            
            if player.altitude < 300 and player.vy > 30:
                thrust = True

        action = LanderAction(thrust=thrust, rotate=rotate)
        self.cycle += 1
        self.previous = player
        return action