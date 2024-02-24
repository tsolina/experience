from experience.types.enum_item import EnumItem

class SearchCondition(EnumItem):
    SearchCondition_AND = 0
    SearchCondition_OR = 1

class SearchMode(EnumItem):
    SearchMode_Easy = 0
    SearchMode_Extended = 1
    SearchMode_Expert = 2
    SearchMode_Predefined = 3

class SearchOperator(EnumItem):
    SearchOperator_EQ = 0
    SearchOperator_NOT_EQ = 1
    SearchOperator_LIKE = 2
    SearchOperator_NOT_LIKE = 3
    SearchOperator_LT = 4
    SearchOperator_LT_EQ = 5
    SearchOperator_GT = 6
    SearchOperator_GT_EQ = 7
    SearchOperator_BETWEEN = 8
    SearchOperator_NOT_BETWEEN = 9
    SearchOperator_NULL = 10
    SearchOperator_NOT_NULL = 11

class SearchSortOrder(EnumItem):
    SearchSortOrder_Ascending = 0
    SearchSortOrder_Descending = 1    