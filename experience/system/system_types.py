from experience.types.enum_item import EnumItem

class CATScriptLanguage(EnumItem):
    CATVBScriptLanguage = 0
    CATVBALanguage = 1
    CATBasicScriptLanguage = 2
    CATJavaLanguage = 3
    CATJScriptLanguage = 4
    CATCSharpLanguage = 5
    CATVBNetLanguage = 6

class CatScriptLibraryType(EnumItem):
    catScriptLibraryTypeDocument = 0
    catScriptLibraryTypeDirectory = 1
    catScriptLibraryTypeVBAProject = 2
    catScriptLibraryTypeVSTAProject = 3
