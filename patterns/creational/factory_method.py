# -*- coding: utf-8 -*-
"""Factory method
- A factory method provide the possiblity to create objects
without knowing the exact class of those objects.

*Use case:
- When you do not know the exact types of the objects you should create in your code
and new types in the future can be created by you or you developers clients. (maintainability)

*Advantages
- Sepration between the creator and the concrete products.
- Single Responsibility Principle. You can move the product creation code
  into one place in the program, making the code easier to support.
- Open/Closed Principle. You can introduce new types of products into
  the program without breaking existing client code.

*Example:
- This example shows us how to train players through
coachs classes without worring about which player class to instanciate.
"""

from abc import ABC, abstractmethod


__author__ = "Rami BELGACEM"
__copyright__ = "Copyright 2022"
__license__ = "GPL"

__version__ = "1.0"
__maintainer__ = "Rami BELGACEM"
__email__ = "ramibelgacem@gmail.com"
__status__ = "Development"


class Player(ABC):
    """This interface define the action that all subclasses must implement"""

    @abstractmethod
    def action(self):
        """The action can a player do"""
        pass


class GoalKeeper(Player):
    def action(self):
        print("Catch the ball")


class Attacker(Player):
    def action(self):
        print("Mark a goal")


class Defender(Player):
    def action(self):
        print("Defend the goal")


# Factory class
class FactoryCoach(ABC):

    @abstractmethod
    def _match_player(self):
        """Factory method that will match the player
        that will be trained by this coach

        :return Player"""
        pass

    def train(self):
        """Apply training on the player"""
        player = self._match_player()
        player.action()


class GoalKeeperCoach(FactoryCoach):
    def _match_player(self):
        return GoalKeeper()


class TeamCoach(FactoryCoach):
    def _match_player(self):
        return Attacker()


# Client
if __name__ == '__main__':
    # start team training
    coach = TeamCoach()
    coach.train()

    # start goal keep training
    gkcoach = GoalKeeperCoach()
    gkcoach.train()
