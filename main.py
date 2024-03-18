from engine.main import Game
# import scriptblue
import script
import sample1

if __name__ == "__main__":
    G = Game((40, 40), script, sample1)
    G.run_game()