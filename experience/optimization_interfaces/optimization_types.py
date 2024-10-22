from experience.types.enum_item import EnumItem

class CatAlgorithmType(EnumItem):
    catSimulatedAnnealing = 0
    catGradient = 1
    catCAAalgorithm = 2
    catLocalForConstraints = 3

class CatOptimizationType(EnumItem):
    catMinimum = 0
    catMaximum = 1
    catTargetValue = 2
    catOnlyBoundedVariation = 3
    catNone = 4
    catCstOnly = 5