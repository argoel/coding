class Solution(object):
    
    def dictOfStr(self, str, dict):
        for ch in str:
            if ch in dict:
                dict[ch] += 1
            else:
                dict[ch] = 1
        return dict

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        ransomNoteDict = {}
        magazineDict = {}

        ransomNoteDict = self.dictOfStr(ransomNote, ransomNoteDict)
        magazineDict = self.dictOfStr(magazine, magazineDict)

        canConstructBool = True

        for ch in ransomNoteDict.keys():
            if ch not in magazineDict:
                canConstructBool = False
                break
            elif ransomNoteDict[ch] > magazineDict[ch]:
                canConstructBool = False
                break
        
        return canConstructBool
