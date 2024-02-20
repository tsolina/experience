from experience.types.enum_item import EnumItem

class CatPaperOrientation(EnumItem):
    catPaperPortrait = 0
    catPaperLandscape = 1
    catPaperBestFit = 2

class CatPaperSize(EnumItem):
    catPaperLetter = 0
    catPaperLegal = 1
    catPaperA0 = 2
    catPaperA1 = 3
    catPaperA2 = 4
    catPaperA3 = 5
    catPaperA4 = 6
    catPaperA = 7
    catPaperB = 8
    catPaperC = 9
    catPaperD = 10
    catPaperE = 11
    catPaperF = 12
    catPaperUser = 13

if __name__ == "__main__":
    val = CatPaperSize.catPaperA0
    print(val, val == CatPaperSize.catPaperA1, val != CatPaperSize.catPaperA1)