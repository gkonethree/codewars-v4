from engine.main import Game
import scriptblue
import scriptred
import script

if __name__ == "__main__":
    G = Game((40, 40), script, scriptred)
    G.run_game()