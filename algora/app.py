from enum import Enum

class DanceMove(Enum):
    TWIRL = 1  # Movimento di danza: TWIRL
    LEAP = 2  # Movimento di danza: LEAP
    SPIN = 3  # Movimento di danza: SPIN

class FancyCreature:
    def __init__(self, name: str, dance_move: DanceMove):
        self.name = name  # Nome della creatura
        self.dance_move = dance_move  # Movimento di danza della creatura

    def combine_moves(self, other_creature: 'FancyCreature') -> str:
        if self.dance_move == DanceMove.TWIRL and other_creature.dance_move == DanceMove.TWIRL:
            return "Fireflies light up the forest."  # Effetto combinato: Lucciole illuminano la foresta
        elif (self.dance_move == DanceMove.LEAP and other_creature.dance_move == DanceMove.SPIN) or \
                (self.dance_move == DanceMove.SPIN and other_creature.dance_move == DanceMove.LEAP):
            return "Gentle rain starts falling."  # Effetto combinato: Inizia a piovere dolcemente
        elif (self.dance_move == DanceMove.SPIN and other_creature.dance_move == DanceMove.LEAP) or \
                (self.dance_move == DanceMove.LEAP and other_creature.dance_move == DanceMove.SPIN):
            return "A rainbow appears in the sky."  # Effetto combinato: Appare un arcobaleno nel cielo
        else:
            return "A magical effect of your choice happens."  # Effetto combinato: Un effetto magico a tua scelta accade

    def proceed_with_sequence(self, sequence: list[DanceMove]) -> None:
        for move in sequence:
            self.dance_move = move
            print(f"The creature {self.name} performs {move.name} dance move.")  # La creatura esegue un movimento di danza
            # Aggiungi eventuali logiche o azioni aggiuntive qui


class Lox(FancyCreature):
    def __init__(self):
        self.dance_moves = [DanceMove.TWIRL, DanceMove.LEAP, DanceMove.SPIN, DanceMove.TWIRL, DanceMove.LEAP]  # Mosse di danza di Lox
        super().__init__("Lox", self.dance_moves[0])  # Inizializza Lox con la prima mossa di danza

class Faelis(FancyCreature):
    def __init__(self):
        self.dance_moves = [DanceMove.SPIN, DanceMove.TWIRL, DanceMove.LEAP, DanceMove.LEAP, DanceMove.SPIN]  # Mosse di danza di Faelis
        super().__init__("Faelis", self.dance_moves[0])  # Inizializza Faelis con la prima mossa di danza

class Forest:
    def __init__(self):
        self.state = "Normal"  # Stato iniziale della foresta: Normale

    def change_state(self, effect: str) -> None:
        if effect == "Fireflies light up the forest.":
            self.state = "Illuminated"  # Stato della foresta: Illuminata
        elif effect == "Gentle rain starts falling.":
            self.state = "Rainy"  # Stato della foresta: Piovosa
        elif effect == "A rainbow appears in the sky.":
            self.state = "Rainbow"  # Stato della foresta: Arcobaleno
        else:
            self.state = "Magical"  # Stato della foresta: Magico

    def display_state(self) -> None:
        print(f"The forest is now {self.state}.")  # Mostra lo stato attuale della foresta

class Dance:
    def __init__(self, creature1: FancyCreature, creature2: FancyCreature, forest: Forest):
        self.creature1 = creature1  # Prima creatura
        self.creature2 = creature2  # Seconda creatura
        self.forest = forest  # Foresta

    def perform(self) -> None:
        sequence1 = self.creature1.dance_moves  # Sequenza di mosse di danza della prima creatura
        sequence2 = self.creature2.dance_moves  # Sequenza di mosse di danza della seconda creatura
        for move1, move2 in zip(sequence1, sequence2):
            self.creature1.proceed_with_sequence([move1])  # La prima creatura esegue la mossa di danza corrente
            self.creature2.proceed_with_sequence([move2])  # La seconda creatura esegue la mossa di danza corrente
            self.forest.change_state(self.creature1.combine_moves(self.creature2))  # Cambia lo stato della foresta in base all'effetto combinato delle mosse di danza
            self.forest.display_state()  # Mostra lo stato attuale della foresta

def main():
    # Inizializza lo stato della foresta
    forest = Forest()

    # Crea le creature e definisci le loro mosse di danza
    lox = Lox()
    faelis = Faelis()

    # Crea la danza con le creature e la foresta
    dance = Dance(lox, faelis, forest)

    # Esegui la danza
    dance.perform()

    # Mostra lo stato finale della foresta
    forest.display_state()

if __name__ == "__main__":
    main()
