from engine.main import Game
import scriptblue
import scriptred
import script
from sample_scripts import sample1,sample2,sample3


if __name__ == "__main__":
    G = Game((40, 40), script, sample3)
    G.run_game()