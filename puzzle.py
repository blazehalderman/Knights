from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Since it cannot be both a knight and a knave, we must choose either one
    Or(And(Not(AKnight), AKnave), And(AKnight, Not(AKnave))),
    #logic for when the question is a knave
    Implication(AKnave, Not(And(AKnight, AKnave))),
    #logic for when the question is a knight
    Implication(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.

knowledge1 = And(
    #If there are two knaves then A is lying, making their be at least one knave, the knave is A, B says nothing
    # implication that they are both knaves, making them both liers
    And(Or(Not(AKnight), AKnight), Or(Not(AKnight), BKnight)),
    #when a is a knave, there cannot be both
    Implication(BKnight, AKnave),
    #when b is a knave, there cannot be both
    Implication(BKnave, Not(And(AKnave, BKnave))),
    #There is only one knave
    Or(And(Not(AKnight), AKnave), And(AKnight, Not(AKnave))),
    Or(And(Not(BKnight), BKnave), And(BKnight, Not(BKnave))),

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

knowledge2 = And(
    
    Implication( Not( And( Or( And(AKnave, BKnave), And(AKnight, BKnight) ), Or( And( Not(AKnave), BKnave ),  
    And( Not(AKnight), BKnight) ) ) ), Or( And (AKnight, BKnave), And (AKnave, AKnight) )),
    Implication(Or(And(AKnight, BKnave), And(AKnave, AKnight)), AKnave),
    Implication(AKnave, BKnight)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

knowledge3 = And(
    #A says they are either a knight or a knave, implying they are wishy washy, meaning they either are lying or telling the truth(Knights always tell the truth)
    #B states that A said they were a knave, which is true but also not completely true
        #Either knight/knave not or
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
    
    #implying that A is either a Knight or a Knave
    Or(
        And(Implication(AKnave, AKnight), Implication(AKnight, Not(AKnight))),
        And(Implication(AKnight, AKnight), Implication(AKnight, Not(AKnave)))
    ),
    #B states that C is a Knave
    Implication(BKnave, Not(And(Implication(AKnave, AKnight), Implication(AKnight, Not(AKnight))))),
    Implication(BKnight, And(Implication(AKnave, AKnight), Implication(AKnight, Not(AKnight)))),
    #C states A is a knight(Knight)
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),

    Implication(AKnight, CKnight),
    Implication(AKnave, CKnave)

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
