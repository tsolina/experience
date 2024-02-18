from experience.types.enum_item import EnumItem

class CATScriptLanguage(EnumItem):
    CATVBScriptLanguage = 1
    CATVBALanguage = 2
    CATBasicScriptLanguage = 3
    CATJavaLanguage = 4
    CATJScriptLanguage = 5
    CATCSharpLanguage = 6
    CATVBNetLanguage = 7

class CatScriptLibraryType(EnumItem):
    catScriptLibraryTypeDocument = 1
    catScriptLibraryTypeDirectory = 2
    catScriptLibraryTypeVBAProject = 3
    catScriptLibraryTypeVSTAProject = 4
